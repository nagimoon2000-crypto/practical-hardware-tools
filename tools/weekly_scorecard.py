"""Build a private weekly scorecard from reconciled aggregate and ledger exports."""
import argparse
import csv
import json
from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path


def rate(part, total):
    if part is None or total is None or total == 0:
        return None
    return round(part / total, 4)


def scorecard(metrics, ledger=None):
    start = date.fromisoformat(metrics["week_start"])
    end = start + timedelta(days=7)
    counts = {}
    for key in ("qualified_organic_sessions", "eligible_sessions", "result_sessions",
                "paid_cta_sessions", "payhip_product_views", "payhip_checkout_starts"):
        value = metrics.get(key)
        if value is not None and (type(value) is not int or value < 0):
            raise ValueError("Invalid count: " + key)
        counts[key] = value
    for key in ("qualified_organic_sessions", "result_sessions", "paid_cta_sessions"):
        if counts[key] is not None and counts["eligible_sessions"] is not None and counts[key] > counts["eligible_sessions"]:
            raise ValueError(key + " exceeds eligible sessions")
    report = {key: metrics.get(key) for key in ("week_start", "timezone", "product_id", "creation_minutes", "support_minutes")}
    report.update(counts)
    report.update(tool_completion_rate=rate(counts["result_sessions"], counts["eligible_sessions"]),
                  cta_click_rate=rate(counts["paid_cta_sessions"], counts["eligible_sessions"]),
                  verified_orders=None, cash_by_currency=None)
    if ledger is None:
        return report
    if metrics.get("payhip_ledger_complete") is not True:
        raise ValueError("Confirm complete Payhip reconciliation for the stated scope and week")
    seen, orders, cash = {}, set(), {}
    for row in ledger:
        day = date.fromisoformat(row["settled_date"])
        if not start <= day < end or row["product_id"] != metrics["product_id"]:
            continue
        kind, currency = row["kind"], row["currency"]
        if kind not in ("payment", "refund") or len(currency) != 3 or not currency.isascii() or not currency.isalpha() or currency != currency.upper():
            raise ValueError("Invalid settled entry")
        amount = Decimal(row["amount"])
        if not amount.is_finite() or amount <= 0 or not row["order_id"] or not row["event_id"]:
            raise ValueError("Missing settlement evidence")
        key = (kind, row["event_id"])
        if key in seen:
            if seen[key] != row:
                raise ValueError("Conflicting settlement identifier")
            continue
        seen[key] = row
        bucket = cash.setdefault(currency, dict(collected=Decimal(0), refunds=Decimal(0)))
        if kind == "payment":
            orders.add(row["order_id"])
            bucket["collected"] += amount
        else:
            bucket["refunds"] += amount
    report["verified_orders"] = len(orders)
    report["cash_by_currency"] = {
        currency: {k: str(v) for k, v in dict(bucket, net_after_refunds=bucket["collected"]-bucket["refunds"]).items()}
        for currency, bucket in cash.items()
    }
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("metrics", type=Path)
    parser.add_argument("--settled-ledger", type=Path)
    args = parser.parse_args()
    metrics = json.loads(args.metrics.read_text(encoding="utf-8-sig"))
    rows = None
    if args.settled_ledger:
        with args.settled_ledger.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if set(reader.fieldnames or []) != set("settled_date,product_id,kind,currency,amount,order_id,event_id".split(",")):
                parser.error("Unexpected ledger headers")
            rows = list(reader)
    print(json.dumps(scorecard(metrics, rows), indent=2))

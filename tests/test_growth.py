import os
import sys
import unittest
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from weekly_scorecard import scorecard


class Accounting(unittest.TestCase):
    def test_unknown_with_observed_clicks(self):
        report = scorecard(dict(week_start="2026-01-05", product_id="test", eligible_sessions=10, paid_cta_sessions=2))
        self.assertEqual(report["cta_click_rate"], 0.2)
        self.assertIsNone(report["verified_orders"])
        self.assertIsNone(report["cash_by_currency"])

    def test_settlement_reconciliation(self):
        metrics = dict(week_start="2026-01-05", product_id="test", payhip_ledger_complete=True)
        paid = dict(settled_date="2026-01-06", product_id="test", kind="payment", currency="USD", amount="10.23", order_id="fixture", event_id="a")
        refund = dict(paid, kind="refund", amount="1.11", event_id="b")
        rows = [paid, paid, refund, dict(paid, product_id="other"), dict(refund, settled_date="2026-01-12")]
        r = scorecard(metrics, rows)
        self.assertEqual(r["verified_orders"], 1)
        self.assertEqual(r["cash_by_currency"]["USD"]["net_after_refunds"], "9.12")
        with self.assertRaises(ValueError):
            scorecard(metrics, [paid, dict(paid, amount="12")])
        with self.assertRaises(ValueError):
            scorecard(dict(metrics,payhip_ledger_complete=False), [])


class MobileFunnel(unittest.TestCase):
    def test_actual_interactions(self):
        from playwright.sync_api import sync_playwright
        with sync_playwright() as runtime:
            browser = runtime.chromium.launch(executable_path=os.environ.get("CHROMIUM_BIN"))
            page = browser.new_page(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True)
            def route(req):
                url = urlsplit(req.request.url)
                if url.hostname != "site.test":
                    return req.fulfill(status=200, body="")
                path = ROOT / url.path.removeprefix("/tools/").strip("/")
                if path.is_dir():
                    path = path / "index.html"
                return req.fulfill(path=path)
            page.route("**/*", route)
            errors = []
            page.on("pageerror", lambda exc: errors.append(str(exc)))
            page.goto("https://site.test/tools/?utm_source=fixture&utm_medium=referral&utm_campaign=field&email=private")
            names = lambda: page.evaluate("Array.from(window.dataLayer || [], row => row[0] === 'event' ? row[1] : null)")
            page.locator("form[data-kind=battery] input").first.fill("1000")
            self.assertNotIn("calculator_result", names())
            page.locator("#analytics-yes").click()
            config = page.evaluate("Array.from(window.dataLayer).find(row=>row[0]==='config')[2]")
            self.assertIn("utm_campaign=field", config["page_location"])
            self.assertNotIn("email", config["page_location"])
            self.assertNotIn("calculator_result", names())
            field = page.locator("form[data-kind=battery] input").first
            field.fill("")
            self.assertNotIn("calculator_result", names())
            field.fill("2000")
            self.assertIn("calculator_result", names())
            self.assertFalse(page.locator("form[data-kind=battery] .result").evaluate("e=>e.classList.contains('invalid')"))
            self.assertAlmostEqual(page.evaluate("calculate('battery',[2000,80,20,1,10,60])[1]"), .3431666667)
            page.get_by_role("link", name="Troubleshoot an RS-485 link with the free field checklist").tap()
            page.wait_for_url("**/circuit-measurement-error-budget/#rs485-field-check")
            page.get_by_text("Termination and idle bias", exact=True).tap()
            self.assertTrue(page.get_by_text("With the bus isolated", exact=False).is_visible())
            page.evaluate("document.addEventListener('click',e=>{if(e.target.closest('a'))e.preventDefault()})")
            cta = page.locator('[data-placement=rs485_termination_example]')
            cta.locator("xpath=ancestor::details/summary").tap()
            self.assertEqual(cta.get_attribute("href").split("?")[0], "https://payhip.com/b/9PVDO")
            cta.tap()
            self.assertEqual(names().count("paid_product_link_click"), 1)
            self.assertNotIn("purchase", names())
            page.locator("#analytics-no").tap()
            cta.tap()
            self.assertEqual(names().count("paid_product_link_click"), 1)
            self.assertEqual(errors, [])
            browser.close()

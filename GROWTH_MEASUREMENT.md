# RS-485 offer experiment

The home link opens an un-gated field checklist at `circuit-measurement-error-budget/#rs485-field-check`. A visitor can test polarity, isolate duplicate addresses and compare termination readings before opening the existing RS485 Troubleshooting Checklist & Test Pack (Payhip ID `bcfR4`). The separate parallel-termination calculation workbook is `9PVDO`. The free field checklist is the HTML on this site. The new CTA makes no claim about a downloadable sample, current price or repair outcome.

Product audit: the November 5 storefront audit recorded both product titles at their Payhip URLs. The October 17 creation record for bcfR4 initially showed hidden visibility. A fresh anonymous HTTP check received a Cloudflare challenge. Before adding the direct troubleshooting-pack CTA, open its destination as a buyer, verify visibility, contents, current price and terms, and that checkout opens. Keep test activity out of the sales report.

## Measure the path

GA4 starts after consent. Configuration sends a page view with an origin-only referrer and a landing URL retaining only syntactically valid utm_source, utm_medium and utm_campaign. Use controlled campaign slugs with no personal identifiers. Use GA4 acquisition dimensions to group sessions. The outbound CTA carries its own stable referral campaign. Browser and consent restrictions limit measured coverage.

Use the GA4 page_view for eligible page views. calculator_result records a valid interactive result on the supported calculators. Repeated edits can create multiple events. paid_product_link_click records activation of links to identified paid product IDs. The existing product_click also covers free product links; never add these event counts together. Register product_id and placement as event-scoped custom dimensions. Turn off automatic form interaction and outbound-link measurement if unneeded; review enhanced measurement and URL redaction in the stream before launch.

## Weekly private report

Copy tools/week.template.json outside the repository. Set the seven-day period start, reporting timezone and one product ID. Use distinct GA4 sessions eligible for that offer and use the same page filter, dates and acquisition dimensions for the numerator. Count sessions with at least one valid result and sessions with at least one matching paid CTA click separately. For an editorial checklist with no calculator, leave the result-session field null. Supply Payhip product page views and checkout starts only when the seller report supports that product and date scope. Record creation and support minutes from actual time records.

Run `python tools/weekly_scorecard.py PRIVATE/week.json`. Missing observations and rates with no denominator stay null. To report money, reconcile successful, settled payments and actual refunds to Payhip records in the reporting timezone. Exclude pending, failed, test, unpaid and abandoned attempts. Keep private order evidence outside Git and GitHub Pages. Prepare a private CSV with exactly these headers:

    settled_date,product_id,kind,currency,amount,order_id,event_id

Use ISO dates, payment or refund, uppercase currency, positive decimal amounts and stable transaction/refund IDs. For a multi-product order use only the amount allocated to the chosen product. Use a single row per settled movement for that product. Convert timestamps to the selected timezone before extracting dates. Set payhip_ledger_complete to true only after checking the full week. Run `python tools/weekly_scorecard.py PRIVATE/week.json --settled-ledger PRIVATE/ledger.csv`. Net after refunds excludes fees, taxes and operating costs. Refunds use their actual settlement week. An omitted ledger gives unknown revenue even when clicks were recorded. Raw customer records never belong in the public repository.

For local tests install Python Playwright in a development environment, run `python -m playwright install chromium`, then `python -m unittest discover -s tests -v`. CHROMIUM_BIN may point to an installed headless Chromium. Browser tests use isolated fixture routes and do not contact Payhip or GA4.

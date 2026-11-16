# iPhone location changer comparison dataset

An open, machine-readable comparison of tools that change the location an
iPhone reports. Each value comes from the vendor's own public page, with the
source URL and the date it was checked.

> **Disclosure:** Made by Roam (roamlocation.com), one of the tools listed.
> Data is from vendors' public pages; corrections via issues/PR welcome.

- Human-readable comparison: [Best iPhone location changer](https://roamlocation.com/guides/best-iphone-location-changer)
- Last checked: **2026-11-16**
- License: [CC BY 4.0](LICENSE), attribution: **Roam - roamlocation.com**

## Files

| File | Contents |
| --- | --- |
| `data/tools.csv` | One row per tool, all fields below. |
| `data/tools.json` | The same rows as JSON, plus dataset metadata. |
| `data/facts.csv` | Long format: one fact per row (`tool_id`, `field`, `value`, `source_urls`, `checked_date`). |
| `data/sources.csv` | Every source URL, its publisher, and which facts it supports. |
| `scripts/build.py` | Generates all data files from one source table. |

## Tools covered (11)

Roam, Geovo, GFaker, Mirage, Locus, Roam Control, Tenorshare iAnyGo,
iMyFone AnyTo, iToolab AnyGo, Dr.Fone Virtual Location, 3uTools (Virtual
Location).

Roam and Roam Control are different products from different makers.

## Methodology

1. The same questions are asked for every tool: does it need a computer or a
   jailbreak, does it run on the iPhone itself, which iOS versions does it
   name, does it work on mobile data, does it offer routes, a joystick and GPX
   import, what does it cost, and what is the refund policy.
2. Answers are copied from the vendor's official website, product page, buy
   page, or project README, read on the check date. Nothing was bought or
   tested hands-on for this dataset.
3. If a page does not state something, the value is `unknown`. `unknown`
   means "not found on the pages checked", not "does not exist".
4. If two official pages of the same vendor disagree, both statements are
   recorded.
5. Prices are copied as displayed, including any discount framing (for
   example "shown beside a higher crossed-out price"). Prices change often and
   may be time-limited; check the vendor's site before buying.
6. No scores, rankings, review counts, user counts or awards are included.
7. Where a vendor page blocked automated reading on the check date, the
   values are taken from the Roam comparison page that recorded them from that
   vendor page the same day, and the row's `verification` field says so.

## Field definitions

| Field | Meaning |
| --- | --- |
| `id` | Stable identifier. |
| `name`, `vendor` | Product name and the company or project behind it. |
| `product_type` | iPhone app, desktop program, hardware device, etc. |
| `needs_computer` | Whether a Mac/Windows/Linux computer is part of setup or use: `yes`, `no`, `partial` (with the stated detail), or `unknown`. |
| `needs_jailbreak` | `yes`, `no` or `unknown`, as stated by the vendor. |
| `runs_on_iphone_itself` | Whether the location change is controlled from an app on the iPhone. |
| `min_ios` | Lowest iOS version named by the vendor. |
| `supported_ios` | The iOS (and where relevant desktop OS) range as worded by the vendor. |
| `android_support` | Whether the vendor names Android support. |
| `works_on_mobile_data` | Whether the vendor states it works on cellular/mobile data, not only Wi-Fi. |
| `route_support` | Movement along a route or between several points, if stated. |
| `joystick_support` | Live joystick movement, if stated. |
| `gpx_import` | Import of GPX route files, if stated. |
| `pricing_model` | Subscription, pass, one-time, lifetime, or no paid plan listed. |
| `cheapest_paid_option` | Lowest listed paid price, with its period, as displayed. |
| `price_currency` | ISO currency of the listed prices. |
| `refund_policy_summary` | Short paraphrase of the vendor's stated refund or money-back terms. |
| `notes` | Other sourced details that affect setup or use. |
| `official_url` | Vendor's main page for the product. |
| `source_urls` | Pages the row's values come from (`;`-separated in CSV, a list in JSON). |
| `checked_date` | Date the sources were read (YYYY-MM-DD). |
| `verification` | `vendor_page_rechecked` or `via_comparison_page_same_day`. |

## Update cadence

Re-checked monthly, and sooner when a vendor changes prices or iOS support.
Each update bumps the version in `CITATION.cff`, updates `checked_date`, and
adds an entry to `CHANGELOG.md`.

## Corrections

If a value is wrong or out of date, open an issue or pull request with a link
to the vendor's official page that shows the correct information. Vendor
pages take precedence over this dataset.

## Citing

Use GitHub's "Cite this repository" button (from `CITATION.cff`), or:

> Roam - roamlocation.com. *iPhone location changer comparison dataset*,
> version 1.0.0, checked 2026-11-16. CC BY 4.0.

## Trademarks and affiliation

All product names, including Geovo, GFaker, Mirage, Locus, Roam Control,
Tenorshare iAnyGo, iMyFone AnyTo, iToolab AnyGo, Dr.Fone and 3uTools, are
trademarks of their respective owners. They are used here only to identify
the products. Roam has no affiliation with, and is not endorsed by, any of
them or by Apple. iPhone and iOS are trademarks of Apple Inc.

## Responsible use

A changed location can mislead people who rely on knowing where you are. Do
not use it to deceive anyone or to commit fraud.

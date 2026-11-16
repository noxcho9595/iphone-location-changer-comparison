#!/usr/bin/env python3
"""Builds data/tools.csv, data/tools.json, data/facts.csv and data/sources.csv
from the single source of truth in this file (TOOLS + SOURCES).
Every value in TOOLS is traceable to a source id in SOURCES."""
import csv, json, pathlib

CHECKED = "2026-11-16"
ROOT = pathlib.Path(__file__).resolve().parent.parent
HUB = "https://roamlocation.com/guides/best-iphone-location-changer"

# id: (url, publisher, type, supports)
SOURCES = {
 "roam-home": ("https://roamlocation.com/", "Roam (BLOCC)", "vendor_official",
   "Roam: no computer, no jailbreak, iOS 27 or newer, Developer Mode, Wi-Fi and mobile data (4G/5G), routes and joystick, restart restores real location, pass prices EUR 4.99 to 49.99"),
 "roam-terms": ("https://roamlocation.com/terms", "Roam (BLOCC)", "vendor_official",
   "Roam: pass lengths 1, 7, 30 or 365 days; iOS 27 or newer and Developer Mode; money back if Roam doesn't work on your iPhone and you tell them within 7 days of paying"),
 "roam-hub": (HUB, "Roam (BLOCC)", "comparison_page",
   "Roam comparison hub: Roam GPX import not included; one-to-one notes for every tool; GFaker figures as read on 2026-11-16"),
 "roam-vs-gfaker": ("https://roamlocation.com/guides/roam-vs-gfaker", "Roam (BLOCC)", "comparison_page",
   "GFaker figures as read from gfaker.com on 2026-11-16 (homepage and GF II page)"),
 "roam-vs-mirage-locus": ("https://roamlocation.com/guides/roam-vs-mirage-locus", "Roam (BLOCC)", "comparison_page",
   "Roam Control is a separate project, not made or sold by BLOCC"),
 "geovo-home": ("https://geovo.app/", "Geovo", "vendor_official",
   "Geovo: Mac/Windows computer and cable for setup, iPhone app continues on Wi-Fi or cellular, renew from computer every 7 days or automatically, iOS 17.4+, macOS 13+, Windows 10/11, not Android, no jailbreak, teleport/drive/joystick, GPX and KML, Pro prices, 15-minute account trial, refund lines (FAQ is on the homepage)"),
 "gfaker-home": ("https://www.gfaker.com/", "GFaker", "vendor_official",
   "GFaker: hardware, no computer, no jailbreak, iOS 9 to iOS 27, single-spot and multi-spot movement, one-time payment, seven-day return (automated re-fetch blocked by a captcha on 2026-11-16; values as recorded on roamlocation.com/guides/roam-vs-gfaker the same day)"),
 "gfaker-gf2": ("https://www.gfaker.com/product/gfaker-gf/", "GFaker", "vendor_official",
   "GFaker GF II: $469.00 to $479.00, iOS 9 through iOS 26.6.2, no computer, no jailbreak (automated re-fetch blocked by a captcha on 2026-11-16; values as recorded on roamlocation.com/guides/roam-vs-gfaker the same day)"),
 "mirage-readme": ("https://github.com/xXWapixelXx/Mirage-updates", "Mirage project (GitHub)", "project_readme",
   "Mirage: iOS 18 to 27, no computer on iOS 27, one-time computer pairing step on iOS 18-26, joystick, routes, GPX import/export, mobile data, sideloaded, invite-only, README says it is free and sponsorship unlocks nothing"),
 "locus-readme": ("https://github.com/ChrisMack32/Locus", "Locus project (GitHub)", "project_readme",
   "Locus: free and open source (MIT), on-device pairing on iOS 27, RPPairing file once on iOS 18-26, LocalDevVPN, joystick, routes on roads, draw a path, GPX import/export, start on Wi-Fi then can continue on cellular"),
 "roamcontrol-readme": ("https://github.com/seanhowarthdev/Roam-Control", "Roam Control project (GitHub)", "project_readme",
   "Roam Control: requires iOS 27+, on-device pairing, LocalDevVPN for Wi-Fi and mobile data, fixed location, routes, joystick, GPX import/export, prebuilt IPA via SideStore or LiveContainer, source not publicly distributed, no price stated"),
 "ianygo-product": ("https://www.tenorshare.com/products/ianygo-change-gps-location-iphone.html", "Tenorshare", "vendor_official",
   "iAnyGo: no jailbreak/root, iOS 14 - iOS 27 or later, Android 4 to 17, joystick, routes up to 99 points, GPX, no computer required after installation, 1-hour try"),
 "ianygo-buy": ("https://www.tenorshare.com/purchase/buy-ianygo-ios-app.html", "Tenorshare", "vendor_official",
   "iAnyGo iOS app: $14.99/month for 1 iOS device (tax excl.), quarter/year/lifetime plans, 30-day money-back guarantee if there is no solution after they analyse the problem"),
 "anyto-product": ("https://www.imyfone.com/location-changer/", "iMyFone", "vendor_official",
   "AnyTo: from $14.99, no jailbreak/root, iOS 5 and up (iOS 27 included), Android 6.0 and up (Android 17 included), Windows 7-11, macOS 10.9-14, joystick, routes, GPX"),
 "anyto-buy": ("https://www.imyfone.com/location-changer/purchase/", "iMyFone", "vendor_official",
   "AnyTo: cancel anytime, 30-day money back guarantee if they cannot help solve the technical problems"),
 "anygo-product": ("https://itoolab.com/gps-location-changer/", "iToolab", "vendor_official",
   "AnyGo: desktop $9.95/month shown beside $19.95, iOS app $19.95/month, Android app $14.95/month, iOS 7.0 - iOS 27, Android 7.0 - 17, no jailbreak/root, joystick, routes, GPX"),
 "anygo-buy": ("https://itoolab.com/buy/anygo-for-ios?lang=en", "iToolab", "vendor_official",
   "AnyGo for iOS: 1 month $19.95, quarter $39.95, year $79.95 (tax excl.), 5 iOS devices, Windows and Mac included, 30-day money-back guarantee"),
 "drfone-product": ("https://drfone.wondershare.com/virtual-location-changer.html", "Wondershare", "vendor_official",
   "Dr.Fone Virtual Location: computer program, Wi-Fi/USB connection (iPhone Wi-Fi after one connection), no jailbreak/root, iOS 27 and Android 16, iOS 5.0 and later, joystick, multi-stop routes, GPX"),
 "drfone-buy": ("https://drfone.wondershare.com/buy/drfone-ios-virtual-location.html", "Wondershare", "vendor_official",
   "Dr.Fone Virtual Location: monthly $4.97 beside $14.95 under a 66% off banner, quarterly $9.97, annually $19.97, plans list iOS 26 and Android 16, up to a 7-day money-back guarantee, 2-hour trial"),
 "3u-home": ("https://www.3u.com/", "3uTools", "vendor_official",
   "3uTools: computer program (PC client) for iPhone management"),
 "3u-tutorial": ("https://www.3u.com/tutorial/articles/12076/how-to-change-location-by-virtual-location-on-3utools", "3uTools", "vendor_official",
   "3uTools Virtual Location: open the PC client, connect the device via USB cable, Toolbox > Virtual Location, modify one virtual location; no price stated"),
}

U = "unknown"
TOOLS = [
 dict(id="roam", name="Roam", vendor="BLOCC", product_type="iPhone app",
  needs_computer="no", needs_jailbreak="no", runs_on_iphone_itself="yes",
  min_ios="27", supported_ios="iOS 27 or newer; Developer Mode must be on", android_support="no",
  works_on_mobile_data="yes", route_support="yes", joystick_support="yes", gpx_import="no",
  pricing_model="fixed-length pass (1, 7, 30 or 365 days), one iPhone per pass",
  cheapest_paid_option="4.99 (day pass); week 9.99, month 14.99, year 49.99", price_currency="EUR",
  refund_policy_summary="Money back only if Roam doesn't work on your iPhone and you ask within 7 days of paying.",
  notes="Not on the App Store; installed from a personal link tied to the iPhone. A restart restores the real location. Listed by the dataset maintainer (see README disclosure).",
  official_url="https://roamlocation.com/", sources=["roam-home","roam-terms","roam-hub"], verification="vendor_page_rechecked"),
 dict(id="geovo", name="Geovo", vendor="Geovo", product_type="Mac/Windows app + iPhone app",
  needs_computer="yes", needs_jailbreak="no", runs_on_iphone_itself="partial",
  min_ios="17.4", supported_ios="iOS 17.4 or later (iPhone XS/XR and newer), iPad; macOS 13+, Windows 10/11", android_support="no",
  works_on_mobile_data="yes", route_support="yes", joystick_support="yes", gpx_import="yes",
  pricing_model="subscription or lifetime (Pro)", cheapest_paid_option="6.99 per week (Pro); also 12.99/month, 29.99/3 months, 79.99/year, 129.99 lifetime", price_currency="USD",
  refund_policy_summary="Page states: refund if it can't work on your iPhone (within 14 days, with support); also: refunds if you haven't used Geovo since buying. See their Refund Policy.",
  notes="Setup from a Mac or Windows PC with a cable; the iPhone app then continues on Wi-Fi or cellular and is renewed from the computer every 7 days, or automatically. One 15-minute account trial per their FAQ. Pro covers 2 computers and 2 iPhones.",
  official_url="https://geovo.app/", sources=["geovo-home"], verification="vendor_page_rechecked"),
 dict(id="gfaker", name="GFaker", vendor="GFaker", product_type="hardware device",
  needs_computer="no", needs_jailbreak="no", runs_on_iphone_itself="no (external hardware device)",
  min_ios="9", supported_ios="Homepage: iOS 9 to iOS 27. GF II product page: iOS 9 through iOS 26.6.2. The pages disagree.", android_support=U,
  works_on_mobile_data=U, route_support="yes", joystick_support=U, gpx_import=U,
  pricing_model="one-time hardware purchase", cheapest_paid_option="469.00 (GF II page range 469.00-479.00; no separate price per model in page text)", price_currency="USD",
  refund_policy_summary="Seven-day no-reason return, per their FAQ.",
  notes="Single-spot and multi-spot movement with a set speed. Vendor pages blocked automated re-fetch on 2026-11-16; values are as recorded from their pages on roamlocation.com/guides/roam-vs-gfaker the same day.",
  official_url="https://www.gfaker.com/", sources=["gfaker-home","gfaker-gf2","roam-vs-gfaker"], verification="via_comparison_page_same_day"),
 dict(id="mirage", name="Mirage", vendor="Mirage project (GitHub)", product_type="sideloaded iPhone app",
  needs_computer="no on iOS 27; one-time computer step on iOS 18-26", needs_jailbreak="no", runs_on_iphone_itself="yes",
  min_ios="18", supported_ios="iOS 18 to 27, tested on iOS 27", android_support=U,
  works_on_mobile_data="yes", route_support="yes", joystick_support="yes", gpx_import="yes",
  pricing_model="no paid plan listed; README says it is free and optional sponsorship unlocks nothing", cheapest_paid_option="none listed", price_currency="",
  refund_policy_summary="not applicable (no paid plan listed)",
  notes="Invite-only access per README. Installed by sideloading (SideStore/AltStore or a signed build).",
  official_url="https://github.com/xXWapixelXx/Mirage-updates", sources=["mirage-readme"], verification="vendor_page_rechecked"),
 dict(id="locus", name="Locus", vendor="Locus project (GitHub, open source)", product_type="sideloaded iPhone app (open source, MIT)",
  needs_computer="no on iOS 27; pairing file from a computer once on iOS 18-26", needs_jailbreak=U, runs_on_iphone_itself="yes",
  min_ios="18", supported_ios="iOS 27 with on-device pairing; iOS 18-26 with an RPPairing file", android_support=U,
  works_on_mobile_data="yes (start on Wi-Fi first, then the session can continue on cellular)", route_support="yes", joystick_support="yes", gpx_import="yes",
  pricing_model="no paid plan listed; README says free and open source (MIT)", cheapest_paid_option="none listed", price_currency="",
  refund_policy_summary="not applicable (no paid plan listed)",
  notes="Also requires the LocalDevVPN app. Prebuilt IPA or build from source.",
  official_url="https://github.com/ChrisMack32/Locus", sources=["locus-readme"], verification="vendor_page_rechecked"),
 dict(id="roam-control", name="Roam Control", vendor="Roam Control project (GitHub)", product_type="sideloaded iPhone app (proprietary)",
  needs_computer=U, needs_jailbreak=U, runs_on_iphone_itself="yes",
  min_ios="27", supported_ios="iOS 27+", android_support=U,
  works_on_mobile_data="yes", route_support="yes", joystick_support="yes", gpx_import="yes",
  pricing_model=U, cheapest_paid_option=U, price_currency="",
  refund_policy_summary=U,
  notes="Separate project; not Roam and not made or sold by BLOCC. README describes on-device pairing and installation via SideStore or LiveContainer; whether a computer is needed is not stated. Price not stated.",
  official_url="https://github.com/seanhowarthdev/Roam-Control", sources=["roamcontrol-readme","roam-vs-mirage-locus"], verification="vendor_page_rechecked"),
 dict(id="tenorshare-ianygo", name="Tenorshare iAnyGo", vendor="Tenorshare", product_type="Windows/Mac program + iOS and Android apps",
  needs_computer="partial: steps start on the computer; page says no computer required after installation", needs_jailbreak="no", runs_on_iphone_itself="yes, after a computer-assisted install",
  min_ios="14", supported_ios="Product page: iOS 14 - iOS 27 or later. 1-device buy plans: iOS 14 to iOS 26 or later, excluding iOS 17.0 and 17.1.", android_support="yes",
  works_on_mobile_data=U, route_support="yes (up to 99 points)", joystick_support="yes", gpx_import="yes",
  pricing_model="subscription or lifetime", cheapest_paid_option="14.99 per month (iOS app, 1 device, tax excl.)", price_currency="USD",
  refund_policy_summary="30-day money-back guarantee if there is no solution after they analyse the problem; see their refund policy.",
  notes="Product page offers trying it for 1 hour. Desktop plans are priced separately.",
  official_url="https://www.tenorshare.com/products/ianygo-change-gps-location-iphone.html", sources=["ianygo-product","ianygo-buy"], verification="vendor_page_rechecked"),
 dict(id="imyfone-anyto", name="iMyFone AnyTo", vendor="iMyFone", product_type="Windows/Mac program + iOS and Android apps",
  needs_computer="partial: iPhone steps get the app through the desktop program; page also says it can be used without a PC", needs_jailbreak="no", runs_on_iphone_itself="yes (iOS app)",
  min_ios="5", supported_ios="iOS 5 and up (iOS 27 included); Windows 7-11, macOS 10.9-14", android_support="yes",
  works_on_mobile_data=U, route_support="yes", joystick_support="yes", gpx_import="yes",
  pricing_model="subscription", cheapest_paid_option="from 14.99 (product page); purchase-page plan amounts not in page text", price_currency="USD",
  refund_policy_summary="Cancel anytime; 30-day money back guarantee if they cannot help solve the technical problem.",
  notes="",
  official_url="https://www.imyfone.com/location-changer/", sources=["anyto-product","anyto-buy"], verification="vendor_page_rechecked"),
 dict(id="itoolab-anygo", name="iToolab AnyGo", vendor="iToolab", product_type="Windows/Mac program + iOS and Android apps",
  needs_computer="yes for desktop steps; an iOS app is sold separately", needs_jailbreak="no", runs_on_iphone_itself="yes (iOS app)",
  min_ios="7.0", supported_ios="iOS 7.0 - iOS 27", android_support="yes",
  works_on_mobile_data=U, route_support="yes", joystick_support="yes", gpx_import="yes",
  pricing_model="subscription or lifetime", cheapest_paid_option="9.95 per month (desktop, shown beside 19.95); iOS app 19.95 per month", price_currency="USD",
  refund_policy_summary="30-day money-back guarantee; whole-order refunds within the guarantee period, no partial OS refunds.",
  notes="iOS buy page: 1 month 19.95, quarter 39.95, year 79.95 (tax excl.), 5 iOS devices, Windows and Mac included.",
  official_url="https://itoolab.com/gps-location-changer/", sources=["anygo-product","anygo-buy"], verification="vendor_page_rechecked"),
 dict(id="drfone-virtual-location", name="Dr.Fone Virtual Location", vendor="Wondershare", product_type="Windows/Mac program",
  needs_computer="yes", needs_jailbreak="no", runs_on_iphone_itself="no (desktop connection described for iPhone)",
  min_ios="5.0", supported_ios="Product page: iOS 5.0 and later, compatible with iOS 27. Buy-page plans: iOS 26.", android_support="yes",
  works_on_mobile_data=U, route_support="yes", joystick_support="yes", gpx_import="yes",
  pricing_model="subscription or perpetual", cheapest_paid_option="4.97 per month (monthly plan, shown beside 14.95 under a 66% off banner)", price_currency="USD",
  refund_policy_summary="Up to a 7-day money-back guarantee, under the circumstances they accept.",
  notes="iPhone connects by USB, or by Wi-Fi after one earlier connection. 2-hour trial per buy page.",
  official_url="https://drfone.wondershare.com/virtual-location-changer.html", sources=["drfone-product","drfone-buy"], verification="vendor_page_rechecked"),
 dict(id="3utools", name="3uTools (Virtual Location)", vendor="3uTools", product_type="computer program (iPhone management)",
  needs_computer="yes", needs_jailbreak=U, runs_on_iphone_itself="no",
  min_ios=U, supported_ios=U, android_support=U,
  works_on_mobile_data=U, route_support=U, joystick_support=U, gpx_import=U,
  pricing_model=U, cheapest_paid_option="not listed on the pages checked", price_currency="",
  refund_policy_summary=U,
  notes="Tutorial: open the PC client, connect via USB cable, Toolbox > Virtual Location, set one modified location.",
  official_url="https://www.3u.com/", sources=["3u-home","3u-tutorial"], verification="vendor_page_rechecked"),
]

FIELDS = ["id","name","vendor","product_type","needs_computer","needs_jailbreak","runs_on_iphone_itself",
 "min_ios","supported_ios","android_support","works_on_mobile_data","route_support","joystick_support","gpx_import",
 "pricing_model","cheapest_paid_option","price_currency","refund_policy_summary","notes",
 "official_url","source_urls","checked_date","verification"]
FACT_FIELDS = FIELDS[4:18]

def main():
    rows=[]
    for t in TOOLS:
        assert all(s in SOURCES for s in t["sources"]), t["id"]
        r={k:t.get(k,"") for k in FIELDS}
        r["source_urls"]=" ; ".join(SOURCES[s][0] for s in t["sources"])
        r["checked_date"]=CHECKED
        rows.append(r)
    d=ROOT/"data"
    with open(d/"tools.csv","w",newline="") as f:
        w=csv.DictWriter(f,FIELDS); w.writeheader(); w.writerows(rows)
    out=[]
    for t,r in zip(TOOLS,rows):
        o={k:r[k] for k in FIELDS if k not in ("source_urls",)}
        o["source_urls"]=[SOURCES[s][0] for s in t["sources"]]
        out.append(o)
    meta={"name":"iPhone location changer comparison","version":"1.0.0","checked_date":CHECKED,
          "license":"CC-BY-4.0","attribution":"Roam - roamlocation.com","made_by":"Roam (roamlocation.com), one of the tools listed",
          "comparison_hub":HUB,"tools":out}
    (d/"tools.json").write_text(json.dumps(meta,indent=2,ensure_ascii=False)+"\n")
    with open(d/"facts.csv","w",newline="") as f:
        w=csv.writer(f); w.writerow(["tool_id","field","value","source_urls","checked_date"])
        for t,r in zip(TOOLS,rows):
            for k in FACT_FIELDS:
                w.writerow([t["id"],k,r[k],r["source_urls"],CHECKED])
    with open(d/"sources.csv","w",newline="") as f:
        w=csv.writer(f); w.writerow(["source_id","url","publisher","source_type","supports","used_by_tool_ids","checked_date"])
        for sid,(url,pub,typ,sup) in SOURCES.items():
            used=",".join(t["id"] for t in TOOLS if sid in t["sources"])
            w.writerow([sid,url,pub,typ,sup,used,CHECKED])
    print(len(rows),"tools,",len(SOURCES),"sources")
main()

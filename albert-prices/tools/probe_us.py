"""Probe how albertlevi.com presents prices/sizes to a US shopper (runs on GitHub Actions, US IP)."""
import json, os, urllib.request, http.cookiejar
OUT = "albert-prices/tools/probe"
os.makedirs(OUT, exist_ok=True)
H = "limited-edition-print-tree-of-life-blue-life"
UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148 Safari/604.1"
cases = {
  "plain_js": f"https://www.albertlevi.com/products/{H}.js",
  "enus_js": f"https://www.albertlevi.com/en-us/products/{H}.js",
  "cur_js": f"https://www.albertlevi.com/products/{H}.js?currency=USD",
  "enus_json": f"https://www.albertlevi.com/en-us/products/{H}.json",
  "enus_list": "https://www.albertlevi.com/en-us/products.json?limit=3",
  "page": f"https://www.albertlevi.com/products/{H}",
  "enus_page": f"https://www.albertlevi.com/en-us/products/{H}",
  "meta": "https://www.albertlevi.com/meta.json",
  "browsing_ctx": "https://www.albertlevi.com/browsing_context_suggestions.json",
}
log = []
for name, url in cases.items():
    for ck in ("", "cart_currency=USD; localization=US"):
        hdr = {"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"}
        if ck: hdr["Cookie"] = ck
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=hdr), timeout=60) as r:
                body = r.read()
                fn = f"{OUT}/{name}{'_ck' if ck else ''}.txt"
                open(fn, "wb").write(body)
                log.append(f"ok {name}{'_ck' if ck else ''} {r.status} {len(body)} {r.geturl()}")
        except Exception as e:
            log.append(f"fail {name}{'_ck' if ck else ''} {e}")
open(f"{OUT}/log.txt", "w").write("\n".join(log) + "\n")
print("\n".join(log))

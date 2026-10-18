"""Fetch the live catalog as a US shopper sees it (runs on GitHub Actions, US IP)."""
import json, os, urllib.request
OUT = "albert-prices/tools"
UA = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148 Safari/604.1", "Accept-Language": "en-US,en;q=0.9"}
def get(u):
    with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60) as r:
        return r.read()
prods, page = [], 1
while True:
    b = json.loads(get(f"https://www.albertlevi.com/products.json?limit=250&page={page}"))["products"]
    if not b: break
    prods += b; page += 1
json.dump({"products": prods}, open(f"{OUT}/products-live.json", "w"), ensure_ascii=False)
# the storefront .js endpoint is what the product page renders from; keep it per product for comparison
js = {}
for p in prods:
    try: js[p["handle"]] = json.loads(get(f"https://www.albertlevi.com/products/{p['handle']}.js"))
    except Exception as e: js[p["handle"]] = {"error": str(e)}
json.dump(js, open(f"{OUT}/products-js.json", "w"), ensure_ascii=False)
print(len(prods), "products")

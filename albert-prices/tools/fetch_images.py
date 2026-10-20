"""Download the store catalog and one 480px thumbnail per product (runs on GitHub Actions)."""
import json, os, urllib.request

BASE = "https://www.albertlevi.com/products.json?limit=250&page=%d"
OUT = "albert-prices/img"
os.makedirs(OUT, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (price-guide image sync)"}

def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        return r.read()

products, page = [], 1
while True:
    batch = json.loads(get(BASE % page))["products"]
    if not batch:
        break
    products += batch
    page += 1
json.dump({"products": products}, open("albert-prices/tools/products.json", "w"), ensure_ascii=False)

log = []
for p in products:
    if not p.get("images"):
        log.append(f"no-image {p['handle']}")
        continue
    src = p["images"][0]["src"]
    url = src + ("&" if "?" in src else "?") + "width=480"
    try:
        data = get(url)
        open(f"{OUT}/{p['handle']}.jpg", "wb").write(data)
        log.append(f"ok {p['handle']} {len(data)}")
    except Exception as e:  # keep going; one failed image should not stop the rest
        log.append(f"fail {p['handle']} {e}")
open("albert-prices/tools/fetch-log.txt", "w").write("\n".join(log) + "\n")
print(len(products), "products;", sum(l.startswith("ok") for l in log), "images")

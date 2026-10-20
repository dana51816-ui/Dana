"""Download up to 5 sharp images per artwork (product photos, flat scans, room shots) at 760px. Runs on GitHub Actions."""
import json, os, urllib.request
OUT = "albert-prices/tools/raw"
prods = {p["handle"]: p for p in json.load(open("albert-prices/tools/products-live.json"))["products"]}
arts = json.load(open("albert-prices/tools/art-handles.json"))
UA = {"User-Agent": "Mozilla/5.0 (price-guide image sync)"}
log = []
for a in arts:
    seen, imgs = set(), []
    for h in a["handles"]:
        for im in prods.get(h, {}).get("images", []):
            base = im["src"].split("?")[0]
            if base in seen: continue
            seen.add(base); imgs.append(im)
    os.makedirs(f"{OUT}/{a['id']}", exist_ok=True)
    for i, im in enumerate(imgs[:5]):
        url = im["src"] + ("&" if "?" in im["src"] else "?") + "width=760"
        name = im["src"].split("/")[-1].split("?")[0][:60]
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                open(f"{OUT}/{a['id']}/{i}.jpg", "wb").write(r.read())
            log.append(f"ok {a['id']} {i} {im['width']}x{im['height']} {name}")
        except Exception as e:
            log.append(f"fail {a['id']} {i} {e}")
open(f"{OUT}/log.txt", "w").write("\n".join(log) + "\n")
print(len(log))

# Pull Albert's logo files from his store at full resolution.
import os,urllib.request
OUT='albert-prices/tools/logo';os.makedirs(OUT,exist_ok=True)
UA={'User-Agent':'Mozilla/5.0 (Macintosh) AppleWebKit/537.36 Chrome/120 Safari/537.36'}
for n in ('1','2'):
    for q in ('','?width=2000'):
        u=f'https://www.albertlevi.com/cdn/shop/files/FINAL_LOGO_RESPONSIVE-{n}.png'+q
        try:
            b=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30).read()
            open(f'{OUT}/logo-{n}{"-w2000" if q else ""}.png','wb').write(b);print(u,len(b))
        except Exception as e:print(u,e)

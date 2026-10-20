# Pull Albert's logo from his store: header logo, favicon and apple-touch-icon, plus the raw header HTML for reference.
import re,os,urllib.request,json,html
OUT='albert-prices/tools/logo';os.makedirs(OUT,exist_ok=True)
UA={'User-Agent':'Mozilla/5.0 (Macintosh) AppleWebKit/537.36 Chrome/120 Safari/537.36'}
def get(u):return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30).read()
found={}
for page in ['https://www.albertlevi.com/','https://www.albertlevi.com/en']:
    try:h=get(page).decode('utf-8','ignore')
    except Exception as e:print(page,e);continue
    open(f'{OUT}/home{len(found)}.html','w').write(h)
    hdr=h[:200000]
    for m in re.finditer(r'<img[^>]+>',hdr):
        tag=m.group(0)
        if re.search(r'logo',tag,re.I):
            for s in re.findall(r'(?:src|srcset)="([^"]+)"',tag):
                for u in s.split(','):found.setdefault(u.strip().split(' ')[0],'logo')
    for m in re.finditer(r'<link[^>]+rel="[^"]*(icon|apple-touch-icon)[^"]*"[^>]*>',hdr):
        u=re.search(r'href="([^"]+)"',m.group(0))
        if u:found.setdefault(u.group(1),m.group(1))
    for u in re.findall(r'(?:https:)?//[^"\'\s]+logo[^"\'\s]*\.(?:png|svg|jpg|jpeg|webp)[^"\'\s]*',hdr,re.I):found.setdefault(u,'logo-ref')
    for s in re.findall(r'<svg[^>]*class="[^"]*logo[^"]*"[\s\S]*?</svg>',hdr,re.I)[:3]:
        open(f'{OUT}/inline{len(os.listdir(OUT))}.svg','w').write(s)
rep=[]
for i,(u,k) in enumerate(list(found.items())[:30]):
    full=html.unescape(u);full='https:'+full if full.startswith('//') else full
    if full.startswith('/'):full='https://www.albertlevi.com'+full
    full=re.sub(r'([?&])width=\d+','\\1width=1200',full)
    try:
        b=get(full);ext=re.search(r'\.(png|svg|jpg|jpeg|webp|ico|gif)',full.split('?')[0],re.I);ext=ext.group(1) if ext else 'bin'
        fn=f'{OUT}/{i:02d}-{k}.{ext}';open(fn,'wb').write(b);rep.append((fn,full,len(b)))
    except Exception as e:rep.append((None,full,str(e)))
json.dump(rep,open(f'{OUT}/report.json','w'),indent=1);print(json.dumps(rep,indent=1))

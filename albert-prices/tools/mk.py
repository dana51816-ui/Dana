import sys,json,os
tpl,data,outdir,preview=sys.argv[1:5]
t=open(tpl).read()
_dd=json.load(open(data))
_op=os.path.join(outdir,'tools','originals-prices.json')
if os.path.exists(_op):
    _o=json.load(open(_op));_dd['OS0']=_o.get('OS',[]);_dd['ORIG0']=_o.get('ORIG',{})
    import hashlib as _h;_dd['OSV']=_h.sha1(json.dumps(_o,sort_keys=True).encode()).hexdigest()[:8]
_tp=os.path.join(outdir,'tools','tour.json')
if os.path.exists(_tp):
    import re as _re,hashlib as _h2
    _t=json.load(open(_tp));_ids={_re.sub(r'[^a-z0-9]+','-',a['k']):a for a in _dd['art']}
    for r in _t['list']:
        if r['new'] and r['id'] not in _ids:
            n=r['new']['n'];w,h=map(int,r['s'].split('x'));q=max(w,h)/min(w,h)
            _dd['art'].append({'k':n.lower().replace(',',''),'n':n,'f':{},'o':True,'os':True,'t':r['new']['t'],'sh':'sq' if q<1.15 else 'rect' if q<1.75 else 'pano','h':None,'img':(r['id'] if os.path.exists(os.path.join(outdir,'art',r['id']+'.webp')) else None),'land':w>h})
            _ids[r['id']]=_dd['art'][-1]
        a=_ids.get(r['id'])
        if a is None:raise SystemExit('tour work not found: '+r['id'])
        a['id']=r['id']
        if r['rename']:a['aka']=a['n'];a['n']=r['rename'];a['k']=a['k']+' '+r['rename'].lower()
    _dd['TOUR0']=[{'id':r['id'],'s':r['s'],'p':r['p'],'d':r['d']} for r in _t['list']];_dd['TOURC']=_t['care']
    _dd['TOURV']=_h2.sha1(json.dumps(_t,sort_keys=True).encode()).hexdigest()[:8]
_vc={}
for _f in os.listdir(os.path.join(outdir,'views')) if os.path.isdir(os.path.join(outdir,'views')) else []:
    _id,_,_n=_f.rpartition('-');_vc[_id]=max(_vc.get(_id,0),int(_n.split('.')[0])+1)
_dd['VIEWS']=_vc
d=json.dumps(_dd,ensure_ascii=False,separators=(',',':')).replace('</','<'+chr(92)+'/')
body=t.replace('__DATA__',d)
open(preview,'w').write(body.replace('__QR_SRC__','https://cdnjs.cloudflare.com/ajax/libs/qrcode-generator/1.4.4/qrcode.min.js'))
body=body.replace('__QR_SRC__','vendor/qrcode.js')
head='''<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#f6f5f1">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Albert Levi">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icon-180.png">
<link rel="icon" href="icon-192.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>
</head><body>'''
open(outdir+'/index.html','w').write(head+body+'</body></html>')
json.dump({"name":"Albert Levi · Price Guide","short_name":"Albert Levi","start_url":"./","scope":"./","display":"standalone","background_color":"#ffffff","theme_color":"#f6f5f1","dir":"rtl","lang":"he",
 "icons":[{"src":"icon-192.png","sizes":"192x192","type":"image/png"},{"src":"icon-512.png","sizes":"512x512","type":"image/png","purpose":"any maskable"}]},open(outdir+'/manifest.webmanifest','w'),ensure_ascii=False,indent=1)
import hashlib
ver=hashlib.sha1((head+body).encode()).hexdigest()[:10]
open(outdir+'/sw.js','w').write('''// Offline cache for the price guide. Bump happens automatically: the version is a hash of index.html.
const V='alp-%s';
const CORE=['./','index.html','manifest.webmanifest','icon-180.png','icon-192.png','icon-512.png','vendor/qrcode.js','originals.html'].concat(%s);
self.addEventListener('install',e=>{e.waitUntil(caches.open(V).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==V&&k.startsWith('alp-')).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{const u=new URL(e.request.url);if(e.request.method!=='GET')return;
  if(u.origin===location.origin){
    // network first for the page (to pick up price updates), cache as fallback offline
    if(e.request.mode==='navigate'){e.respondWith(fetch(e.request.url,{cache:'no-cache'}).then(r=>{const cp=r.clone();caches.open(V).then(c=>c.put(e.request,cp));return r}).catch(()=>caches.match(e.request).then(r=>r||caches.match('index.html'))));return}
    // paintings and room photos are cached the first time they are seen
    e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request).then(n=>{if(n.ok&&/\\/(art|views)\\//.test(u.pathname)){const cp=n.clone();caches.open(V).then(c=>c.put(e.request,cp))}return n})));return}
  if(/fonts\\.(googleapis|gstatic)\\.com$/.test(u.hostname)){
    e.respondWith(caches.open(V+'-fonts').then(c=>c.match(e.request).then(r=>r||fetch(e.request).then(n=>{c.put(e.request,n.clone());return n}))))}
});
'''%(ver,json.dumps(['art-sm/'+f for f in sorted(__import__('os').listdir(outdir+'/art-sm'))])))
print('ok',ver)

# originals form page
import os
arts=json.loads(open(data).read())['art']
orig=[{'id':__import__('re').sub(r'[^a-z0-9]+','-',a['k']),'n':a['n'],'os':a.get('os'),'sh':a.get('sh')} for a in arts if a['o']]
orig.sort(key=lambda a:(a['os'] is False,a['n'].lower()))
ot=open(os.path.join(os.path.dirname(tpl),'tplO.html')).read().replace('__DATA__',json.dumps(orig,ensure_ascii=False).replace('</','<\\/'))
open(outdir+'/originals.html','w').write(head.replace('<link rel="manifest" href="manifest.webmanifest">','')+ot+'</body></html>')
open(os.path.join(os.path.dirname(preview),'originals-preview.html'),'w').write(ot)
print('originals',len(orig))

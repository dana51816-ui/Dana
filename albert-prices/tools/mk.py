import sys,json
tpl,data,outdir,preview=sys.argv[1:5]
t=open(tpl).read(); d=open(data).read().replace('</','<\\/')
body=t.replace('__DATA__',d)
open(preview,'w').write(body.replace('__QR_SRC__','https://cdnjs.cloudflare.com/ajax/libs/qrcode-generator/1.4.4/qrcode.min.js'))
body=body.replace('__QR_SRC__','vendor/qrcode.js')
head='''<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#1d3a8f">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="מחירון אלברט">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icon-180.png">
<link rel="icon" href="icon-192.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>
</head><body>'''
open(outdir+'/index.html','w').write(head+body+'</body></html>')
json.dump({"name":"מחירון אלברט לוי","short_name":"מחירון אלברט","start_url":"./","scope":"./","display":"standalone","background_color":"#f3f5fb","theme_color":"#1d3a8f","dir":"rtl","lang":"he",
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
    if(e.request.mode==='navigate'){e.respondWith(fetch(e.request).then(r=>{const cp=r.clone();caches.open(V).then(c=>c.put(e.request,cp));return r}).catch(()=>caches.match(e.request).then(r=>r||caches.match('index.html'))));return}
    e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request)));return}
  if(/fonts\\.(googleapis|gstatic)\\.com$/.test(u.hostname)){
    e.respondWith(caches.open(V+'-fonts').then(c=>c.match(e.request).then(r=>r||fetch(e.request).then(n=>{c.put(e.request,n.clone());return n}))))}
});
'''%(ver,json.dumps(['thumbs/'+f for f in sorted(__import__('os').listdir(outdir+'/thumbs'))])))
print('ok',ver)

# originals form page
import os
arts=json.loads(open(data).read())['art']
orig=[{'id':__import__('re').sub(r'[^a-z0-9]+','-',a['k']),'n':a['n'],'os':a.get('os')} for a in arts if a['o']]
orig.sort(key=lambda a:(a['os'] is False,a['n'].lower()))
ot=open(os.path.join(os.path.dirname(tpl),'tplO.html')).read().replace('__DATA__',json.dumps(orig,ensure_ascii=False).replace('</','<\\/'))
open(outdir+'/originals.html','w').write(head.replace('<link rel="manifest" href="manifest.webmanifest">','')+ot+'</body></html>')
open(os.path.join(os.path.dirname(preview),'originals-preview.html'),'w').write(ot)
print('originals',len(orig))

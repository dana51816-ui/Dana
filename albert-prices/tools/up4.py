import re
t=open('tpl3.html').read()
def R(a,b,n=1):
    global t
    c=t.count(a); assert c>=1,('MISSING',a[:80]); t=t.replace(a,b,n)
def RX(pat,b):
    global t
    m=re.search(pat,t,re.S); assert m,('NOREGEX',pat[:60]); t=t[:m.start()]+b+t[m.end():]

# ---------- CSS ----------
R("@media (prefers-reduced-motion:no-preference){.sheet{", r"""/* quick actions */
.qa{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:2px}
.qa button{border:1px solid var(--line);background:var(--card);border-radius:16px;padding:10px 8px;display:grid;gap:2px;justify-items:center;text-align:center;box-shadow:var(--shadow)}
.qa b{font-size:.86rem;font-weight:600}
.qa small{font-size:.72rem;color:var(--muted);font-family:var(--display);font-variant-numeric:tabular-nums}
.qa .ic{width:30px;height:30px;border-radius:10px;display:grid;place-items:center;font-size:1rem;margin-bottom:2px}
/* quick sheet */
.qtabs{display:flex;gap:8px}
.qtabs button{flex:1;border:1.5px solid var(--line);background:var(--card);border-radius:12px;padding:10px;font-weight:600}
.qtabs button[aria-pressed="true"]{background:var(--navy);border-color:var(--navy);color:#fff}
td .cp{display:block;font-size:.68rem;color:var(--ok);font-weight:600;margin-top:2px}
/* sales */
.kpis{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.kpi{background:linear-gradient(160deg,var(--navy),var(--navy-deep));color:#fff;border-radius:16px;padding:12px;display:grid;gap:2px}
.kpi small{color:#b9c3ea;font-size:.72rem}
.kpi b{font-family:var(--display);font-stretch:118%;font-weight:900;font-size:1.35rem;font-variant-numeric:tabular-nums;direction:ltr;text-align:right}
.deal{display:grid;grid-template-columns:auto 1fr auto;gap:2px 10px;align-items:center;padding:10px 0;border-bottom:1px solid var(--line)}
.deal:last-child{border-bottom:0}
.deal time{grid-row:1/3;font-family:var(--display);font-weight:700;color:var(--muted);font-size:.85rem}
.deal .nm{font-weight:600;font-size:.92rem;direction:ltr;text-align:right;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.deal small{color:var(--muted);font-size:.76rem}
.deal .amt{grid-row:1/3;font-family:var(--display);font-weight:800;font-variant-numeric:tabular-nums}
.deal .del{border:0;background:none;color:var(--sold);font-size:.75rem;padding:0;justify-self:start}
.bars{display:grid;gap:8px}
.bar{display:grid;grid-template-columns:70px 1fr auto;gap:8px;align-items:center;font-size:.85rem}
.bar i{display:block;height:12px;border-radius:999px;background:var(--gold)}
.bar span:last-child{font-family:var(--display);font-weight:700;font-variant-numeric:tabular-nums}
/* close deal */
.cthumbs{display:flex;gap:8px;overflow-x:auto}
.cthumbs img{width:64px;height:64px;object-fit:contain;background:var(--soft);border-radius:12px;flex:none}
.bigtotal{font-family:var(--display);font-stretch:118%;font-weight:900;font-size:2.6rem;direction:ltr;text-align:right;line-height:1}
.green{border:0;background:var(--ok);color:#fff;border-radius:14px;padding:14px 16px;font-weight:700;font-size:1.02rem}
/* showroom */
.cust{place-items:start center}
.room{width:100%;border-radius:18px;overflow:hidden;box-shadow:0 30px 60px -25px rgba(0,0,0,.6);background:#e8e2d8}
.room svg{display:block;width:100%;height:auto}
.room image{transition:all .45s cubic-bezier(.2,.8,.2,1)}
.srow{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;padding-bottom:2px}
.srow::-webkit-scrollbar{display:none}
.srow button{flex:none;border:1px solid rgba(255,255,255,.3);background:rgba(255,255,255,.06);color:#fff;border-radius:12px;padding:8px 12px;font-family:var(--display);font-weight:700;font-size:.85rem;font-variant-numeric:tabular-nums}
.srow button small{display:block;font-weight:500;font-size:.66rem;color:#aab6e6}
.srow button[aria-pressed="true"]{background:#fff;color:#14215e;border-color:#fff}
.srow button[aria-pressed="true"] small{color:#5f6789}
.srow.fr button{font-family:var(--body);font-weight:500}
.slabel{font-size:.7rem;letter-spacing:.14em;color:#aab6e6;font-family:var(--display);font-stretch:125%;font-weight:800}
.pricebox{display:flex;justify-content:space-between;align-items:flex-end;gap:14px}
.qr{background:#fff;border-radius:14px;padding:8px;display:grid;gap:2px;justify-items:center;flex:none}
.qr svg{width:84px;height:84px;display:block}
.qr small{color:#14215e;font-size:.6rem;font-weight:700;letter-spacing:.06em;font-family:var(--display)}
.cbtns{display:flex;gap:8px;flex-wrap:wrap;direction:rtl}
.cbtns .line{padding:10px 14px}
.lines .th{width:46px;height:46px;object-fit:contain;background:rgba(255,255,255,.08);border-radius:10px;flex:none}
.lines .li{display:flex;gap:10px;align-items:center;min-width:0}
/* splash */
#splash{position:fixed;inset:0;z-index:100;background:linear-gradient(180deg,#1d3a8f,#0a0f2c);display:grid;place-items:center;color:#fff;transition:opacity .45s ease}
#splash .lg{display:flex;align-items:center;direction:ltr}
#splash .A{font-family:var(--script);font-size:7rem;line-height:.6;clip-path:inset(0 100% 0 0);animation:draw 1s .1s ease-out forwards}
#splash b{font-family:var(--thin);font-weight:300;letter-spacing:.4em;font-size:1.5rem;opacity:0;animation:fadein .6s .7s ease forwards}
#splash small{display:block;text-align:center;color:var(--gold);font-family:var(--display);font-stretch:125%;font-weight:800;letter-spacing:.2em;font-size:.7rem;margin-top:22px;opacity:0;animation:fadein .6s 1s ease forwards}
@keyframes draw{to{clip-path:inset(0 0 0 0)}}@keyframes fadein{to{opacity:1}}
#fx{position:fixed;inset:0;z-index:90;pointer-events:none}
@media (prefers-reduced-motion:no-preference){.tile{animation:rise .5s cubic-bezier(.2,.8,.2,1) both}.tile:nth-child(2){animation-delay:.04s}.tile:nth-child(3){animation-delay:.08s}.tile:nth-child(4){animation-delay:.12s}.tile:nth-child(n+5){animation-delay:.16s}@keyframes rise{from{transform:translateY(10px)}to{transform:none}}}
@media (prefers-reduced-motion:no-preference){.sheet{""")

# ---------- markup ----------
R('''  <div class="themes" id="themes" style="margin-top:14px"></div>''','''  <div class="qa" id="qa"></div>
  <div class="themes" id="themes" style="margin-top:14px"></div>''')
R('''<section class="cust" id="cust" hidden aria-label="תצוגה ללקוח"></section>''','''<section class="cust" id="cust" hidden aria-label="תצוגה ללקוח"></section>
<section class="sheet" id="quick" hidden aria-label="מחירון מהיר"></section>
<section class="sheet" id="sales" hidden aria-label="מכירות"></section>
<section class="sheet" id="close" hidden aria-label="סגירת עסקה"></section>
<canvas id="fx" hidden></canvas>''')
R('''<script type="application/json" id="data">''','''<script src="__QR_SRC__"></script>
<script type="application/json" id="data">''')

# ---------- state ----------
R("function persist(){try{localStorage.setItem(LSK,JSON.stringify({S,ORIG,T,tour,pkg}))}catch(e){}}","function persist(){try{localStorage.setItem(LSK,JSON.stringify({S,ORIG,T,tour,pkg,SALES}))}catch(e){}}")
R("let ORIG=L.ORIG||{}, T=L.T||{}, tour=L.tour||[], pkg=L.pkg||[];","let ORIG=L.ORIG||{}, T=L.T||{}, tour=L.tour||[], pkg=L.pkg||[], SALES=L.SALES||[];")
R("let S=Object.assign({rate:3.7,round:'5',unit:'in',verified:false,coll:true,second:25},L.S||{});","let S=Object.assign({rate:3.7,round:'5',unit:'in',verified:false,coll:true,second:25,me:''},L.S||{});")

# ---------- room scene replaces wallSVG ----------
RX(r"function wallSVG\(\)\{.*?</p></div>`\}\n", r"""function roomSVG(a,w,h,fr,opt){opt=opt||{};const W=Math.max(380,w+150),floor=16,sofaH=82,gap=24,H=Math.max(270,floor+sofaH+gap+h+46);
  const fy=H-floor,ax=(W-w)/2,ay=fy-sofaH-gap-h,sx=(W-210)/2,id='r'+a.id+(opt.k||'');
  const fs={black:'#121318',white:'#f7f7f4',espresso:'#4a2f22',natural:'#c79a62'}[fr]||null;const fw=Math.max(2.5,Math.min(w,h)*.035);
  return `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Room preview ${sz(w+'x'+h,'cm')}">
  <defs><linearGradient id="${id}w" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#efe9df"/><stop offset="1" stop-color="#ddd5c8"/></linearGradient>
  <radialGradient id="${id}l" cx=".5" cy=".3" r=".7"><stop offset="0" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
  <filter id="${id}s" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="${Math.max(2,h*.03)}" stdDeviation="${Math.max(2,h*.03)}" flood-color="#000" flood-opacity=".35"/></filter>
  <clipPath id="${id}c"><rect x="${ax}" y="${ay}" width="${w}" height="${h}"/></clipPath></defs>
  <rect width="${W}" height="${fy}" fill="url(#${id}w)"/><ellipse cx="${W/2}" cy="${ay+h*.4}" rx="${W*.55}" ry="${H*.45}" fill="url(#${id}l)"/>
  <rect y="${fy}" width="${W}" height="${floor}" fill="#a77b52"/><rect y="${fy}" width="${W}" height="2.5" fill="#f4efe7"/>
  ${Array.from({length:Math.ceil(W/38)},(_,i)=>`<rect x="${i*38}" y="${fy+2.5}" width=".8" height="${floor}" fill="#8e6641"/>`).join('')}
  <g transform="translate(${W-62},${fy})"><rect x="14" y="-150" width="2" height="150" fill="#2b2b2b"/><path d="M0 -150 L30 -150 L24 -178 L6 -178Z" fill="#f2e3c6"/><ellipse cx="15" cy="-1" rx="12" ry="2" fill="#2b2b2b"/></g>
  <g transform="translate(26,${fy})"><path d="M-10 0 L10 0 L13 -34 L-13 -34Z" fill="#c2643a"/><g fill="#3f7d4e"><ellipse cx="-12" cy="-60" rx="9" ry="26" transform="rotate(-25 -12 -60)"/><ellipse cx="10" cy="-66" rx="9" ry="30" transform="rotate(20 10 -66)"/><ellipse cx="0" cy="-74" rx="8" ry="34"/></g></g>
  <g><rect x="${sx}" y="${fy-sofaH}" width="210" height="48" rx="12" fill="#3e4f78"/><rect x="${sx-10}" y="${fy-sofaH+24}" width="230" height="44" rx="14" fill="#34436a"/>
  <rect x="${sx+8}" y="${fy-sofaH+14}" width="94" height="30" rx="10" fill="#4a5c88"/><rect x="${sx+108}" y="${fy-sofaH+14}" width="94" height="30" rx="10" fill="#4a5c88"/>
  <rect x="${sx+24}" y="${fy-sofaH+2}" width="34" height="28" rx="8" fill="${a.c[1]}" opacity=".9"/><rect x="${sx+152}" y="${fy-sofaH+2}" width="34" height="28" rx="8" fill="${a.c[2]}" opacity=".9"/>
  <rect x="${sx+6}" y="${fy-14}" width="6" height="14" fill="#222"/><rect x="${sx+198}" y="${fy-14}" width="6" height="14" fill="#222"/></g>
  <g filter="url(#${id}s)"><rect x="${ax}" y="${ay}" width="${w}" height="${h}" fill="${a.c[0]}"/><image href="${img(a)}" x="${ax-w*.08}" y="${ay-h*.08}" width="${w*1.16}" height="${h*1.16}" preserveAspectRatio="xMidYMid slice" clip-path="url(#${id}c)"/>
  ${fs?`<rect x="${ax-fw/2}" y="${ay-fw/2}" width="${w+fw}" height="${h+fw}" fill="none" stroke="${fs}" stroke-width="${fw}"/>`:''}${fr==='rolled'?`<rect x="${ax}" y="${ay}" width="${w}" height="${h}" fill="none" stroke="#fff" stroke-dasharray="5 4" stroke-width="1.4"/>`:''}</g>
  ${opt.label!==false?`<g transform="translate(${W/2},${ay-14})"><rect x="-58" y="-11" width="116" height="20" rx="10" fill="#14215e" opacity=".9"/><text y="3.5" text-anchor="middle" font-size="10" fill="#fff" font-family="Archivo, sans-serif" font-weight="700" style="direction:ltr;unicode-bidi:plaintext">${sz(w+'x'+h,'in')} · ${w}×${h} cm</text></g>`:''}
  </svg>`}
function wallSVG(){if(!sel)return '';const [w,h]=sel.custom?[sel.w,sel.h]:dims(sel.s);
  return `<div class="wallbox" style="padding:0;overflow:hidden">${roomSVG(cur,w,h,sel.fr)}<p style="padding:6px 10px 8px">הדמיה בקנה מידה: ספה ברוחב 2.1 מטר</p></div>`}
""")

# ---------- pbar: count-up ----------
R("""<div class="pval">${$f(p.fin)}${p.pct?`<s>${$f(it.list)}</s>`:''}</div></div>""","""<div class="pval"><span data-roll="${p.fin}">${$f(renderBar.last??p.fin)}</span>${p.pct?`<s>${$f(it.list)}</s>`:''}</div></div>""")
R("""  $('pbar').hidden=false;renderFab()}""","""  $('pbar').hidden=false;roll($('pbar'));renderBar.last=p.fin;renderFab()}
function roll(root){root.querySelectorAll('[data-roll]').forEach(el=>{const to=+el.dataset.roll,from=parseFloat(el.textContent.replace(/[^\\d.]/g,''))||to;
  if(from===to||matchMedia('(prefers-reduced-motion: reduce)').matches){el.textContent=$f(to);return}
  const t0=performance.now(),d=420;(function step(t){const k=Math.min(1,(t-t0)/d),e=1-Math.pow(1-k,3);el.textContent=$f(from+(to-from)*e);if(k<1)requestAnimationFrame(step)})(t0)})}""")

# ---------- package: close deal button ----------
R("""<button class="ghost" type="button" data-act="pclear">ניקוי החבילה</button></div></div>`}""","""<button class="ghost" type="button" data-act="pclear">ניקוי החבילה</button></div>
  ${c.items.length?`<button class="green" type="button" data-act="pdeal">✓ סגירת עסקה · ${$f(c.fin)}</button>`:''}</div>`}""")
R("""  else if(d.act==='pclear')pkg=[];""","""  else if(d.act==='pclear')pkg=[];
  else if(d.act==='pdeal'){const c=pkgCalc();return openClose(c.items,true)}""")

# ---------- showroom replaces showCust ----------
RX(r"/\* ---------- customer view ---------- \*/.*?\$\('cust'\)\.addEventListener\('click',\(\)=>back\(\)\);\n", r"""/* ---------- showroom (customer view) ---------- */
let CV=null;
function qrSVG(url){try{if(!window.qrcode)return '';const q=qrcode(0,'M');q.addData(url);q.make();return q.createSvgTag({cellSize:3,margin:0,scalable:true})}catch(e){return ''}}
function showCust(o){CV=o;renderCust();$('cust').hidden=false;$('cust').scrollTop=0;renderFab();history.pushState({d:1,c:1},'')}
function renderCust(){const o=CV;let h=`<div class="cc"><div class="who"><span class="A">A</span><b>Albert Levi</b></div>`;
  if(o.single){const it=current(),p=single(it);const a=cur;
    if(kind==='orig'){h+=`<div class="room">${roomSVG(a,100,120,'stretch',{label:false,k:'c'})}</div><h2>${esc(a.n)}</h2><div class="slabel">ORIGINAL PAINTING · ONE OF A KIND</div>`}
    else{const [w,hh]=sel.custom?[sel.w,sel.h]:dims(sel.s);const F=a.f[sel.f];
      h+=`<div class="room" id="room">${roomSVG(a,w,hh,sel.fr,{k:'c'})}</div><h2>${esc(a.n)}</h2><div class="slabel">${FMT[sel.f].en.toUpperCase()}</div>`;
      if(!sel.custom){const ss=Object.keys(F).sort((x,y)=>area(x)-area(y));const frs=FRO.filter(x=>F[sel.s][x]!==undefined);
        h+=`<div class="srow" role="group" aria-label="Size">${ss.map(s=>`<button type="button" data-cs="${s}" aria-pressed="${s===sel.s}">${sz(s,'in')}<small>${sz(s,'cm')}</small></button>`).join('')}</div>
        <div class="srow fr" role="group" aria-label="Finish">${frs.map(x=>`<button type="button" data-cf="${x}" aria-pressed="${x===sel.fr}">${FR[x].en}</button>`).join('')}</div>`}}
    const url=a.h?`https://www.albertlevi.com/products/${a.h}`:'';const qr=url?qrSVG(url):'';
    h+=`${p.coll?`<span class="cpill">THE COLLECTOR'S RATE · ${p.pct}% OFF</span>`:''}<div class="pricebox"><div class="big">${p.pct?`<s>${$f(it.list)}</s>`:''}<span data-roll="${p.fin}">${$f(renderCust.last??p.fin)}</span></div>${qr?`<div class="qr">${qr}<small>SHOP ONLINE</small></div>`:''}</div>`;
    renderCust.last=p.fin;
    h+=`<div class="cbtns"><button class="gold" type="button" data-cx="deal">✓ סגירת עסקה</button><button class="line" type="button" data-cx="add">+ לחבילה</button><button class="line" type="button" data-cx="x">סגירה</button></div>`}
  else{const c=pkgCalc();h+=`<h2>Your collection</h2><div class="lines">${c.items.map(x=>{const a=ART.find(y=>y.id===x.id);return `<div><span class="li">${a?`<img class="th" src="${img(a)}" alt="">`:''}<span>${esc(x.n)}<br><small style="color:#aab6e6">${esc(x.spec)}</small></span></span><span>${x.fin!==x.list?`<s style="color:#aab6e6;font-weight:500">${$f(x.list)}</s> `:''}${$f(x.fin)}</span></div>`}).join('')}</div>
    <div class="big">${c.fin<c.list?`<s>${$f(c.list)}</s>`:''}${$f(c.fin)}</div><div class="cbtns"><button class="gold" type="button" data-cx="pdeal">✓ סגירת עסקה</button><button class="line" type="button" data-cx="x">סגירה</button></div>`}
  $('cust').innerHTML=h+`</div>`;roll($('cust'))}
$('cust').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;const d=b.dataset;
  if(d.cs){sel={f:sel.f,s:d.cs,fr:cur.f[sel.f][d.cs][sel.fr]!==undefined?sel.fr:FRO.find(x=>cur.f[sel.f][d.cs][x]!==undefined)};renderCust();renderDetail();return}
  if(d.cf){sel=Object.assign({},sel,{fr:d.cf});renderCust();renderDetail();return}
  if(d.cx==='add'){const it=current();if(it){pkg.push(it);persist();toast('נוסף לחבילה · '+pkg.length)}return}
  if(d.cx==='deal'){const it=current();const p=single(it);return openClose([Object.assign({},it,{fin:p.fin})],false)}
  if(d.cx==='pdeal'){return openClose(pkgCalc().items,true)}
  if(d.cx==='x')back()});

/* ---------- close deal + sales log ---------- */
const PAY=['אשראי','מזומן','Zelle','Venmo','אחר'];let CL=null;
function openClose(items,fromPkg){CL={items,fromPkg,pay:'אשראי',cust:'',note:''};$('close').hidden=false;renderClose();history.pushState({d:1},'')}
function renderClose(){const tot=CL.items.reduce((s,x)=>s+x.fin,0);
  $('close').innerHTML=`<div class="wrap sbody"><div class="shead"><h2>סגירת עסקה</h2><button class="back" type="button" data-act="back">ביטול</button></div>
  <div class="panel"><div class="cthumbs">${CL.items.map(x=>{const a=ART.find(y=>y.id===x.id);return a?`<img src="${img(a)}" alt="${esc(a.n)}">`:''}).join('')}</div>
    <div class="items">${CL.items.map(x=>`<div class="item" style="grid-template-columns:1fr auto"><span class="nm">${esc(x.n)}</span><small>${esc(x.spec)}</small><span class="pr">${$f(x.fin)}</span></div>`).join('')}</div>
    <div class="bigtotal">${$f(tot)}</div></div>
  <div class="panel"><h3>אמצעי תשלום</h3><div class="seg">${PAY.map(p=>`<button type="button" data-pay="${p}" aria-pressed="${CL.pay===p}">${p}</button>`).join('')}</div>
    <div class="field"><label for="clCust">שם הלקוח (לא חובה)</label><input id="clCust" value="${esc(CL.cust)}" placeholder="Sarah, Miami"></div>
    <div class="field"><label for="clNote">הערה (משלוח, הקדשה…)</label><input id="clNote" value="${esc(CL.note)}"></div>
    <p class="note">נמכר על ידי: <b>${S.me||'לא הוגדר'}</b>${S.me?'':' · מגדירים בהגדרות מי משתמש במכשיר'}</p></div>
  <button class="green" type="button" data-act="save">✓ אישור, נמכר</button></div>`}
$('close').addEventListener('input',e=>{if(e.target.id==='clCust')CL.cust=e.target.value;if(e.target.id==='clNote')CL.note=e.target.value});
$('close').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;
  if(b.dataset.act==='back')return back();
  if(b.dataset.pay){CL.pay=b.dataset.pay;return renderClose()}
  if(b.dataset.act==='save'){const deal={id:Date.now().toString(36)+Math.random().toString(36).slice(2,6),ts:Date.now(),items:CL.items.map(x=>({id:x.id,n:x.n,spec:x.spec,list:x.list,fin:x.fin,orig:!!x.orig})),total:CL.items.reduce((s,x)=>s+x.fin,0),pay:CL.pay,cust:CL.cust,note:CL.note,by:S.me||''};
    SALES.push(deal);deal.items.filter(x=>x.orig).forEach(x=>{ORIG[x.id]=Object.assign({},ORIG[x.id]||{},{status:'sold'})});
    if(CL.fromPkg)pkg=[];persist();celebrate();toast('נמכר! '+$f(deal.total)+' נרשם ביומן');
    for(const id of ['close','cust','pkg'])$(id).hidden=true;history.go(-1);setTimeout(()=>{if(!$('detail').hidden)renderDetail();renderHome()},60)}});
function dayKey(ts){const d=new Date(ts);return d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate()}
let salesRange='today';
function openSales(){$('sales').hidden=false;renderSales();history.pushState({d:1},'')}
function renderSales(){const today=dayKey(Date.now());const list=SALES.filter(s=>salesRange==='all'||dayKey(s.ts)===today).sort((a,b)=>b.ts-a.ts);
  const tot=list.reduce((s,x)=>s+x.total,0),pcs=list.reduce((s,x)=>s+x.items.length,0);
  const by={};list.forEach(s=>{const k=s.by||'לא ידוע';by[k]=(by[k]||0)+s.total});const pay={};list.forEach(s=>{pay[s.pay]=(pay[s.pay]||0)+s.total});
  const mx=Math.max(1,...Object.values(by),...Object.values(pay));
  const bars=o=>Object.entries(o).sort((a,b)=>b[1]-a[1]).map(([k,v])=>`<div class="bar"><span>${esc(k)}</span><i style="width:${Math.max(4,v/mx*100)}%"></i><span>${$f(v)}</span></div>`).join('');
  $('sales').innerHTML=`<div class="wrap sbody"><div class="shead"><h2>מכירות</h2><button class="back" type="button" data-act="back">סגירה</button></div>
  <div class="qtabs"><button type="button" data-r="today" aria-pressed="${salesRange==='today'}">היום</button><button type="button" data-r="all" aria-pressed="${salesRange==='all'}">כל הטור</button></div>
  <div class="kpis"><div class="kpi"><small>הכנסות</small><b>${$f(tot)}</b></div><div class="kpi"><small>עסקאות</small><b>${list.length}</b></div><div class="kpi"><small>יצירות</small><b>${pcs}</b></div></div>
  ${list.length?`<div class="panel"><h3>לפי מוכר</h3><div class="bars">${bars(by)}</div><h3>לפי תשלום</h3><div class="bars">${bars(pay)}</div></div>`:''}
  <div class="panel"><h3>עסקאות</h3>${list.length?list.map(s=>`<div class="deal"><time>${new Date(s.ts).toLocaleTimeString('he-IL',{hour:'2-digit',minute:'2-digit'})}</time><span class="nm">${esc(s.items.map(x=>x.n).join(' + '))}</span><span class="amt">${$f(s.total)}</span><small>${esc([s.pay,s.by,s.cust].filter(Boolean).join(' · '))}${salesRange==='all'?' · '+new Date(s.ts).toLocaleDateString('he-IL'):''}</small>${CL&&CL.confirm===s.id?`<button class="del" type="button" data-delok="${s.id}">למחוק? לחצו שוב</button>`:`<button class="del" type="button" data-del="${s.id}">מחיקה</button>`}</div>`).join(''):'<p class="note">עוד אין מכירות. סוגרים עסקה מחדר התצוגה או מהחבילה, והיא נרשמת כאן.</p>'}</div>
  ${list.length?`<button class="primary" type="button" data-act="rep">העתקת דוח לוואטסאפ</button>`:''}</div>`}
$('sales').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;const d=b.dataset;
  if(d.act==='back')return back();if(d.r){salesRange=d.r}
  else if(d.del){CL=Object.assign(CL||{},{confirm:d.del})}
  else if(d.delok){SALES=SALES.filter(s=>s.id!==d.delok);CL=null;persist()}
  else if(d.act==='rep'){const today=dayKey(Date.now());const list=SALES.filter(s=>salesRange==='all'||dayKey(s.ts)===today);
    const tot=list.reduce((s,x)=>s+x.total,0);return copy(`Albert Levi · ${salesRange==='all'?'כל הטור':'סיכום יום '+new Date().toLocaleDateString('he-IL')}\nהכנסות: ${$f(tot)} · ${list.length} עסקאות\n\n`+list.map(s=>`${new Date(s.ts).toLocaleTimeString('he-IL',{hour:'2-digit',minute:'2-digit'})} ${s.items.map(x=>x.n).join(' + ')} — ${$f(s.total)} (${s.pay}${s.by?', '+s.by:''})`).join('\n'),'הדוח הועתק')}
  else return;renderSales()});

/* ---------- quick price sheet ---------- */
let qf='canvas';
function openQuick(){$('quick').hidden=false;renderQuick();history.pushState({d:1},'')}
function renderQuick(){const T2=STD[qf],ks=Object.keys(T2).sort((x,y)=>area(x)-area(y)),cols=FRO.filter(fr=>ks.some(k=>T2[k][fr]));
  $('quick').innerHTML=`<div class="wrap sbody"><div class="shead"><h2>מחירון מהיר</h2><button class="back" type="button" data-act="back">סגירה</button></div>
  <p class="note">המחיר זהה לכל היצירות לפי גודל וגימור. בירוק: המחיר אחרי Collector's Rate.</p>
  <div class="qtabs">${['canvas','emb'].map(f=>`<button type="button" data-q="${f}" aria-pressed="${qf===f}">${FMT[f].he}</button>`).join('')}</div>
  <section class="pcard"><div class="tscroll"><table><thead><tr><th style="text-align:right;padding-inline-start:16px">גודל</th>${cols.map(c=>`<th>${FR[c].he}</th>`).join('')}</tr></thead><tbody>
  ${ks.map(k=>`<tr><td class="sz"><b>${sz(k,S.unit)}</b><small>${sz(k,S.unit==='cm'?'in':'cm')}</small></td>${cols.map(c=>{const o=T2[k][c];if(!o)return '<td class="na">–</td>';const l=usd(o.p),pc=collPct(l);return `<td><button type="button" class="${o.w?'w':''}" tabindex="-1">${$f(l)}</button>${pc?`<span class="cp">${$f(usd(o.p*(1-pc/100)))}</span>`:''}</td>`}).join('')}</tr>`).join('')}
  </tbody></table></div></section></div>`}
$('quick').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;if(b.dataset.act==='back')return back();if(b.dataset.q){qf=b.dataset.q;renderQuick()}});

/* ---------- celebration ---------- */
function celebrate(){if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;const c=$('fx');c.hidden=false;const x=c.getContext('2d');const W=c.width=innerWidth,H=c.height=innerHeight;
  const cols=['#f2b33d','#2f4be0','#e0337a','#11a198','#ffffff','#f26b2a'];const ps=Array.from({length:120},()=>({x:W/2,y:H*.45,vx:(Math.random()-.5)*14,vy:-Math.random()*14-4,r:Math.random()*5+3,c:cols[Math.random()*cols.length|0],a:Math.random()*6}));
  const t0=performance.now();(function f(t){x.clearRect(0,0,W,H);ps.forEach(p=>{p.vy+=.45;p.x+=p.vx;p.y+=p.vy;p.a+=.2;x.save();x.translate(p.x,p.y);x.rotate(p.a);x.fillStyle=p.c;x.fillRect(-p.r,-p.r/2,p.r*2,p.r);x.restore()});if(t-t0<1700)requestAnimationFrame(f);else{x.clearRect(0,0,W,H);c.hidden=true}})(t0)}
""")

# ---------- popstate: handle new sheets ----------
R("""window.addEventListener('popstate',()=>{if(!$('cust').hidden){$('cust').hidden=true;return}""","""window.addEventListener('popstate',()=>{if(!$('close').hidden){$('close').hidden=true;return}if(!$('cust').hidden){$('cust').hidden=true;renderFab();return}if(!$('quick').hidden||!$('sales').hidden){$('quick').hidden=true;$('sales').hidden=true;renderHome();return}""")

# ---------- home quick actions ----------
R("""  renderFab();
}
document.addEventListener('click',e=>{const b=e.target.closest('#grid [data-id],#tour [data-id]');""","""  const td=dayKey(Date.now()),tt=SALES.filter(s=>dayKey(s.ts)===td).reduce((s,x)=>s+x.total,0);
  $('qa').innerHTML=`<button type="button" data-qa="quick"><span class="ic" style="background:color-mix(in srgb,var(--gold) 30%,transparent)">$</span><b>מחירון מהיר</b><small>כל הגדלים</small></button>
  <button type="button" data-qa="sales"><span class="ic" style="background:color-mix(in srgb,var(--ok) 25%,transparent)">✓</span><b>מכירות היום</b><small>${$f(tt)}</small></button>
  <button type="button" data-qa="pkg"><span class="ic" style="background:color-mix(in srgb,var(--cobalt) 22%,transparent)">◫</span><b>חבילה</b><small>${pkg.length?pkg.length+' · '+$f(pkgCalc().fin):'ריקה'}</small></button>`;
  renderFab();
}
$('qa').addEventListener('click',e=>{const b=e.target.closest('[data-qa]');if(!b)return;const k=b.dataset.qa;if(k==='quick')openQuick();else if(k==='sales')openSales();else{$('pkg').hidden=false;renderPkg();renderFab();history.pushState({d:1},'')}});
document.addEventListener('click',e=>{const b=e.target.closest('#grid [data-id],#tour [data-id]');""")
R("function renderFab(){const show=pkg.length>0&&$('pkg').hidden&&$('cust').hidden;","function renderFab(){const show=pkg.length>0&&$('pkg').hidden&&$('cust').hidden&&$('close').hidden&&$('quick').hidden&&$('sales').hidden;")

# ---------- settings: device owner + sales in sync ----------
R("""  <div class="panel"><h3>סנכרון בין אלברט לעירש</h3>""","""  <div class="panel"><h3>מי משתמש במכשיר הזה?</h3><div class="seg">${['אלברט','עירש'].map(n=>`<button type="button" data-me="${n}" aria-pressed="${S.me===n}">${n}</button>`).join('')}</div><p class="note">כך כל מכירה נרשמת על שם מי שסגר אותה.</p></div>
  <div class="panel"><h3>סנכרון בין אלברט לעירש</h3>""")
R("הקוד כולל את השער, ההנחות, מחירי המקורים ורשימת הטור.","הקוד כולל את השער, ההנחות, מחירי המקורים, רשימת הטור ויומן המכירות. מכירות משני המכשירים מתאחדות.")
R("function syncCode(){const json=JSON.stringify({v:1,S,ORIG,T,tour});","function syncCode(){const {me,...shared}=S;const json=JSON.stringify({v:1,S:shared,ORIG,T,tour,SALES});")
R("Object.assign(S,o.S||{});ORIG=o.ORIG||{};T=o.T||{};tour=o.tour||[];","const me=S.me;Object.assign(S,o.S||{});S.me=me;ORIG=o.ORIG||{};T=o.T||{};tour=o.tour||[];const ids=new Set(SALES.map(s=>s.id));(o.SALES||[]).forEach(s=>{if(!ids.has(s.id))SALES.push(s)});")
R("  if(d.round)S.round=d.round;else if(d.unit)S.unit=d.unit;","  if(d.me)S.me=d.me;else if(d.round)S.round=d.round;else if(d.unit)S.unit=d.unit;")

# ---------- splash (installed app only) ----------
R("""renderHome();
if('serviceWorker'""","""renderHome();
(function(){const standalone=matchMedia('(display-mode: standalone)').matches||navigator.standalone;let seen=false;try{seen=sessionStorage.getItem('alp_splash')}catch(e){}
  if(!standalone||seen||matchMedia('(prefers-reduced-motion: reduce)').matches)return;try{sessionStorage.setItem('alp_splash','1')}catch(e){}
  const s=document.createElement('div');s.id='splash';s.innerHTML='<div><div class="lg"><span class="A">A</span><b>Albert Levi</b></div><small>USA TOUR · PRICE GUIDE</small></div>';document.body.appendChild(s);
  setTimeout(()=>{s.style.opacity='0';setTimeout(()=>s.remove(),450)},1700)})();
if('serviceWorker'""")
open('tpl4.html','w').write(t)
print('ok',len(t))

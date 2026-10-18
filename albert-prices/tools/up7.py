import re
t=open('tpl6.html').read()
def R(a,b):
    global t
    assert a in t,('MISSING',a[:90]); t=t.replace(a,b,1)
def RX(p,b):
    global t
    m=re.search(p,t,re.S); assert m,('NOREGEX',p[:60]); t=t[:m.start()]+b+t[m.end():]
R("localStorage.setItem(LSK,JSON.stringify({S,ORIG,T,tour,pkg,SALES}))","localStorage.setItem(LSK,JSON.stringify({S,ORIG,OS,tour,pkg,SALES}))")
R("let ORIG=L.ORIG||{}, T=L.T||{},","let ORIG=L.ORIG||{}, T=L.T||{}, OS=L.OS||[], osel=null,")
R("function origInfo(a){const o=Object.assign({sc:'',cx:'',status:a.os===false?'sold':'avail',ovr:null},ORIG[a.id]||{});o.tier=(o.sc&&o.cx&&T[o.sc]&&T[o.sc][o.cx])||null;o.price=o.ovr||o.tier;return o}",
"""// originals are painted to order: one price per size (OS), with optional per-work prices and sizes left out
function origSizes(a){const o=ORIG[a.id]||{};if(o.nfs)return [];return OS.filter(r=>!(o.off||[]).includes(r.s)).map(r=>({s:r.s,p:(o.ovr&&o.ovr[r.s])||r.p})).filter(r=>r.p).sort((x,y)=>area(x.s)-area(y.s))}
function origInfo(a){const o=ORIG[a.id]||{},ss=origSizes(a);return {nfs:!!o.nfs,sizes:ss,min:ss.length?Math.min(...ss.map(r=>r.p)):null,status:'avail'}}""")
R("""  const badge=o?`<span class="badge${o.status==='sold'?' sold':''}">מקור${o.status==='sold'?' · נמכר':o.status==='hold'?' · שמור':''}</span>`:'';
  const pr=m!=null?`הדפס מ־<b>${$f(m)}</b>`:(o&&o.price?`מקור · <b>${$f(o.price)}</b>`:'מקור · לפי קבוצת מחיר');""",
"""  const badge=o&&!o.nfs?`<span class="badge">מקור${o.min?' מ־'+$f(o.min):''}</span>`:'';
  const pr=m!=null?`הדפס מ־<b>${$f(m)}</b>`:(o&&o.min?`מקור מ־<b>${$f(o.min)}</b>`:'מקור');""")
RX(r"function origHTML\(\)\{.*?\n(?=function renderDetail)", r"""function origHTML(){const o=origInfo(cur);
  if(o.nfs)return `<section class="ocard"><p class="note">אלברט סימן שהציור הזה לא מוצע כמקור.</p></section>`;
  if(!o.sizes.length)return `<section class="ocard"><div class="warn">עוד אין מחירי מקורים. אלברט ממלא אותם בטופס, ואחר כך מדביקים את הקוד בהגדרות ← סנכרון.</div></section>`;
  return `<section class="pcard"><header><b>מקור · Original painting</b><small>ציור מקורי בעבודת יד בגודל שהלקוח בוחר</small></header><div class="tscroll"><table><thead><tr><th style="text-align:right;padding-inline-start:16px">גודל</th><th>מחיר</th></tr></thead><tbody>
  ${o.sizes.map(r=>`<tr><td class="sz"><b>${sz(r.s,S.unit)}</b><small>${sz(r.s,S.unit==='cm'?'in':'cm')}</small></td><td><button type="button" class="${osel===r.s?'on':''}" data-os="${r.s}">${$f(r.p)}</button></td></tr>`).join('')}
  </tbody></table></div></section>`}
""")
R("  if(kind==='orig')h+=origHTML();","  if(kind==='orig'){h+=origHTML();if(osel)h+=wallSVG()}")
R("if(kind==='orig'){const o=origInfo(cur);if(!o.price)return null;return {id:cur.id,n:cur.n,spec:'Original painting · one of a kind',orig:true,list:o.price}}",
  "if(kind==='orig'){const r=origInfo(cur).sizes.find(x=>x.s===osel);if(!r)return null;return {id:cur.id,n:cur.n,spec:`Original painting · ${sz(r.s,'in')} (${sz(r.s,'cm')})`,orig:true,list:r.p}}")
R("function openArt(id){cur=ART.find(a=>a.id===id);kind=Object.keys(cur.f).length?'print':'orig';","function openArt(id){cur=ART.find(a=>a.id===id);kind=Object.keys(cur.f).length?'print':'orig';osel=(origInfo(cur).sizes[0]||{}).s||null;")
R("  else if(d.sc||d.cx||d.st){","  else if(d.os){osel=d.os}\n  else if(d.sc||d.cx||d.st){")
# mini preview + scene for originals
R("function selIn(){return sel.custom?[sel.w,sel.h]:dims(sel.s)}","function selIn(){if(kind==='orig'&&osel)return dims(osel);return sel.custom?[sel.w,sel.h]:dims(sel.s)}")
R("function drawMini(){const cv=$('mini');if(!cv||!sel)return;const [w,h]=selIn();drawScene(cv,{a:cur,w:w*2.54,h:h*2.54,lbl:inLabel(w,h),fr:sel.fr,",
  "function drawMini(){const cv=$('mini');if(!cv||!(sel||osel))return;const [w,h]=selIn();drawScene(cv,{a:cur,w:w*2.54,h:h*2.54,lbl:inLabel(w,h),fr:kind==='orig'?'stretch':sel.fr,")
R("function wallSVG(){if(!sel)return '';","function wallSVG(){if(!sel&&!osel)return '';")
R("function vrIn(){if(kind==='orig'){const m=(origInfo(cur).dim||'').match(/(\\d+(?:\\.\\d+)?)\\s*[x×X*]\\s*(\\d+(?:\\.\\d+)?)/);return m?[+m[1],+m[2]]:[40,48]}return selIn()}",
  "function vrIn(){if(kind==='orig')return osel?dims(osel):[40,48];return selIn()}")
t=re.sub(r"dims:VR\.dims&&\(kind!=='orig'\|\|!!\(origInfo\(cur\)\.dim\|\|''\)\.match\([^)]*\)\)","dims:VR.dims",t)
assert "origInfo(cur).dim" not in t, 'dim leftover'
R("""    let sizes='',fins='';if(kind!=='orig'&&!sel.custom){""","""    let sizes='',fins='';if(kind==='orig'){sizes=`<div class="vr-sizes" role="group" aria-label="Size">${origInfo(a).sizes.map(r=>`<button type="button" data-cos="${r.s}" aria-pressed="${r.s===osel}">${sz(r.s,'in')}<small>${sz(r.s,'cm')}</small></button>`).join('')}</div>`}
    else if(!sel.custom){""")
R("  if(d.cs){vrSetSize(d.cs);return}","  if(d.cs){vrSetSize(d.cs);return}\n  if(d.cos){osel=d.cos;renderCust();renderDetail();return}")
R("if(Math.abs(dx)<40||kind==='orig'||sel.custom)return;const ss=vrSizes(),i=ss.indexOf(sel.s);const n=dx<0?Math.min(ss.length-1,i+1):Math.max(0,i-1);if(n!==i&&ss[n])vrSetSize(ss[n])",
  "if(Math.abs(dx)<40)return;if(kind==='orig'){const ss=origInfo(cur).sizes.map(r=>r.s),i=ss.indexOf(osel),n=dx<0?Math.min(ss.length-1,i+1):Math.max(0,i-1);if(n!==i&&ss[n]){osel=ss[n];renderCust();renderDetail()}return}if(sel.custom)return;const ss=vrSizes(),i=ss.indexOf(sel.s);const n=dx<0?Math.min(ss.length-1,i+1):Math.max(0,i-1);if(n!==i&&ss[n])vrSetSize(ss[n])")
R("${kind!=='orig'&&!sel.custom?'<div class=\"vr-hint\">","${kind==='orig'||!sel.custom?'<div class=\"vr-hint\">")
R("'ORIGINAL PAINTING · ONE OF A KIND'","'ORIGINAL PAINTING · HAND-PAINTED TO ORDER'")
R("SALES.push(deal);deal.items.filter(x=>x.orig).forEach(x=>{ORIG[x.id]=Object.assign({},ORIG[x.id]||{},{status:'sold'})});","SALES.push(deal);")
R("const json=JSON.stringify({v:1,S:shared,ORIG,T,tour,SALES});","const json=JSON.stringify({v:1,S:shared,ORIG,OS,tour,SALES});")
R("if(o.T)T=o.T;","if(o.T)T=o.T;if(o.OS)OS=o.OS;")
# settings: originals sizes editor
RX(r'  <div class="panel"><h3>מחירי מקורים לפי קבוצה \(\$\)</h3>.*?</tbody></table></div></div>\n',
"""  <div class="panel"><h3>מחירי מקורים לפי גודל ($)</h3><p class="note">אלברט ממלא בטופס ושולח קוד. אפשר גם לערוך כאן. מידה באינצ׳ים, למשל 30x40.</p>
    <div class="tiers"><table><thead><tr><th>מידה</th><th>מחיר</th><th></th></tr></thead><tbody>${OS.map((r,i)=>`<tr><td><input data-osz="${i}" value="${esc(r.s)}" placeholder="30x40"></td><td><input inputmode="numeric" data-osp="${i}" value="${r.p||''}" placeholder="$"></td><td><button class="ghost" type="button" data-osdel="${i}" aria-label="מחיקה">✕</button></td></tr>`).join('')}</tbody></table></div>
    <div class="seg"><button class="ghost" type="button" data-act="osadd">+ גודל</button></div></div>
""")
R("  document.querySelectorAll('#settings [data-t]').forEach(i=>{const [s,c]=i.dataset.t.split('|');const v=parseInt(i.value.replace(/[^\\d]/g,''),10)||null;T[s]=T[s]||{};T[s][c]=v});persist()}",
  "  document.querySelectorAll('#settings [data-osz]').forEach(i=>{const k=+i.dataset.osz,m=i.value.match(/(\\d+(?:\\.\\d+)?)\\s*[x×X*]\\s*(\\d+(?:\\.\\d+)?)/);if(OS[k]&&m)OS[k].s=m[1]+'x'+m[2]});\n  document.querySelectorAll('#settings [data-osp]').forEach(i=>{const k=+i.dataset.osp;if(OS[k])OS[k].p=parseInt(i.value.replace(/[^\\d]/g,''),10)||null});persist()}")
R("  if(d.me)S.me=d.me;","  if(d.act==='osadd'){OS.push({s:'',p:null});persist();return renderSettings()}\n  if(d.osdel!==undefined){OS.splice(+d.osdel,1);persist();return renderSettings()}\n  if(d.me)S.me=d.me;")
t=t.replace("הקוד כולל את ההנחות, מחירי המקורים,","הקוד כולל את ההנחות, מחירי המקורים לפי גודל,")
open('tpl7.html','w').write(t);print('ok')

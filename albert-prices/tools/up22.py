t=open('tpl21.html').read()
def R(a,b,n=1):
    global t
    c=t.count(a);assert c>=1,('MISSING',a[:120]);t=t.replace(a,b,n if n else c)
# --- Currency: the store's US dollar prices, shown in Canadian dollars at an editable rate ---
R("let S=Object.assign({rate:3.7,round:'5',unit:'in',verified:false,coll:true,second:25,me:''},L.S||{});",
"""let S=Object.assign({rate:3.7,round:'5',unit:'in',verified:false,coll:true,second:25,me:'',cur:'CAD',fx:1.4235},L.S||{});
if(S.fx===1.4)S.fx=1.4235; // the first Canadian build guessed 1.40; Dana checked the rate on 26 Nov 2026
// prices are kept in US dollars; in Canada they are converted once at load: prints end in 9, originals round up to the hundred
const CUR=S.cur==='CAD'?'CAD':'USD',FX=CUR==='CAD'?(+S.fx||1.4235):1;
const pr=v=>FX===1?v:Math.ceil((v*FX+1)/10)*10-1, oc=v=>FX===1?v:Math.ceil(v*FX/100)*100;
if(FX!==1){for(const f in STD)for(const k in STD[f])for(const fr in STD[f][k]){const o=STD[f][k][fr];if(o&&o.p)o.p=pr(o.p)}
  ART.forEach(a=>{for(const f in a.f)for(const s in a.f[f])for(const fr in a.f[f][s]){const v=a.f[f][s][fr];if(v>0)a.f[f][s][fr]=pr(v)}})}
const fmtC=(n,c)=>((c||'USD')==='CAD'?'C$':'$')+Math.round(n).toLocaleString('en-US');""")
R("const $f=n=>'$'+Math.round(n).toLocaleString('en-US');","const $f=n=>fmtC(n,CUR);")
R("(D.TOUR0||[]).forEach(r=>TOURP[r.id]=r)","(D.TOUR0||[]).forEach(r=>TOURP[r.id]=Object.assign({},r,{p:oc(r.p)}))")
R(".map(r=>({s:r.s,p:(o.ovr&&o.ovr[r.s])||r.p}))",".map(r=>({s:r.s,p:oc((o.ovr&&o.ovr[r.s])||r.p)}))")
R("const MINI={p:120,","const MINI={p:pr(120),")
R("const collPct=list=>!S.coll?0:list>500?20:list>300?15:10;","const collPct=list=>!S.coll?0:list/FX>500?20:list/FX>300?15:10;")
# a package started in one currency is not carried into the other
R("JSON.stringify({S,ORIG,OS,OSV,TOURV,TOURIDS,tour,pkg,SALES})","JSON.stringify({S,ORIG,OS,OSV,TOURV,TOURIDS,tour,pkg,PCUR:CUR,SALES})")
R("let ftab='canvas',discOpen=false;","if((L.PCUR||'USD')!==CUR)pkg=[];\nlet ftab='canvas',discOpen=false;")
# sales remember their currency; totals count only the current one
R("total:CL.items.reduce((s,x)=>s+x.fin,0),pay:CL.pay,","total:CL.items.reduce((s,x)=>s+x.fin,0),cur:CUR,pay:CL.pay,")
R("function renderSales(){const today=dayKey(Date.now());const list=SALES.filter(s=>salesRange==='all'||dayKey(s.ts)===today).sort((a,b)=>b.ts-a.ts);\n  const tot=list.reduce((s,x)=>s+x.total,0)",
  "function renderSales(){const today=dayKey(Date.now());const list=SALES.filter(s=>salesRange==='all'||dayKey(s.ts)===today).sort((a,b)=>b.ts-a.ts);\n  const lc=list.filter(s=>(s.cur||'USD')===CUR),oth=list.filter(s=>(s.cur||'USD')!==CUR),othTot=oth.reduce((s,x)=>s+x.total,0);\n  const tot=lc.reduce((s,x)=>s+x.total,0)")
R("const by={};list.forEach(","const by={};lc.forEach(")
R("const pay={};list.forEach(","const pay={};lc.forEach(")
R("<small>הכנסות</small><b>${$f(tot)}</b>","<small>הכנסות</small><b>${$f(tot)}</b>${oth.length?`<small>+ ${fmtC(othTot,CUR==='CAD'?'USD':'CAD')}</small>`:''}")
R("<span class=\"amt\">${$f(s.total)}</span>","<span class=\"amt\">${fmtC(s.total,s.cur)}</span>")
R("toast('נמכר! '+$f(deal.total)","toast('נמכר! '+fmtC(deal.total,deal.cur)")
# settings: pick the currency and the rate
R('<div class="panel"><h3>מחירי מקורים לפי גודל ($)</h3>','''<div class="panel"><h3>מטבע</h3><div class="seg">${[['CAD','דולר קנדי C$'],['USD','דולר אמריקאי $']].map(([c,l])=>`<button type="button" data-cur="${c}" aria-pressed="${CUR===c}">${l}</button>`).join('')}</div>
    <div class="field"><label for="fxIn">שער: 1 דולר אמריקאי = כמה דולר קנדי</label><input id="fxIn" inputmode="decimal" value="${S.fx}"></div>
    <p class="note">כל המחירים באתר בדולר אמריקאי, והאפליקציה ממירה לפי השער. הדפסים מעוגלים למחיר שמסתיים ב־9, ומקורים מעוגלים למאה הבאה. מכירות שכבר נרשמו נשארות במטבע שבו נמכרו.</p></div>
  <div class="panel"><h3>מחירי מקורים לפי גודל (בדולר אמריקאי, לפני המרה)</h3>''')
R("$('settings').addEventListener('change',()=>{readInputs();renderHome()});","$('settings').addEventListener('change',e=>{if(e.target.id==='fxIn'){const v=parseFloat(e.target.value);if(v>0.5&&v<3){S.fx=v;persist();location.reload()}return}readInputs();renderHome()});")
R("$('settings').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;const d=b.dataset;readInputs();",
  "$('settings').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;const d=b.dataset;if(d.cur){if(d.cur!==CUR){S.cur=d.cur;persist();location.reload()}return}readInputs();")
R("const tot=list.reduce((s,x)=>s+x.total,0);return copy(","const tot=list.filter(s=>(s.cur||'USD')===CUR).reduce((s,x)=>s+x.total,0);return copy(")
R("— ${$f(s.total)} (${s.pay}","— ${fmtC(s.total,s.cur)} (${s.pay}")
t=t.replace("[['CAD','דולר קנדי C$'],['USD','דולר אמריקאי $']]","[['CAD','דולר קנדי (CAD)'],['USD','דולר אמריקאי (USD)']]")
open('tpl22.html','w').write(t);print('ok')

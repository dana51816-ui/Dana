t=open('tpl15.html').read()
def R(a,b,n=1):
    global t
    assert t.count(a)>=1,('MISSING',a[:120]); t=t.replace(a,b,n)
R("ART.forEach(a=>{a.id=a.k.replace(/[^a-z0-9]+/g,'-');","ART.forEach(a=>{a.id=a.id||a.k.replace(/[^a-z0-9]+/g,'-');")
# the tour list ships with the app; a newer list is merged in on each device, keeping anything starred by hand
R("let ftab='canvas',discOpen=false;","""const TOURP={};(D.TOUR0||[]).forEach(r=>TOURP[r.id]=r);
let TOURV=L.TOURV||null;
let TOURIDS=L.TOURIDS||(L.TOURV?['together-we-will-win','peace-will-return']:[]);
if(D.TOURV&&TOURV!==D.TOURV){tour=(D.TOUR0||[]).map(r=>r.id).concat(tour.filter(id=>!TOURP[id]&&!TOURIDS.includes(id)));TOURV=D.TOURV;TOURIDS=(D.TOUR0||[]).map(r=>r.id)}
let ftab='canvas',discOpen=false;""")
R("localStorage.setItem(LSK,JSON.stringify({S,ORIG,OS,OSV,tour,pkg,SALES}))","localStorage.setItem(LSK,JSON.stringify({S,ORIG,OS,OSV,TOURV,TOURIDS,tour,pkg,SALES}))")
R("let ORIG=L.ORIG||{}, T=L.T||{}, OS=L.OS||[], osel=null, tour=L.tour||[], pkg=L.pkg||[], SALES=L.SALES||[];","let ORIG=L.ORIG||{}, T=L.T||{}, OS=L.OS||[], osel=null, tour=L.tour||[], pkg=L.pkg||[], SALES=L.SALES||[];")
# the piece on tour comes first among the original sizes; its row key is 'tour' so it never collides with a commission size
R("function origSizes(a){const o=ORIG[a.id]||{};if(o.nfs)return [];","function origSizes(a){const tp=TOURP[a.id],tr=tp?[{s:tp.s,p:tp.p,k:'tour',tour:true}]:[];return tr.concat(commSizes(a))}\nfunction commSizes(a){const o=ORIG[a.id]||{};if(o.nfs)return [];")
R("function origInfo(a){","const okey=r=>r.k||r.s;const oRow=()=>cur&&osel?origInfo(cur).sizes.find(x=>okey(x)===osel):null;\nfunction origInfo(a){")
R("osel=(origInfo(cur).sizes[0]||{}).s||null;","osel=(s=>s?okey(s):null)(origInfo(cur).sizes[0]);if(TOURP[cur.id])ftab='orig',kind='orig';")
R("const size=it.orig?osel:sel.custom?","const size=it.orig?oRow().s:sel.custom?")
R("function selIn(){if(kind==='orig'&&osel){let [w,h]=dims(osel);","function selIn(){if(kind==='orig'&&osel&&oRow()){let [w,h]=dims(oRow().s);")
R("if(kind==='orig'){const r=origInfo(cur).sizes.find(x=>x.s===osel);if(!r)return null;return {id:cur.id,n:cur.n,spec:`Original painting · ${sz(r.s,'in')} (${sz(r.s,'cm')})`,orig:true,list:r.p}}",
  "if(kind==='orig'){const r=oRow();if(!r)return null;return {id:cur.id,n:cur.n,spec:`Original painting${r.tour?' (one of a kind, on tour)':' (commission)'} · ${sz(r.s,'in')} (${sz(r.s,'cm')})`,orig:true,list:r.p}}")
R("""${o.sizes.map(r=>`<div class="pmr${osel===r.s?' on':''}"><span class="s">${sz(r.s,S.unit)}<small>${sz(r.s,S.unit==='cm'?'in':'cm')}</small></span><button type="button" aria-pressed="${osel===r.s}" data-os="${r.s}">${$f(r.p)}</button></div>`).join('')}""",
  """${o.sizes.map(r=>`${r.tour?'':(o.sizes[0].tour&&r===o.sizes[1]?`<div class="pmr pmsub"><span>בהזמנה אישית, בגודל לבחירה</span></div>`:'')}<div class="pmr${osel===okey(r)?' on':''}${r.tour?' tourrow':''}"><span class="s">${r.tour?'<em>★ המקור בטור</em>':''}${sz(r.s,S.unit)}<small>${sz(r.s,S.unit==='cm'?'in':'cm')}</small></span><button type="button" aria-pressed="${osel===okey(r)}" data-os="${okey(r)}">${$f(r.p)}</button></div>`).join('')}""")
R("<h3>מחירון · ציור מקורי</h3><p class=\"note\">אלברט מצייר את היצירה מחדש בגודל שהלקוח בוחר. נוגעים במחיר כדי לבחור.</p>",
  "<h3>מחירון · ציור מקורי</h3><p class=\"note\">${TOURP[cur.id]?'הציור המקורי שאיתנו בטור, יחיד מסוגו. אפשר גם להזמין מאלברט ציור מקורי בגודל אחר.':'אלברט מצייר את היצירה מחדש בגודל שהלקוח בוחר.'} נוגעים במחיר כדי לבחור.</p>")
# customer view sizes use the same keys
R("""${origInfo(a).sizes.map(r=>`<button type="button" data-cos="${r.s}" aria-pressed="${r.s===osel}">""","""${origInfo(a).sizes.map(r=>`<button type="button" data-cos="${okey(r)}" aria-pressed="${okey(r)===osel}">${r.tour?'★ ':''}""")
R("const ss=origInfo(cur).sizes.map(r=>r.s),i=ss.indexOf(osel)","const ss=origInfo(cur).sizes.map(okey),i=ss.indexOf(osel)")
# the story under the title
R("""<h2 class="dtitle">${esc(a.n)}</h2>""","""<h2 class="dtitle">${esc(a.n)}</h2>${a.aka?`<p class="dsub">באתר: ${esc(a.aka)}</p>`:''}${TOURP[a.id]?`<details class="story"><summary><span>★ בטור · הסיפור של היצירה</span></summary><p>${esc(TOURP[a.id].d)}</p><p class="care">${esc(D.TOURC||'')}</p></details>`:''}""")
# works without a photo yet get a quiet typographic card instead of a broken image
R("""<figure class="g0"><img class="heroimg" src="${artL(a)}" alt="${esc(a.n)}"></figure>""","""<figure class="g0">${a.img===null?`<div class="noimg"><span>Albert Levi · Original</span><b>${esc(a.n)}</b><small>תמונה תתווסף בקרוב</small></div>`:`<img class="heroimg" src="${artL(a)}" alt="${esc(a.n)}">`}</figure>""")
R("""<div class="art ph" style="background:${artBg(a)}"><img src="${img(a)}" alt="" loading="lazy" decoding="async" onerror="this.remove();this.parentNode&&this.parentNode.classList.remove('ph')">""",
  """<div class="art ph" style="background:${artBg(a)}">${a.img===null?`<div class="noimg sm"><b>${esc(a.n)}</b><small>Original</small></div>`:`<img src="${img(a)}" alt="" loading="lazy" decoding="async" onerror="this.remove();this.parentNode&&this.parentNode.classList.remove('ph')">`}""")
# tiles: elegant star, and the tour price for pieces on tour
R("""${onTour?'<span class="star">⭐ בטור</span>':''}""","""${onTour?'<span class="star">★</span>':''}""")
R("""const pr=[m!=null?`<span>הדפס <b>${$f(m)}</b></span>`:'',o&&o.min?`<span>מקור <b>${$f(o.min)}</b></span>`:''].filter(Boolean).join('')||'<span>מקור</span>';""",
  """const tp=TOURP[a.id];const pr=tp?`<span>מקור בטור <b>${$f(tp.p)}</b></span>${m!=null?`<span>הדפס <b>${$f(m)}</b></span>`:''}`:[m!=null?`<span>הדפס <b>${$f(m)}</b></span>`:'',o&&o.min?`<span>מקור <b>${$f(o.min)}</b></span>`:''].filter(Boolean).join('')||'<span>מקור</span>';""")
R('<h2>בטור</h2>','<h2>המקורים שבטור</h2>')
R("""פותחים יצירה ולוחצים ⭐ כדי להוסיף""","""פותחים יצירה ולוחצים ☆ כדי להוסיף""")
css=r"""
/* ===================== v6: originals on tour ===================== */
.tile .star{position:absolute;top:8px;inset-inline-start:8px;width:26px;height:26px;display:grid;place-items:center;border-radius:50%;background:var(--ink);color:#e9c98b;font-size:.82rem;padding:0;box-shadow:0 2px 6px rgba(0,0,0,.18)}
.tile .art{position:relative}
#tourWrap .sec h2{font-family:var(--serif)}
.pmr.tourrow{background:color-mix(in srgb,var(--bronze) 9%,transparent)}
.pmr.tourrow .s em{font-style:normal;font-family:var(--body);font-size:.68rem;font-weight:600;color:var(--bronze);letter-spacing:.04em;margin-bottom:4px}
.pmr.pmsub{display:block;padding:14px 0 6px;font-size:.72rem;font-weight:600;color:var(--muted);border-bottom:1px solid var(--line)}
.story{margin:14px 16px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.story summary{list-style:none;cursor:pointer;padding:12px 0;font-size:.85rem;font-weight:600;color:var(--bronze);display:flex;justify-content:space-between;align-items:center}
.story summary::-webkit-details-marker{display:none}
.story summary::after{content:"+";font-size:1.1rem;color:var(--muted)}
.story[open] summary::after{content:"–"}
.story p{margin:0 0 12px;direction:ltr;text-align:left;font-family:var(--serif);font-size:1rem;line-height:1.55}
.story p.care{font-family:var(--body);font-size:.78rem;color:var(--muted)}
.noimg{width:100%;height:100%;min-height:260px;display:grid;place-content:center;gap:8px;text-align:center;border:1px solid var(--line);background:var(--card);padding:20px}
.noimg span{font-size:.62rem;letter-spacing:.3em;color:var(--muted);text-transform:uppercase}
.noimg b{font-family:var(--serif);font-weight:400;font-size:1.6rem}
.noimg small{font-size:.75rem;color:var(--muted)}
.noimg.sm{position:absolute;inset:12%;min-height:0;padding:8px;gap:4px;box-shadow:0 8px 14px rgba(26,24,20,.14)}
.noimg.sm b{font-size:1rem}
"""
R("</style>",css+"</style>")
R("const m=f==='orig'?origInfo(a).min:fmtMin(a,f);return `<button type=\"button\" role=\"tab\" data-tab=\"${f}\" aria-pressed=\"${ftab===f}\"><b>${l}</b><small>${s}</small><em>${m!=null?'מ־'+$f(m):'—'}</em></button>`",
  "const tp=f==='orig'&&TOURP[a.id];const m=f==='orig'?origInfo(a).min:fmtMin(a,f);return `<button type=\"button\" role=\"tab\" data-tab=\"${f}\" aria-pressed=\"${ftab===f}\"><b>${l}</b><small>${tp?'★ בטור':s}</small><em>${tp?$f(tp.p):m!=null?'מ־'+$f(m):'—'}</em></button>`")
R("סנכרון בין אלברט לעירש","סנכרון בין אלברט להירש")
t=t.replace("'עירש'","'הירש'")
# the salesperson is Hirsh; carry over devices that already saved the old spelling
R("let ftab='canvas',discOpen=false;","if(S.me==='עירש')S.me='הירש';SALES.forEach(s=>{if(s.by==='עירש')s.by='הירש'});\nlet ftab='canvas',discOpen=false;")
open('tpl16.html','w').write(t);print('ok')

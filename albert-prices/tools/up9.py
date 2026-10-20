import re
t=open('tpl8.html').read()
def R(a,b):
    global t
    assert a in t,('MISSING',a[:100]); t=t.replace(a,b,1)
# ---------- CSS ----------
R(".hero{padding-block:14px 4px;display:grid;gap:12px}",""".hero{padding-block:10px 4px;display:grid;gap:10px}
.stick{position:sticky;top:env(safe-area-inset-top,0px);z-index:8;background:var(--wall);margin-inline:-16px;padding:8px 16px 10px;box-shadow:0 8px 16px -14px rgba(40,50,90,.35)}""")
R(".promo{background:var(--navy-deep);",".promo{background:var(--navy-deep);font-size:.62rem!important;padding:7px 12px!important;")
R(".tile .tp{font-size:.82rem;color:var(--muted);margin-top:-3px}",".tile .tp{font-size:.8rem;color:var(--muted);margin-top:-3px;display:flex;gap:4px 10px;flex-wrap:wrap}")
R(".qa{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:2px}",".qa{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:12px}")
R(".qa button{border:1px solid var(--line);background:var(--card);border-radius:16px;padding:10px 8px;display:grid;gap:2px;justify-items:center;text-align:cent",
  ".qa button{border:1px solid var(--line);background:var(--card);border-radius:14px;padding:8px 10px;display:grid;grid-template-columns:auto 1fr;grid-template-rows:auto auto;column-gap:8px;align-items:center;text-align:right;justify-items:start;text-align:righ")
R(".qa .ic{width:30px;height:30px;border-radius:10px;display:grid;place-items:center;font-size:1rem;margin-bottom:2px}",".qa .ic{grid-row:1/3;width:30px;height:30px;border-radius:10px;display:grid;place-items:center;font-size:.95rem}\n.qa b{font-size:.8rem!important;line-height:1.2}")
R(".heroimg{display:block;max-width:100%;max-height:min(42vh,320px);",".heroimg{display:block;max-width:100%;max-height:min(30vh,240px);")
R(".dtitle{font-family:var(--display);font-stretch:112%;font-weight:800;font-size:clamp(1.8rem,8vw,2.7rem);",".dtitle{font-family:var(--display);font-stretch:112%;font-weight:800;font-size:clamp(1.45rem,6.4vw,2.2rem);")
R(".kind{display:grid;grid-template-columns:1fr 1fr;",".kind{display:grid;grid-auto-flow:column;grid-auto-columns:1fr;")
R(".kind button{border:0;background:none;color:#fff;border-radius:12px;padding:10px;font-weight:600}",".kind button{border:0;background:none;color:#fff;border-radius:12px;padding:10px 6px;font-weight:600;font-size:.9rem;line-height:1.15}\n.kind button small{display:block;font-weight:400;font-size:.7rem;opacity:.8}")
R("td button{border:1.5px solid transparent;background:var(--soft);","td button{border:1.5px solid transparent;background:transparent;color:var(--ink);")
R("td button.on{background:var(--sel-bg);color:var(--sel-fg)}","td button.on{background:var(--sel-bg);color:var(--sel-fg);box-shadow:0 4px 12px -6px rgba(40,60,120,.5)}\ntr.sel td{background:color-mix(in srgb,var(--navy) 6%,transparent)}\ntbody tr{cursor:pointer}\n@media (hover:hover){td button:hover:not(.on){background:var(--soft)}}")
R(".custom{border-top:1px solid var(--line);padding:12px 16px 14px;display:grid;gap:10px;",".custom summary{cursor:pointer;font-weight:600;font-size:.9rem;color:var(--accent);list-style:none}\n.custom summary::-webkit-details-marker{display:none}\n.custom summary::before{content:'＋ '}\n.custom[open] summary::before{content:'－ '}\n.custom{border-top:1px solid var(--line);padding:12px 16px 14px;display:grid;gap:10px;")
R(".pbar .wrap{display:grid;grid-template-columns:minmax(0,1fr);gap:9px;padding-block:12px 12px}",".pbar .wrap{display:grid;grid-template-columns:minmax(0,1fr);gap:8px;padding-block:10px 10px}\n.dtog{border:0;background:rgba(255,255,255,.12);color:#fff;border-radius:999px;padding:3px 10px;font-size:.72rem;margin-top:4px;display:inline-flex;gap:6px;align-items:center}\n.dtog .coll{padding:2px 7px}")
R(".pval{font-family:var(--display);font-stretch:112%;font-weight:800;font-size:2.15rem;",".pval{font-family:var(--display);font-stretch:112%;font-weight:800;font-size:1.95rem;")
# ---------- home markup ----------
R("""    <div class="eyebrow">USA TOUR · PRICE GUIDE</div>
    <h1 class="greet">על איזו יצירה <em>הלקוח שואל?</em></h1>
    <div class="searchbox">""","""    <div class="stick"><div class="searchbox">""")
R("""      <button class="clear" id="clearQ" type="button" aria-label="ניקוי החיפוש" hidden>✕</button>
    </div>
  </section>""","""      <button class="clear" id="clearQ" type="button" aria-label="ניקוי החיפוש" hidden>✕</button>
    </div></div>
  </section>""")
R('placeholder="שם היצירה, למשל Freedom"','placeholder="איזו יצירה הלקוח שואל? למשל Freedom"')
R("""  <div id="tourWrap"><div class="sec"><h2>⭐ בטור</h2><span id="tourCount"></span></div><div class="tourrow" id="tour"></div></div>
  <div class="qa" id="qa"></div>""","""  <div class="qa" id="qa"></div>
  <div id="tourWrap"><div class="sec"><h2>⭐ בטור</h2><span id="tourCount"></span></div><div class="tourrow" id="tour"></div></div>""")
R("$('tourWrap').hidden=!!q;","$('tourWrap').hidden=!!q||!tr.length;")
R("""  const badge=o&&!o.nfs?`<span class="badge">מקור${o.min?' מ־'+$f(o.min):''}</span>`:'';
  const pr=m!=null?`הדפס מ־<b>${$f(m)}</b>`:(o&&o.min?`מקור מ־<b>${$f(o.min)}</b>`:'מקור');""","""  const badge='';
  const pr=[m!=null?`<span>הדפס <b>${$f(m)}</b></span>`:'',o&&o.min?`<span>מקור <b>${$f(o.min)}</b></span>`:''].filter(Boolean).join('')||'<span>מקור</span>';""")
# qa compact labels
R("""<b>מחירון מהיר</b><small>כל הגדלים</small>""","""<b>מחירון</b><small>כל הגדלים</small>""")
R("""<b>מכירות היום</b><small>""","""<b>מכירות</b><small>היום """)
# ---------- detail: tabs per format ----------
R("let theme='all',cur=null,","let ftab='canvas',discOpen=false;\nlet theme='all',cur=null,")
R("function openArt(id){cur=ART.find(a=>a.id===id);kind=Object.keys(cur.f).length?'print':'orig';",
  "function openArt(id){cur=ART.find(a=>a.id===id);ftab=['canvas','emb','float'].find(f=>cur.f[f])||'orig';kind=ftab==='orig'?'orig':'print';discOpen=false;")
R("function pickFirst(){for(const f of ['canvas','emb','float'])if(cur.f[f]){","function pickFirst(){for(const f of [ftab,'canvas','emb','float'])if(cur.f[f]){")
R("""    <div class="kind"><button type="button" data-kind="print" aria-pressed="${kind==='print'}"${hasP?'':' disabled'}>הדפס / מהדורה</button><button type="button" data-kind="orig" aria-pressed="${kind==='orig'}"${a.o?'':' disabled'}>מקור${a.o?'':' · אין'}</button></div>""",
"""    <div class="kind" role="tablist">${[['canvas','קנבס','הדפס'],['emb','Embellished','עבודת יד'],['float','מסגרת צפה','הדפס'],['orig','מקור','ציור מקורי']].filter(([f])=>f==='orig'?a.o:a.f[f]).map(([f,l,s])=>`<button type="button" role="tab" data-tab="${f}" aria-pressed="${ftab===f}">${l}<small>${s}</small></button>`).join('')}</div>""")
R("""  else{h+=['canvas','emb','float'].filter(f=>a.f[f]).map(tableHTML).join('');""","""  else{h+=a.f[ftab]?tableHTML(ftab):'';""")
R("  else if(d.kind){kind=d.kind;disc='auto';if(kind==='print'&&!sel)pickFirst()}","  else if(d.tab){ftab=d.tab;kind=ftab==='orig'?'orig':'print';disc='auto';if(kind==='print'&&(!sel||sel.f!==ftab)){sel=null;pickFirst()}}")
# table: whole row highlight + custom collapsible
R("""  for(const s of ss){h+=`<tr><td class="sz">""","""  for(const s of ss){h+=`<tr class="${sel&&!sel.custom&&sel.f===f&&sel.s===s?'sel':''}"><td class="sz">""")
R("""    h+=`<div class="custom"><div class="row"><label>גודל מיוחד</label>""","""    h+=`<details class="custom"${custom.f===f?' open':''}><summary>גודל מיוחד שלא ברשימה</summary><div class="row"><label>גודל</label>""")
m=re.search(r"(<span class=\"note\">\$\{S\.unit==='cm'\?'ס״מ':'אינץ׳'\}</span></div>\$\{res\})</div>`\}",t); assert m,'custom end'
t=t[:m.start()]+m.group(1)+"</details>`}"+t[m.end():]
R("""  ${o.sizes.map(r=>`<tr><td class="sz">""","""  ${o.sizes.map(r=>`<tr class="${osel===r.s?'sel':''}"><td class="sz">""")
# tap anywhere on a row selects its first price
R("$('detail').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;","$('detail').addEventListener('click',e=>{let b=e.target.closest('button');if(!b){const tr=e.target.closest('tbody tr');if(tr)b=tr.querySelector('td button');}if(!b)return;")
# ---------- price bar: one row, discount behind a toggle ----------
m=re.search(r"  \$\('pbar'\)\.innerHTML=`<div class=\"wrap\"><div class=\"prow\">.*?</div></div>`;\n",t,re.S); assert m,'pbar'
t=t[:m.start()]+"""  const dl=disc==='auto'?(p.pct?`אוטומטי −${p.pct}%`:'בלי'):disc?`−${disc}%`:'בלי';
  $('pbar').innerHTML=`<div class="wrap"><div class="prow"><div class="pinfo"><small>${esc(it.spec)}</small><div class="pval"><span data-roll="${p.fin}">${$f(renderBar.last??p.fin)}</span>${p.pct?`<s>${$f(it.list)}</s>`:''}</div>
    <button class="dtog" type="button" data-act="dtog" aria-expanded="${discOpen}">${p.coll?`<span class="coll">COLLECTOR'S</span>`:''}הנחה: ${dl} ${discOpen?'▴':'▾'}</button></div>
  <div class="pbtns"><button class="line" type="button" data-act="add" aria-label="הוספה לחבילה">+ חבילה</button><button class="gold" type="button" data-act="cust">הצג ללקוח</button></div></div>
  ${discOpen?`<div class="disc">${opts.map(d=>`<button type="button" data-disc="${d}" aria-pressed="${disc===d||(d===0&&disc==='auto'&&!opts.includes('auto'))}">${d==='auto'?'אוטומטי':d?d+'%':'בלי'}</button>`).join('')}</div>`:''}</div>`;
"""+t[m.end():]
R("  if(b.dataset.disc!==undefined){disc=b.dataset.disc==='auto'?'auto':+b.dataset.disc;return renderBar()}","  if(b.dataset.act==='dtog'){discOpen=!discOpen;return renderBar()}\n  if(b.dataset.disc!==undefined){disc=b.dataset.disc==='auto'?'auto':+b.dataset.disc;discOpen=false;return renderBar()}")
R(".dbody{display:grid;grid-template-columns:minmax(0,1fr);gap:18px;padding-block:18px 220px}",".dbody{display:grid;grid-template-columns:minmax(0,1fr);gap:16px;padding-block:16px 170px}")
open('tpl9.html','w').write(t);print('ok')

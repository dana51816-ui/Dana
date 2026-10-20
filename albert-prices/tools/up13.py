import re
t=open('tpl12.html').read()
def R(a,b,cnt=1):
    global t
    assert a in t,('MISSING',a[:120]); t=t.replace(a,b,cnt)
def RX(p,b):
    global t
    m=re.search(p,t,re.S); assert m,('NOREGEX',p[:60]); t=t[:m.start()]+b+t[m.end():]
css=r"""
/* ===================== v3: opening, price list, summary ===================== */
/* The opening is one full-bleed room photograph with the name set on it; the work page states every price at once
   as a clean price list (sizes down, finishes across) and spells out the chosen line like a receipt. */
.promo{display:none!important}
#home .hero{position:relative;padding-top:0}
#home .topline{position:absolute;inset:0 0 auto 0;z-index:4;padding:calc(env(safe-area-inset-top,0px) + 14px) 18px 0;background:none!important;border:0!important}
#home .topline .brandlogo,#home .topline .brandlogo *{color:#fff!important}
#home .topline .brandlogo small{opacity:.8}
#home .topline #setBtn{color:#fff;background:transparent!important}
.exhibit{height:min(78vh,640px);min-height:440px;margin:0 calc(-1*var(--gut,16px));width:auto}
.exhibit::before{content:"";position:absolute;inset:0 0 auto 0;height:140px;z-index:2;background:linear-gradient(180deg,rgba(15,13,11,.55),rgba(15,13,11,0));pointer-events:none}
.exhibit .excap{padding:0 22px 34px}
.exhibit .excap .n{font-size:clamp(2rem,9vw,2.8rem);line-height:1.05;margin:6px 0 10px}
.exhibit .excap .p{display:flex;gap:16px;font-size:.85rem}
.exhibit .dots{bottom:16px;top:auto}
.exhibit .count{top:auto;bottom:12px}
.qa{display:grid!important;grid-template-columns:repeat(3,1fr);gap:0;margin:22px 0 6px;border:0!important;background:none!important}
.qa button{background:none!important;border:0!important;border-inline-start:1px solid var(--line)!important;display:flex;flex-direction:column;align-items:center;gap:4px;padding:6px 4px;min-height:84px;color:var(--ink);border-radius:0!important;box-shadow:none!important}
.qa button:first-child{border-inline-start:0!important}
.qa .ic{display:block!important;background:none!important;width:auto;height:auto;color:var(--ink);margin-bottom:2px}
.qa .ic .ico{width:22px;height:22px}
.qa b{font-weight:600;font-size:.8rem;color:var(--muted)}
.qa small{font-family:var(--serif);font-size:1.15rem;color:var(--ink)}
.tile{transition:transform .25s cubic-bezier(.2,.8,.2,1)}
.tile:active{transform:scale(.975)}
/* work page */
.eyebrow{margin:20px 16px 0;font-size:.68rem;letter-spacing:.24em;color:var(--muted);text-transform:uppercase}
.dtitle{margin-top:6px!important}
.kind{grid-auto-columns:1fr;gap:8px!important;border:0!important;margin:18px 16px 0!important}
.kind button{border:1px solid var(--line)!important;background:var(--card)!important;color:var(--ink)!important;display:flex;flex-direction:column;align-items:center;gap:2px;padding:12px 6px!important;min-height:84px}
.kind button b{font-weight:600;font-size:.92rem}
.kind button small{display:block!important;font-size:.7rem;color:var(--muted);opacity:1}
.kind button em{font-style:normal;font-family:var(--serif);font-size:1.12rem;margin-top:4px}
.kind button[aria-pressed="true"]{background:var(--ink)!important;color:var(--wall)!important;border-color:var(--ink)!important}
.kind button[aria-pressed="true"] small{color:color-mix(in srgb,var(--wall) 70%,transparent)}
.plist{display:grid;gap:10px}
.plist h3{margin:6px 0 0;font-family:var(--serif);font-weight:400;font-size:1.45rem}
.plist .note{margin:0}
.pm{border-top:1.5px solid var(--ink)}
.pmr{display:grid;grid-template-columns:minmax(92px,1.25fr) repeat(var(--n),minmax(0,1fr));align-items:stretch;border-bottom:1px solid var(--line)}
.pmh{font-size:.72rem;color:var(--muted);font-weight:600}
.pmh>span{padding:10px 4px;display:flex;flex-direction:column;align-items:center;gap:5px;text-align:center;line-height:1.2}
.pmh>span:first-child{align-items:flex-start;justify-content:flex-end}
.pmh i{width:16px;height:16px;border:1px solid var(--line);display:block}
.pmr .s{padding:12px 0;padding-left:10px;font-family:var(--serif);font-size:1.1rem;direction:ltr;text-align:right;line-height:1.1;display:flex;flex-direction:column;justify-content:center;align-items:flex-start}
.pmr .s small{font-family:var(--body);font-size:.7rem;color:var(--muted);margin-top:3px}
.pmr button,.pmr .na{border:0;background:transparent;font-family:var(--serif);font-size:1.08rem;color:var(--ink);min-height:56px;margin:4px 2px;display:grid;place-items:center;transition:background .2s,color .2s}
.pmr .na{color:var(--line)}
.pmr button[aria-pressed="true"]{background:var(--ink);color:var(--wall)}
.pmr.on{background:var(--soft)}
.pmr button.w{color:var(--warn);outline:1px dashed var(--warn);outline-offset:-5px}
.legend{font-size:.72rem;color:var(--muted);display:flex;gap:6px;align-items:center}
.legend i{width:14px;height:10px;outline:1px dashed var(--warn);display:inline-block}
.sum{border:1px solid var(--line);background:var(--card);padding:18px 18px 16px;display:grid;gap:0}
.sum .h{font-size:.68rem;letter-spacing:.22em;color:var(--muted);text-transform:uppercase;margin-bottom:8px}
.sum dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:0}
.sum dt,.sum dd{padding:9px 0;border-bottom:1px solid var(--line);margin:0;font-size:.92rem}
.sum dt{color:var(--muted)}
.sum dd{text-align:left;direction:ltr;font-weight:600;unicode-bidi:plaintext}
.sum dd.off{color:var(--bronze)}
.sum .tot{display:flex;justify-content:space-between;align-items:baseline;padding-top:14px}
.sum .tot span{font-size:.9rem;font-weight:600}
.sum .tot b{font-family:var(--serif);font-weight:400;font-size:2.1rem;letter-spacing:-.01em}
.sum .rates{margin-top:10px;font-size:.72rem;color:var(--muted)}
"""
R("</style>",css+"</style>")
# quick actions: line icons, values in serif
R("""<span class="ic">$</span><b>מחירון מהיר</b><small>כל הגדלים</small>""","""<span class="ic"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h10"/></svg></span><b>מחירון מהיר</b><small>כל הגדלים</small>""")
R("""<span class="ic" style="background:color-mix(in srgb,var(--ok) 25%,transparent)">✓</span>""","""<span class="ic"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 19V9M10 19V5M16 19v-7M22 19H2"/></svg></span>""")
R("""<span class="ic" style="background:color-mix(in srgb,var(--cobalt) 22%,transparent)">◫</span>""","""<span class="ic"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="7" width="18" height="13"/><path d="M8 7V4h8v3"/></svg></span>""")
R('<h2>⭐ בטור</h2>','<h2>בטור</h2>')
# format cards carry their starting price
R("""<div class="kind" role="tablist">${[['canvas','קנבס','הדפס'],['emb','Embellished','עבודת יד'],['float','מסגרת צפה','הדפס'],['orig','מקור','ציור מקורי']].filter(([f])=>f==='orig'?a.o:a.f[f]).map(([f,l,s])=>`<button type="button" role="tab" data-tab="${f}" aria-pressed="${ftab===f}">${l}<small>${s}</small></button>`).join('')}</div>""",
"""<div class="kind" role="tablist">${[['canvas','קנבס','הדפס'],['emb','Embellished','הדפס + עבודת יד'],['float','מסגרת צפה','הדפס'],['orig','מקור','ציור מקורי']].filter(([f])=>f==='orig'?a.o:a.f[f]).map(([f,l,s])=>{const m=f==='orig'?origInfo(a).min:fmtMin(a,f);return `<button type="button" role="tab" data-tab="${f}" aria-pressed="${ftab===f}"><b>${l}</b><small>${s}</small><em>${m!=null?'מ־'+$f(m):'—'}</em></button>`}).join('')}</div>""")
R("""    <h2 class="dtitle">""","""    <p class="eyebrow">Albert Levi · ${a.o?'Original & Editions':'Editions'}</p><h2 class="dtitle">""")
# the price list: sizes down, finishes across, every price visible
RX(r"  const fr0=\(sel&&sel\.f===f.*?\.join\(''\)\}</div>`;\n",r"""  const sw={stretch:'linear-gradient(135deg,#e4dfd6,#bdb6aa)',black:'#1a1814',white:'#ffffff',rolled:'repeating-linear-gradient(90deg,#f1ede5 0 3px,#ddd6ca 3px 6px)',espresso:'#3d271c',natural:'#c39a66'};
  let h=`<section class="plist"><h3>מחירון · ${f==='canvas'?'קנבס':f==='emb'?'Embellished':'מסגרת צפה'}</h3><p class="note">${FMT[f].d}. נוגעים במחיר כדי לבחור.</p>
  <div class="pm" style="--n:${cols.length}"><div class="pmr pmh"><span>מידה</span>${cols.map(c=>`<span><i style="background:${sw[c]||'var(--soft)'}"></i>${FR[c].he}</span>`).join('')}</div>
  ${ss.map(s=>{const rowOn=sel&&!sel.custom&&sel.f===f&&sel.s===s;return `<div class="pmr${rowOn?' on':''}"><span class="s">${sz(s,S.unit)}<small>${sz(s,S.unit==='cm'?'in':'cm')}</small></span>${cols.map(fr=>{const c=cell(cur,f,s,fr);if(!c)return '<span class="na">—</span>';const on=rowOn&&sel.fr===fr;
    return `<button type="button" class="${c.w?'w':''}" aria-pressed="${!!on}" aria-label="${sz(s,'in')} ${FR[fr].he} ${$f(usd(c.ils))}" data-c="${f}|${s}|${fr}">${$f(usd(c.ils))}</button>`}).join('')}</div>`}).join('')}</div>
  ${ss.some(s=>cols.some(fr=>{const c=cell(cur,f,s,fr);return c&&c.w}))?`<p class="legend"><i></i>מחיר חריג באתר. בודקים לפני שאומרים ללקוח</p>`:''}`;
""")
RX(r"  h\+=`<h4>גודל · מחיר</h4><div class=\"tiles\">.*?\.join\(''\)\}</div>`;\n","")
# originals as the same price list
R("""  return `<section class="cfg"><p class="note">ציור מקורי בעבודת יד, בגודל שהלקוח בוחר</p><h4>גודל · מחיר</h4><div class="tiles">${o.sizes.map(r=>`<button type="button" class="sz2" aria-pressed="${osel===r.s}" data-os="${r.s}"><span class="s">${sz(r.s,S.unit)}<small>${sz(r.s,S.unit==='cm'?'in':'cm')}</small></span><span class="p">${$f(r.p)}</span></button>`).join('')}</div></section>`}""",
"""  return `<section class="plist"><h3>מחירון · ציור מקורי</h3><p class="note">אלברט מצייר את היצירה מחדש בגודל שהלקוח בוחר. נוגעים במחיר כדי לבחור.</p>
  <div class="pm" style="--n:1"><div class="pmr pmh"><span>מידה</span><span>מחיר</span></div>${o.sizes.map(r=>`<div class="pmr${osel===r.s?' on':''}"><span class="s">${sz(r.s,S.unit)}<small>${sz(r.s,S.unit==='cm'?'in':'cm')}</small></span><button type="button" aria-pressed="${osel===r.s}" data-os="${r.s}">${$f(r.p)}</button></div>`).join('')}</div></section>`}""")
# the chosen line, spelled out
R("""function wallSVG(){""","""function fmtMin(a,f){let m=Infinity;for(const s in a.f[f])for(const fr in a.f[f][s]){const c=cell(a,f,s,fr);if(c&&!c.w&&c.ils<m)m=c.ils}return isFinite(m)?usd(m):null}
function sumHTML(){const it=current();if(!it)return '<div id="sumcard"></div>';const p=single(it);
  const fmt=it.orig?'ציור מקורי':sel.f==='canvas'?'הדפס על קנבס':sel.f==='emb'?'Embellished Edition':'מסגרת צפה';
  const size=it.orig?osel:sel.custom?sel.w+'x'+sel.h:sel.s;
  const rows=[['יצירה',esc(it.n)],['סוג',fmt],['מידה',`${sz(size,'in')} · ${sz(size,'cm')}`]];
  if(!it.orig)rows.push(['גימור',FR[sel.fr].he+(sel.custom?' · גודל מיוחד':'')]);
  rows.push(['מחיר מחירון',$f(it.list)]);
  return `<div class="sum" id="sumcard"><div class="h">הבחירה שלך</div><dl>${rows.map(([k,v])=>`<dt>${k}</dt><dd>${v}</dd>`).join('')}${p.pct?`<dt>${p.coll?'Collector\\'s Rate':'הנחה'} ${p.pct}%</dt><dd class="off">−${$f(it.list-p.fin)}</dd>`:''}</dl>
  <div class="tot"><span>מחיר ללקוח</span><b>${$f(p.fin)}</b></div>${S.coll&&!it.orig?`<p class="rates">Collector's Rate אוטומטי: 10% · 15% מעל $300 · 20% מעל $500. משנים בכפתור ההנחה למטה.</p>`:''}</div>`}
function wallSVG(){""")
R("""  if(kind==='orig'){h+=origHTML();if(osel)h+=wallSVG()}""","""  if(kind==='orig'){h+=origHTML();h+=sumHTML();if(osel)h+=wallSVG()}""")
R("""    if(c&&c.w)h+=`<div class="warn"><b>כדאי לבדוק לפני שאומרים ללקוח.</b> במחירון באתר: ${esc(c.w)}.</div>`;
    h+=wallSVG()}""","""    if(c&&c.w)h+=`<div class="warn"><b>כדאי לבדוק לפני שאומרים ללקוח.</b> במחירון באתר: ${esc(c.w)}.</div>`;
    h+=sumHTML();h+=wallSVG()}""")
# keep the summary in step with the discount chosen in the bar
R("""  $('pbar').hidden=false;roll($('pbar'));renderBar.last=p.fin;renderFab()}""","""  $('pbar').hidden=false;roll($('pbar'));renderBar.last=p.fin;const sc=$('sumcard');if(sc&&!$('detail').hidden)sc.outerHTML=sumHTML();renderFab()}""")
open('tpl13.html','w').write(t);print('ok')

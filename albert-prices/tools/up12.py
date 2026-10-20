import re
t=open('tpl11.html').read()
def R(a,b):
    global t
    assert a in t,('MISSING',a[:100]); t=t.replace(a,b,1)
def RX(p,b):
    global t
    m=re.search(p,t,re.S); assert m,('NOREGEX',p[:60]); t=t[:m.start()]+b+t[m.end():]
# fonts
R('family=Bellefair&family=Heebo:wght@300;400;500;600','family=Frank+Ruhl+Libre:wght@300;400;500&family=Assistant:wght@300;400;600&family=Bellefair&family=Heebo:wght@300;400;500;600')
# remove editorial span rule
t=re.sub(r"\.grid \.tile:nth-child\(5n\+1\)[^\n]*\n","",t)
css=r"""
/* ===================== VIEWING ROOM v2 ===================== */
/* Layout: a quiet viewing room — stone-toned walls, real room photographs as the opening, a uniform catalogue grid, and an Apple-style configurator: pick a finish, tap a size tile, the price waits at the bottom. Bordeaux is reserved for the one action that matters. */
:root{
  --wall:#f7f6f2; --card:#ffffff; --ink:#1a1814; --muted:#857f76; --line:#e4e0d8; --soft:#efede8; --hang:#ecebe6;
  --acc:#7a2e2a; --on-acc:#ffffff; --bronze:#8a6a3a; --sel-bg:#1a1814; --sel-fg:#f7f6f2;
  --serif:"Frank Ruhl Libre","Bellefair",Georgia,serif; --body:"Assistant","Heebo",system-ui,sans-serif;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --wall:#141311; --card:#1a1917; --ink:#eeeae3; --muted:#9c968c; --line:#2c2a26; --soft:#1f1e1b; --hang:#1d1c19;
  --acc:#c4705f; --on-acc:#141311; --bronze:#c9a66b; --sel-bg:#eeeae3; --sel-fg:#141311; color-scheme:dark}}
:root[data-theme="dark"]{
  --wall:#141311; --card:#1a1917; --ink:#eeeae3; --muted:#9c968c; --line:#2c2a26; --soft:#1f1e1b; --hang:#1d1c19;
  --acc:#c4705f; --on-acc:#141311; --bronze:#c9a66b; --sel-bg:#eeeae3; --sel-fg:#141311; color-scheme:dark}
body{font-family:var(--body);font-size:16px}
.ico{width:18px;height:18px;stroke:currentColor;fill:none;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round;flex:none}
/* header */
.brandlogo .t b{font-family:var(--serif);font-weight:400;font-size:1.25rem;letter-spacing:.36em}
#setBtn{border:0;width:44px;height:44px}
#setBtn .ico{width:22px;height:22px}
/* opening: real rooms */
.exhibit{height:min(58vh,500px);min-height:360px;background:#2a2723;margin-top:4px}
.exhibit .sl{display:block}
.exhibit .frame{position:absolute;inset:0;padding:0}
.exhibit .frame img{width:100%;height:100%;max-width:none;max-height:none;object-fit:cover;filter:none}
.exhibit .sl.on .frame img{animation:kb 9s ease-out both}
.exhibit .light{background:linear-gradient(180deg,rgba(20,18,16,.05) 40%,rgba(20,18,16,.72))}
.exhibit .excap{position:absolute;inset:auto 0 0 0;padding:20px 22px 24px;background:none}
.exhibit .excap .k{color:rgba(255,255,255,.75)}
.exhibit .excap .n{color:#fff;font-family:var(--serif);font-weight:400}
.exhibit .excap .p{color:rgba(255,255,255,.8)}
.exhibit .excap .p b{color:#fff}
.exhibit .dots i{background:rgba(255,255,255,.35)}
.exhibit .dots i.on{background:#fff}
.exhibit .count{color:rgba(255,255,255,.8)}
/* catalogue grid: uniform */
.grid{grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:28px 12px}
.art{aspect-ratio:1;background:var(--hang)!important}
.art img{padding:15%;filter:drop-shadow(0 8px 10px rgba(26,24,20,.22)) drop-shadow(0 1px 1px rgba(26,24,20,.12))}
.tile .tn{font-family:var(--serif);font-size:1.05rem;font-weight:400}
.tile .tp{font-size:.78rem}
.tile .tp b{font-weight:600}
.sec h2,.shead h2,.pcard header b,.dtitle,.vr-title,.pval,.vr-price,.kpi b,.totals .grand,.bigtotal,.item .nm,.item .pr,.deal .amt,.tile .tn,.excap .n{font-family:var(--serif)!important}
/* work page */
.navrow{padding:8px 12px}
.iconbtn{border:0!important;display:inline-flex;align-items:center;gap:6px;padding:10px 8px;min-height:44px;font-size:.85rem}
.iconbtn[aria-pressed="true"]{background:transparent!important;color:var(--acc)!important}
.iconbtn[aria-pressed="true"] .ico{fill:currentColor}
.hgal{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;background:var(--hang)}
.hgal::-webkit-scrollbar{display:none}
.hgal figure{flex:none;width:100%;aspect-ratio:1/1;max-height:62vh;margin:0;scroll-snap-align:center;display:grid;place-items:center;overflow:hidden}
.hgal .g0{padding:13%}
.hgal .g0 img{max-width:100%;max-height:100%;object-fit:contain;filter:drop-shadow(0 18px 18px rgba(26,24,20,.28)) drop-shadow(0 2px 2px rgba(26,24,20,.15))}
.hgal .gv img{width:100%;height:100%;object-fit:cover}
.gdots{display:flex;justify-content:center;gap:6px;padding:12px 0 0}
.gdots i{width:6px;height:6px;border-radius:50%;background:var(--line)}
.gdots i.on{background:var(--ink)}
.gnote{text-align:center;font-size:.72rem;color:var(--muted);padding-top:6px}
.dtitle{font-size:clamp(1.9rem,8vw,2.5rem);margin:18px 16px 2px;font-weight:400}
.dsub{margin:0 16px;color:var(--muted);font-size:.85rem}
.kind{display:grid!important;grid-auto-flow:column;grid-auto-columns:1fr;margin:18px 16px 0;padding:0;border:1px solid var(--line);border-bottom:1px solid var(--line);column-gap:0}
.kind button{padding:12px 4px;border:0!important;margin:0;font-size:.9rem;color:var(--muted)}
.kind button[aria-pressed="true"]{background:var(--ink)!important;color:var(--wall)!important}
.dbody{padding-top:4px;gap:20px}
.cfg{display:grid;gap:12px}
.cfg h4{margin:8px 0 0;font-size:.75rem;color:var(--muted);font-weight:600;letter-spacing:.06em}
.fins{display:flex;gap:18px;flex-wrap:wrap}
.fins button{border:0;background:transparent;display:flex;align-items:center;gap:8px;padding:6px 0;color:var(--muted);font-size:.9rem;min-height:44px}
.fins i{width:22px;height:22px;display:block;border:1px solid var(--line)}
.fins button[aria-pressed="true"]{color:var(--ink);font-weight:600}
.fins button[aria-pressed="true"] i{outline:1.5px solid var(--ink);outline-offset:3px}
.tiles{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.sz2{border:1px solid var(--line);background:var(--card);padding:12px 14px;display:flex;justify-content:space-between;align-items:center;gap:8px;min-height:60px;text-align:right}
.sz2 .s{font-family:var(--serif);font-size:1.12rem;direction:ltr;line-height:1.1}
.sz2 .s small{display:block;font-family:var(--body);font-size:.7rem;color:var(--muted);margin-top:3px}
.sz2 .p{font-family:var(--serif);font-size:1.08rem;color:var(--ink)}
.sz2[aria-pressed="true"]{border-color:var(--ink);box-shadow:inset 0 0 0 1px var(--ink)}
.sz2.w{border-style:dashed;border-color:var(--warn)}
.sz2.w .p{color:var(--warn)}
.cfg .note{font-size:.8rem}
.custom{padding:4px 0 0}
/* price bar: the one bordeaux action */
.pbar .gold{background:var(--acc)!important;color:var(--on-acc)!important}
.pbar .line{border:0!important;text-decoration:underline;text-underline-offset:4px;padding-inline:8px}
.vr-cta .gold{background:var(--acc)!important;color:var(--on-acc)!important}
.pval{font-size:2rem}
.toast{bottom:calc(120px + env(safe-area-inset-bottom,0px))}
"""
R("</style>",css+"</style>")
# header icon
R('<button class="pill" id="setBtn" type="button" aria-label="הגדרות"><span aria-hidden="true">⚙︎</span> הגדרות</button>','<button class="pill" id="setBtn" type="button" aria-label="הגדרות"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/></svg></button>')
# images
R("const img=a=>'thumbs/'+a.id+'.webp';","const img=a=>'art-sm/'+a.id+'.webp';const artL=a=>'art/'+a.id+'.webp';const VIEWS=D.VIEWS||{};const views=a=>Array.from({length:VIEWS[a.id]||0},(_,i)=>'views/'+a.id+'-'+i+'.webp');")
R("im=new Image();im.decoding='async';im.src=img(a);","im=new Image();im.decoding='async';im.src=artL(a);")
R("const iw=im.naturalWidth,ih=im.naturalHeight,ins=.085;","const iw=im.naturalWidth,ih=im.naturalHeight,ins=0;")
# exhibit uses room photos
R("""<div class="frame"><img src="${img(a)}" alt="${esc(a.n)}" ${i>1?'loading="lazy"':''}>""","""<div class="frame"><img src="${views(a)[0]||artL(a)}" alt="${esc(a.n)}" ${i>1?'loading="lazy"':''}>""")
# work page hero gallery + subtitle
R("""    <img class="heroimg" src="${img(a)}" alt="${esc(a.n)}" onerror="this.remove()">""","""    <div class="hgal" id="hgal">${[`<figure class="g0"><img class="heroimg" src="${artL(a)}" alt="${esc(a.n)}"></figure>`].concat(views(a).map(v=>`<figure class="gv"><img src="${v}" alt="${esc(a.n)} on a wall" loading="lazy"></figure>`)).join('')}</div>
    ${views(a).length?`<div class="gdots" id="gdots">${[0].concat(views(a).map((_,i)=>i+1)).map(i=>`<i class="${i?'':'on'}"></i>`).join('')}</div><div class="gnote">החליקו לראות את היצירה בחדר</div>`:''}""")
R(""".dhero .wrap>.heroimg{background:var(--hang);width:100%;max-width:100%;height:min(42vh,340px);max-height:none;object-fit:contain;padding:30px 12%;box-sizing:border-box;filter:none}""","")
# tiles instead of the price table
RX(r"function tableHTML\(f\)\{.*?\n  h\+=`</tbody></table></div>`;\n",r"""function tableHTML(f){const F=cur.f[f],ss=Object.keys(F).sort((x,y)=>area(x)-area(y)),cols=FRO.filter(fr=>ss.some(s=>F[s][fr]!==undefined));
  const fr0=(sel&&sel.f===f&&!sel.custom&&cols.includes(sel.fr))?sel.fr:cols[0];
  const sw={stretch:'linear-gradient(135deg,#e4dfd6,#bdb6aa)',black:'#1a1814',white:'#ffffff',rolled:'repeating-linear-gradient(90deg,#f1ede5 0 3px,#ddd6ca 3px 6px)',espresso:'#3d271c',natural:'#c39a66'};
  let h=`<section class="cfg"><p class="note">${FMT[f].d}</p>`;
  if(cols.length>1)h+=`<h4>גימור</h4><div class="fins" role="group" aria-label="גימור">${cols.map(c=>`<button type="button" data-fin="${f}|${c}" aria-pressed="${c===fr0}"><i style="background:${sw[c]||'var(--soft)'}"></i>${FR[c].he}</button>`).join('')}</div>`;
  h+=`<h4>גודל · מחיר</h4><div class="tiles">${ss.filter(s=>F[s][fr0]!==undefined).map(s=>{const c=cell(cur,f,s,fr0);const on=sel&&!sel.custom&&sel.f===f&&sel.s===s&&sel.fr===fr0;
    return `<button type="button" class="sz2${c.w?' w':''}" aria-pressed="${!!on}" data-c="${f}|${s}|${fr0}"><span class="s">${sz(s,S.unit)}<small>${sz(s,S.unit==='cm'?'in':'cm')}</small></span><span class="p">${$f(usd(c.ils))}</span></button>`}).join('')}</div>`;
""")
R("""  return h+`</section>`}
function roomSVG""","""  return h+`</section>`}
function roomSVG""")
# originals as tiles
RX(r"  return `<section class=\"pcard\"><header><b>מקור · Original painting</b>.*?</tbody></table></div></section>`\}\n",r"""  return `<section class="cfg"><p class="note">ציור מקורי בעבודת יד, בגודל שהלקוח בוחר</p><h4>גודל · מחיר</h4><div class="tiles">${o.sizes.map(r=>`<button type="button" class="sz2" aria-pressed="${osel===r.s}" data-os="${r.s}"><span class="s">${sz(r.s,S.unit)}<small>${sz(r.s,S.unit==='cm'?'in':'cm')}</small></span><span class="p">${$f(r.p)}</span></button>`).join('')}</div></section>`}
""")
# finish switch handler
R("  else if(d.os){osel=d.os}","  else if(d.fin){const [f,fr]=d.fin.split('|');const F=cur.f[f];const s=(sel&&sel.f===f&&F[sel.s]&&F[sel.s][fr]!==undefined)?sel.s:Object.keys(F).sort((x,y)=>area(x)-area(y)).find(z=>F[z][fr]!==undefined);sel={f,s,fr}}\n  else if(d.os){osel=d.os}")
# gallery dots + remove hero parallax
R("const h=$('detail').querySelector('.heroimg');if(h&&y<600)h.style.transform=`translateY(${y*.28}px) scale(${1+y*.0003})`;","")
R("$('detail').addEventListener('scroll',()=>{","$('detail').addEventListener('scroll',e=>{if(e.target.id==='hgal'){const g=e.target,i=Math.round(Math.abs(g.scrollLeft)/g.clientWidth);document.querySelectorAll('#gdots i').forEach((d,k)=>d.classList.toggle('on',k===i));return}")
t=t.replace("$('detail').addEventListener('scroll',e=>{","$('detail').addEventListener('scroll',e=>{",1)
# scroll events on the gallery don't bubble: listen in capture phase
t=t.replace("const t=$('navt');if(t)t.classList.toggle('on',y>330)},{passive:true});","const t=$('navt');if(t)t.classList.toggle('on',y>330)},{passive:true,capture:true});")
# flight target: painting inside the first gallery figure
R("const hero=$('detail').querySelector('.heroimg');if(!hero)return;\n  const hr=hero.getBoundingClientRect(),cs=getComputedStyle(hero);const pt=parseFloat(cs.paddingTop),pl=parseFloat(cs.paddingLeft);",
  "const hero=$('detail').querySelector('.heroimg');if(!hero)return;\n  const hr=hero.getBoundingClientRect();const pt=0,pl=0;")
# icons in navrow
t=t.replace('<button class="iconbtn" type="button" data-act="back">→ חזרה</button>','<button class="iconbtn" type="button" data-act="back"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>חזרה</button>')
t=t.replace("${tour.includes(a.id)?'⭐ בטור':'☆ להוסיף לטור'}","<svg class=\"ico\" viewBox=\"0 0 24 24\" aria-hidden=\"true\"><path d=\"M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9 6.8 19.6l1-5.8L3.5 9.7l5.9-.9z\"/></svg>${tour.includes(a.id)?'בטור':'לטור'}")
t=t.replace('target="_blank" rel="noopener">↗</a>','target="_blank" rel="noopener" aria-label="באתר"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg></a>')
open('tpl12.html','w').write(t);print('ok')

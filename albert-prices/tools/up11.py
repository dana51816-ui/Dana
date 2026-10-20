t=open('tpl10.html').read()
def R(a,b):
    global t
    assert a in t,('MISSING',a[:100]); t=t.replace(a,b,1)
css=r"""
/* ===== wow layer ===== */
.exhibit{position:relative;margin-inline:-16px;height:min(66vh,560px);min-height:380px;background:var(--hang);overflow:hidden;touch-action:pan-y;cursor:pointer}
.exhibit .sl{position:absolute;inset:0;opacity:0;transition:opacity 1.1s ease;display:grid;grid-template-rows:1fr auto}
.exhibit .sl.on{opacity:1}
.exhibit .frame{position:relative;min-height:0;display:grid;place-items:center;padding:34px 13% 8px}
.exhibit .frame img{max-width:100%;max-height:100%;object-fit:contain;filter:drop-shadow(0 22px 26px rgba(0,0,0,.28)) drop-shadow(0 2px 3px rgba(0,0,0,.12));transform-origin:50% 60%}
.exhibit .sl.on .frame img{animation:kb 7s ease-out both}
@keyframes kb{from{transform:scale(1)}to{transform:scale(1.055)}}
.exhibit .light{position:absolute;inset:0;pointer-events:none;background:radial-gradient(60% 46% at 50% 38%,rgba(255,255,255,.55),transparent 70%)}
.exhibit .cap{padding:6px 22px 26px;display:grid;gap:4px;text-align:right;background:linear-gradient(180deg,transparent,var(--hang) 30%)}
.exhibit .cap .k{font-size:.6rem;letter-spacing:.24em;text-transform:uppercase;color:var(--muted)}
.exhibit .cap .n{font-family:var(--serif);font-size:clamp(1.9rem,8.5vw,2.8rem);line-height:1.02;direction:ltr;text-align:right;color:var(--ink)}
.exhibit .cap .p{font-size:.8rem;color:var(--muted);display:flex;gap:14px;justify-content:flex-start}
.exhibit .cap .p b{color:var(--ink);font-weight:500}
.exhibit .dots{position:absolute;left:22px;bottom:30px;display:flex;gap:6px;direction:ltr}
.exhibit .dots i{width:18px;height:2px;background:color-mix(in srgb,var(--ink) 25%,transparent);transition:background .3s,width .3s}
.exhibit .dots i.on{background:var(--ink);width:30px}
.exhibit .count{position:absolute;top:16px;left:22px;font-size:.62rem;letter-spacing:.2em;color:var(--muted);direction:ltr}
.stick{margin-top:8px}
/* editorial rhythm */
.grid .tile:nth-child(5n+1){grid-column:1/-1}
.grid .tile:nth-child(5n+1) .art{aspect-ratio:16/11}
.grid .tile:nth-child(5n+1) .art img{padding:9% 16%}
.grid .tile:nth-child(5n+1) .tn{font-size:1.6rem}
@media (prefers-reduced-motion:no-preference){
  .grid .tile{animation:none}
  .rv{transform:translateY(18px);transition:transform .8s cubic-bezier(.2,.8,.2,1)}
  .rv.in{transform:none}
}
/* work page depth */
.navrow{display:grid!important;grid-template-columns:auto 1fr auto;gap:10px}
.navt{font-family:var(--serif);font-size:1.05rem;text-align:center;direction:ltr;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;opacity:0;transform:translateY(6px);transition:opacity .25s,transform .25s}
.navt.on{opacity:1;transform:none}
.dhero .wrap>.heroimg{will-change:transform}
#detail.flipping{animation:none!important}
.flipclone{position:fixed;z-index:40;object-fit:contain;pointer-events:none;filter:drop-shadow(0 18px 22px rgba(0,0,0,.25))}
"""
R("</style>",css+"</style>")
R("""    <div class="stick"><div class="searchbox">""","""    <div class="exhibit" id="exhibit" aria-label="יצירות נבחרות"></div>
    <div class="stick"><div class="searchbox">""")
# navrow center title
R("""    <div class="navrow"><button class="iconbtn" type="button" data-act="back">→ חזרה</button><div class="r">""","""    <div class="navrow"><button class="iconbtn" type="button" data-act="back">→ חזרה</button><span class="navt" id="navt">${esc(a.n)}</span><div class="r">""")
# exhibit + reveal + flip + parallax JS
R("document.addEventListener('click',e=>{const b=e.target.closest('#grid [data-id],#tour [data-id]');if(b)openArt(b.dataset.id)});",
r"""document.addEventListener('click',e=>{const b=e.target.closest('#grid [data-id],#tour [data-id]');if(!b)return;const im=b.querySelector('.art img');FLIP=im&&im.complete&&im.naturalWidth?{r:im.getBoundingClientRect(),src:im.currentSrc||im.src,pad:.14}:null;openArt(b.dataset.id)});
/* ---- exhibition carousel ---- */
let FLIP=null;const EX={i:0,t:0,list:[]};
const PICKS=['tree-of-life-blue-life','israel-hamsa','a-noble-peacock','freedom','after-nova-smile-forever','a-moment-of-silence'];
function renderExhibit(){const el=$('exhibit');const tr=tour.map(id=>ART.find(a=>a.id===id)).filter(Boolean);
  EX.list=(tr.length>=2?tr:PICKS.map(id=>ART.find(a=>a.id===id)).filter(Boolean)).slice(0,8);EX.i=Math.min(EX.i,EX.list.length-1);
  el.innerHTML=EX.list.map((a,i)=>{const o=a.o?origInfo(a):null,m=minUSD(a);return `<div class="sl${i===EX.i?' on':''}" data-ex="${a.id}"><div class="frame"><img src="${img(a)}" alt="${esc(a.n)}" ${i>1?'loading="lazy"':''}><span class="light"></span></div>
    <div class="cap"><span class="k">${tr.length>=2?'בטור · ON TOUR':'Albert Levi · Collection'}</span><span class="n">${esc(a.n)}</span><span class="p">${m!=null?`<span>הדפס מ־<b>${$f(m)}</b></span>`:''}${o&&o.min?`<span>מקור מ־<b>${$f(o.min)}</b></span>`:''}</span></div></div>`}).join('')+
    `<span class="count">${String(EX.i+1).padStart(2,'0')} / ${String(EX.list.length).padStart(2,'0')}</span><span class="dots">${EX.list.map((_,i)=>`<i class="${i===EX.i?'on':''}"></i>`).join('')}</span>`;
  exArm()}
function exGo(n){const el=$('exhibit');const L=EX.list.length;if(!L)return;EX.i=(n+L)%L;el.querySelectorAll('.sl').forEach((s,i)=>s.classList.toggle('on',i===EX.i));el.querySelectorAll('.dots i').forEach((d,i)=>d.classList.toggle('on',i===EX.i));const c=el.querySelector('.count');if(c)c.textContent=`${String(EX.i+1).padStart(2,'0')} / ${String(L).padStart(2,'0')}`;exArm()}
function exArm(){clearTimeout(EX.t);if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;EX.t=setTimeout(()=>{if(!document.hidden&&$('detail').hidden)exGo(EX.i+1);else exArm()},5200)}
(function(){const el=$('exhibit');let x0=null,moved=false;el.addEventListener('pointerdown',e=>{x0=e.clientX;moved=false});
  el.addEventListener('pointerup',e=>{if(x0==null)return;const dx=e.clientX-x0;x0=null;if(Math.abs(dx)>40){moved=true;exGo(EX.i+(dx<0?1:-1))}});
  el.addEventListener('click',e=>{if(moved)return;const s=el.querySelector('.sl.on');if(!s)return;const im=s.querySelector('img');FLIP=im&&im.naturalWidth?{r:im.getBoundingClientRect(),src:im.currentSrc||im.src,pad:0}:null;openArt(s.dataset.ex)})})();
/* ---- reveal on scroll (content is visible at rest; this only adds a gentle rise) ---- */
const RIO='IntersectionObserver' in window&&!matchMedia('(prefers-reduced-motion: reduce)').matches?new IntersectionObserver(es=>es.forEach(en=>{if(en.isIntersecting){en.target.classList.add('in');RIO.unobserve(en.target)}}),{rootMargin:'0px 0px -6% 0px'}):null;
function armReveal(){if(!RIO)return;document.querySelectorAll('#grid .tile').forEach((el,i)=>{if(el.getBoundingClientRect().top>innerHeight){el.classList.add('rv');RIO.observe(el)}})}
/* ---- shared-element flight from tile to the work page ---- */
function flyIn(){const f=FLIP;FLIP=null;if(!f||matchMedia('(prefers-reduced-motion: reduce)').matches)return;const hero=$('detail').querySelector('.heroimg');if(!hero)return;
  const hr=hero.getBoundingClientRect(),cs=getComputedStyle(hero);const pt=parseFloat(cs.paddingTop),pl=parseFloat(cs.paddingLeft);
  const to={left:hr.left+pl,top:hr.top+pt,width:hr.width-2*pl,height:hr.height-2*pt};
  const from={left:f.r.left+f.r.width*f.pad,top:f.r.top+f.r.height*f.pad,width:f.r.width*(1-2*f.pad),height:f.r.height*(1-2*f.pad)};
  const c=document.createElement('img');c.src=f.src;c.className='flipclone';Object.assign(c.style,{left:from.left+'px',top:from.top+'px',width:from.width+'px',height:from.height+'px'});document.body.appendChild(c);
  hero.style.opacity='0';$('detail').classList.add('flipping');$('detail').animate([{opacity:0},{opacity:1}],{duration:320,easing:'ease-out'});
  const px=v=>v+'px';const an=c.animate([{left:px(from.left),top:px(from.top),width:px(from.width),height:px(from.height)},{left:px(to.left),top:px(to.top),width:px(to.width),height:px(to.height)}],{duration:520,easing:'cubic-bezier(.2,.8,.2,1)',fill:'forwards'});
  an.onfinish=()=>{hero.style.opacity='';c.remove();$('detail').classList.remove('flipping')}}
/* ---- depth while scrolling the work page ---- */
$('detail').addEventListener('scroll',()=>{const y=$('detail').scrollTop;const h=$('detail').querySelector('.heroimg');if(h&&y<600)h.style.transform=`translateY(${y*.28}px) scale(${1+y*.0003})`;const t=$('navt');if(t)t.classList.toggle('on',y>330)},{passive:true});
""")
R("  $('detail').hidden=false;$('detail').scrollTop=0;renderDetail();history.pushState({d:1},'')}","  $('detail').hidden=false;$('detail').scrollTop=0;renderDetail();flyIn();history.pushState({d:1},'')}")
# render exhibit + reveal with home
R("function renderHome(){","function renderHome(){if(!renderHome.ex){renderHome.ex=1;setTimeout(renderExhibit,0)}setTimeout(armReveal,0);")
open('tpl11.html','w').write(t);print('ok')

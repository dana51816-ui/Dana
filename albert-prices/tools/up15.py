t=open('tpl14.html').read()
def R(a,b):
    global t
    assert a in t,('MISSING',a[:120]); t=t.replace(a,b,1)
css=r"""
/* ===================== v5: gallery-wall banner ===================== */
/* Chosen direction: three of Albert's works hung on a stone wall under a soft light, his name set beneath them like a gallery
   title. Light wall in light mode, a dim gallery wall in dark mode. */
.banner{background:linear-gradient(180deg,#efede7,#e5e2da)!important;color:var(--ink)!important;height:auto!important;display:block!important;
  padding:calc(env(safe-area-inset-top,0px) + 68px) 16px 28px!important;text-align:center}
.banner::after{display:none!important}
.banner::before{background:radial-gradient(60% 55% at 50% 22%,rgba(255,255,255,.75),rgba(255,255,255,0) 70%)!important;z-index:0!important}
.banner .glow{display:none!important}
.banner .wall{position:relative;z-index:1;display:flex;justify-content:center;align-items:center;gap:18px;height:100px;direction:ltr}
.banner .wall img{display:block;height:68px;width:auto;max-width:22vw;object-fit:contain;box-shadow:0 10px 16px rgba(26,24,20,.22),0 1px 2px rgba(26,24,20,.2);
  opacity:0;transform:translateY(-6px);animation:hang .9s cubic-bezier(.2,.8,.2,1) forwards}
.banner .wall img.c{height:96px;max-width:38vw;animation-delay:.12s}
.banner .wall img:last-child{animation-delay:.24s}
@keyframes hang{to{opacity:1;transform:none}}
.banner .in{position:relative;z-index:1;margin-top:24px;gap:6px!important;animation:none!important}
.banner h1{font-weight:300!important;font-size:clamp(2.2rem,10vw,2.7rem)!important;letter-spacing:.1em!important;color:var(--ink)}
.banner .tag{font-family:var(--body)!important;font-style:normal!important;font-size:.64rem!important;letter-spacing:.38em!important;color:var(--muted)!important;text-transform:uppercase}
.banner .eb,.banner .rule{display:none!important}
#home .topline #setBtn{color:var(--ink)!important}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .banner{background:linear-gradient(180deg,#22201c,#1a1916)!important}
  :root:not([data-theme="light"]) .banner::before{background:radial-gradient(60% 55% at 50% 22%,rgba(255,240,215,.10),rgba(255,240,215,0) 70%)!important}
  :root:not([data-theme="light"]) .banner .wall img{box-shadow:0 12px 20px rgba(0,0,0,.55)}}
:root[data-theme="dark"] .banner{background:linear-gradient(180deg,#22201c,#1a1916)!important}
:root[data-theme="dark"] .banner::before{background:radial-gradient(60% 55% at 50% 22%,rgba(255,240,215,.10),rgba(255,240,215,0) 70%)!important}
@media (prefers-reduced-motion:reduce){.banner .wall img{animation:none;opacity:1;transform:none}}
"""
R("</style>",css+"</style>")
R('''<div class="banner" role="banner"><img class="glow" id="bnGlow" alt="" aria-hidden="true"><div class="in">''','''<div class="banner" role="banner"><img class="glow" id="bnGlow" alt="" aria-hidden="true"><div class="wall" id="bnWall" aria-hidden="true"></div><div class="in">''')
R("const g=$('bnGlow'),a=ART.find(x=>x.id==='tree-of-life-blue-life')||ART[0];if(g&&a)g.src=img(a)}",
  "const W=$('bnWall');if(W)W.innerHTML=['hamsa','tree-of-life-blue-life','a-noble-peacock'].map((id,i)=>{const a=ART.find(x=>x.id===id);return a?`<img class=\"${i===1?'c':''}\" src=\"${img(a)}\" alt=\"\">`:''}).join('')}")
open('tpl15.html','w').write(t);print('ok')

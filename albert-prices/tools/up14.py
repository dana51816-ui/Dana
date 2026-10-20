t=open('tpl13.html').read()
def R(a,b):
    global t
    assert a in t,('MISSING',a[:120]); t=t.replace(a,b,1)
css=r"""
/* ===================== v4: the banner ===================== */
/* A compact ink banner replaces the photo carousel: Albert's name set large in Frank Ruhl Libre, a bronze hairline frame,
   and the colour of one painting glowing softly behind it. It reads in a second and leaves the catalogue one thumb away. */
.exhibit{display:none!important}
.banner{position:relative;margin:0 calc(-1*var(--gut,16px));height:calc(clamp(220px,32vh,270px) + env(safe-area-inset-top,0px));padding-top:env(safe-area-inset-top,0px);
  background:#14120f;color:#f3efe8;overflow:hidden;display:grid;place-items:center;text-align:center;isolation:isolate}
.banner .glow{position:absolute;inset:-30%;width:160%;height:160%;object-fit:cover;filter:blur(42px) saturate(1.35);opacity:.5;z-index:-2;animation:bdrift 28s ease-in-out infinite alternate}
.banner::before{content:"";position:absolute;inset:0;z-index:-1;background:radial-gradient(120% 90% at 50% 40%,rgba(20,18,15,0) 0%,rgba(20,18,15,.55) 60%,rgba(14,12,10,.92) 100%)}
.banner::after{content:"";position:absolute;inset:calc(env(safe-area-inset-top,0px) + 14px) 14px 14px;border:1px solid rgba(201,166,107,.6);pointer-events:none}
@keyframes bdrift{from{transform:translate3d(-4%,-2%,0) scale(1)}to{transform:translate3d(4%,3%,0) scale(1.08)}}
.banner .in{display:grid;justify-items:center;gap:10px;padding:0 30px;animation:brise 1.1s cubic-bezier(.2,.8,.2,1) both}
@keyframes brise{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.banner .eb{font-family:var(--body);font-size:.62rem;letter-spacing:.38em;color:#c9a66b;font-weight:600;text-transform:uppercase}
.banner h1{margin:0;font-family:var(--serif);font-weight:300;font-size:clamp(2.4rem,11vw,3.3rem);letter-spacing:.12em;line-height:1;direction:ltr;padding-left:.12em}
.banner .rule{width:44px;height:1px;background:#c9a66b;opacity:.9}
.banner .tag{font-family:var(--serif);font-style:italic;font-size:.95rem;color:rgba(243,239,232,.78);letter-spacing:.04em;direction:ltr}
@media (prefers-reduced-motion:reduce){.banner .glow,.banner .in{animation:none}}
#home .topline{padding:calc(env(safe-area-inset-top,0px) + 18px) 22px 0!important}
#home .topline .brandlogo{visibility:hidden}
.banner+.stick{margin-top:18px}
"""
R("</style>",css+"</style>")
R('<div class="exhibit" id="exhibit" aria-label="יצירות נבחרות"></div>','''<div class="banner" role="banner"><img class="glow" id="bnGlow" alt="" aria-hidden="true"><div class="in"><span class="eb">USA Tour · Price Guide</span><h1>Albert Levi</h1><span class="rule" aria-hidden="true"></span><span class="tag">A Splash of Art</span></div></div>
    <div class="exhibit" id="exhibit" hidden></div>''')
R("function renderHome(){if(!renderHome.ex){renderHome.ex=1;setTimeout(renderExhibit,0)}","function renderHome(){if(!renderHome.ex){renderHome.ex=1;const g=$('bnGlow'),a=ART.find(x=>x.id==='tree-of-life-blue-life')||ART[0];if(g&&a)g.src=img(a)}")
open('tpl14.html','w').write(t);print('ok')

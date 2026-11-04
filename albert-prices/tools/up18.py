t=open('tpl17.html').read()
def R(a,b,n=1):
    global t
    c=t.count(a);assert c>=1,('MISSING',a[:120]);t=t.replace(a,b,n if n else c)
# --- no automatic discount: nothing is taken off until someone taps a discount ---
R("let theme='all',cur=null,kind='print',sel=null,disc='auto',custom={w:'',h:''};","let theme='all',cur=null,kind='print',sel=null,disc=0,custom={w:'',h:''};")
R("disc='auto';custom={w:'',h:''};","disc=0;custom={w:'',h:''};")
R("ftab=d.tab;kind=ftab==='orig'?'orig':'print';disc='auto';","ftab=d.tab;kind=ftab==='orig'?'orig':'print';disc=0;")
R("let pkgRule='coll',pkgManual=10;","let pkgRule='none',pkgManual=10;")
R("const opts=(S.coll&&!it.orig?['auto']:[]).concat([0,10,15,20]);","const opts=[0].concat(S.coll&&!it.orig?['auto']:[],[10,15,20]);")
R("const dl=disc==='auto'?(p.pct?`אוטומטי −${p.pct}%`:'בלי'):disc?`−${disc}%`:'בלי';","const dl=disc==='auto'?`−${p.pct}%`:disc?`−${disc}%`:'';")
R("""${p.coll?'Collector\\'s ':'הנחה: '}${dl}<svg""","""${p.coll?'Collector\\'s ':p.pct?'הנחה ':'הוספת הנחה'}${dl}<svg""")
R("""aria-pressed="${disc===d||(d===0&&disc==='auto'&&!opts.includes('auto'))}">${d==='auto'?'אוטומטי':d?d+'%':'בלי'}</button>""","""aria-pressed="${disc===d}">${d==='auto'?`Collector's ${collPct(it.list)}%`:d?d+'%':'בלי'}</button>""")
R("""<p class="rates">Collector's Rate אוטומטי: 10% · 15% מעל $300 · 20% מעל $500. משנים בכפתור ההנחה למטה.</p>""","""<p class="rates">אין הנחה עד שבוחרים. Collector's Rate בכפתור ההנחה למטה: 10%, ‏15% מעל $300, ‏20% מעל $500.</p>""")
# --- Albert's own logo: on the banner wall and drawn on the opening screen ---
R('<h1>Albert Levi</h1>','<h1><img class="logo" src="logo-wide.webp" alt="Albert Levi · A splash of art" width="620" height="154"></h1>')
R("""s.innerHTML='<div><div class="lg"><span class="A">A</span><b>Albert Levi</b></div><small>USA TOUR · PRICE GUIDE</small></div>';""","""s.innerHTML='<div class="sp"><img class="mk" src="logo-mark.webp" alt="Albert Levi"><b>Albert Levi</b><small>USA Tour</small></div>';""")
R("setTimeout(()=>{s.style.opacity='0';setTimeout(()=>s.remove(),450)},1700)})();","setTimeout(()=>{s.style.opacity='0';setTimeout(()=>s.remove(),600)},2700)})();")
# --- the customer view arrives like a curtain rising; a picked price answers the touch ---
R("function showCust(o){CV=o;$('cust').innerHTML='';renderCust();$('cust').hidden=false;","function showCust(o){CV=o;$('cust').innerHTML='';renderCust();$('cust').hidden=false;$('cust').classList.remove('enter');void $('cust').offsetWidth;$('cust').classList.add('enter');")
css=r"""
/* ===================== v8: tour-ready ===================== */
/* Albert's brush mark draws itself on launch; his logo signs the gallery wall; prices answer the touch. */
#splash{background:#fff!important;color:#1a1814!important}
#splash .sp{display:grid;justify-items:center;gap:14px}
#splash .mk{width:min(62vw,300px);height:auto;clip-path:inset(0 100% 0 0);animation:brush 1.15s .15s cubic-bezier(.6,.05,.25,1) forwards}
#splash b{font-family:var(--serif)!important;font-weight:300!important;letter-spacing:.32em!important;font-size:1.25rem!important;opacity:0!important;animation:spfade .7s 1.15s ease forwards!important;padding-left:.32em}
#splash small{font-family:var(--body)!important;font-size:.72rem!important;letter-spacing:.3em!important;text-transform:uppercase;color:#857f76!important;opacity:0!important;margin:0!important;animation:spfade .7s 1.35s ease forwards!important}
@keyframes brush{to{clip-path:inset(0 0 0 0)}}
@keyframes spfade{to{opacity:1}}
.banner h1{margin:0 auto!important;line-height:0!important;padding:0!important}
.banner h1 .logo{display:block;width:min(64vw,270px);height:auto;margin:0 auto}
.banner .tag{display:none!important}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .banner h1 .logo{filter:invert(1) hue-rotate(180deg) brightness(1.15)}}
:root[data-theme="dark"] .banner h1 .logo{filter:invert(1) hue-rotate(180deg) brightness(1.15)}
.pm .pmh{position:sticky;top:0;z-index:2;background:var(--wall);box-shadow:0 1px 0 var(--line)}
.pmr button[aria-pressed="true"]{animation:pick .38s cubic-bezier(.2,.8,.2,1)}
@keyframes pick{0%{transform:scale(.92)}60%{transform:scale(1.03)}100%{transform:none}}
.cust.enter{animation:curtain .55s cubic-bezier(.2,.8,.2,1)}
.cust.enter .vr-info>*{animation:rise .6s cubic-bezier(.2,.8,.2,1) both}
.cust.enter .vr-info>*:nth-child(2){animation-delay:.06s}.cust.enter .vr-info>*:nth-child(3){animation-delay:.12s}.cust.enter .vr-info>*:nth-child(4){animation-delay:.18s}
@keyframes curtain{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}
@keyframes rise{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
.dtog{color:var(--acc)!important}
@media (prefers-reduced-motion:reduce){#splash .mk{animation:none;clip-path:none}.pmr button[aria-pressed="true"],.cust.enter,.cust.enter .vr-info>*{animation:none}}
"""
R("</style>",css+"</style>")
open('tpl18.html','w').write(t);print('ok')

t=open('tpl22.html').read()
def R(a,b,n=1):
    global t
    c=t.count(a);assert c>=1,('MISSING',a[:120]);t=t.replace(a,b,n)
# Black Friday: the more you shop, the more you save — tiers on the whole order, in Canadian dollars
R("const collPct=list=>","const BF=[[850,25],[570,20],[210,15]];const bfPct=tot=>{const c=CUR==='CAD'?tot:tot*(+S.fx||1.4235);for(const [m,p] of BF)if(c>m)return p;return 0};\nconst collPct=list=>")
R("const pct=disc==='show'?showPct(it):","const pct=disc==='bf'?bfPct(it.list):disc==='show'?showPct(it):")
R("show:disc==='show'&&pct>0,","show:disc==='show'&&pct>0,bf:disc==='bf',")
R("const opts=[0].concat(showPct(it)?['show']:[],","const opts=[0].concat(['bf'],showPct(it)?['show']:[],")
R("const dl=disc==='auto'||disc==='show'?","const dl=disc==='bf'&&!p.pct?`(מעל ${$f(CUR==='CAD'?210:210/S.fx)})`:disc==='auto'||disc==='show'||disc==='bf'?")
R("""${p.show?'מבצע כנס ':p.coll?""","""${p.bf?'בלאק פריידי ':p.show?'מבצע כנס ':p.coll?""")
R("""${d==='show'?`מבצע כנס −${showPct(it)}%`:""","""${d==='bf'?(bfPct(it.list)?`בלאק פריידי −${bfPct(it.list)}%`:`בלאק פריידי (מעל ${$f(CUR==='CAD'?210:210/S.fx)})`):d==='show'?`מבצע כנס −${showPct(it)}%`:""")
R("""<dt>${p.show?'מבצע כנס':""","""<dt>${p.bf?'בלאק פריידי':p.show?'מבצע כנס':""")
R("disc=b.dataset.disc==='auto'||b.dataset.disc==='show'?b.dataset.disc:","disc=['auto','show','bf'].includes(b.dataset.disc)?b.dataset.disc:")
R("${p.show?`<span class=\"cpill\">SHOW SPECIAL","${p.bf&&p.pct?`<span class=\"cpill\">BLACK FRIDAY · ${p.pct}% OFF</span>`:p.show?`<span class=\"cpill\">SHOW SPECIAL")
# package
R("[['none','בלי'],['show','מבצע כנס'],","[['none','בלי'],['bf','בלאק פריידי'],['show','מבצע כנס'],")
R("else if(rule==='show'){","else if(rule==='bf'){const pc=bfPct(list);items.forEach(x=>x.fin=rnd(x.list*(1-pc/100)));label=`בלאק פריידי −${pc}%`}\n  else if(rule==='show'){")
R("pkgRule==='show'?'קנייה בכנס:","pkgRule==='bf'?`בלאק פריידי על כל ההזמנה: ‏15% מעל ${$f(CUR==='CAD'?210:210/S.fx)}, ‏20% מעל ${$f(CUR==='CAD'?570:570/S.fx)}, ‏25% מעל ${$f(CUR==='CAD'?850:850/S.fx)}.`:pkgRule==='show'?'קנייה בכנס:")
# close deal
R("[[0,'בלי הנחה'],['show','מבצע כנס'],","[[0,'בלי הנחה'],['bf','בלאק פריידי'],['show','מבצע כנס'],")
R("function setCloseDisc(d){CL.disc=d;CL.items=CL.items.map((x,i)=>Object.assign({},x,{fin:d==='show'?",
  "function setCloseDisc(d){CL.disc=d;const bp=bfPct(CL.items.reduce((s,x)=>s+x.list,0));CL.items=CL.items.map((x,i)=>Object.assign({},x,{fin:d==='bf'?rnd(x.list*(1-bp/100)):d==='show'?")
R("setCloseDisc(v==='show'?'show':+v)","setCloseDisc(v==='show'||v==='bf'?v:+v)")
open('tpl23.html','w').write(t);print('ok')

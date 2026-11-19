t=open('tpl20.html').read()
def R(a,b,n=1):
    global t
    c=t.count(a);assert c>=1,('MISSING',a[:120]);t=t.replace(a,b,n)
# Show special: bought at the show -> 20% off originals, 10% off Embellished; prices stay full until it is tapped
R("const collPct=list=>","const isEmb=x=>x.f==='emb'||/Embellished/.test(x.spec||'');const showPct=x=>x.orig?20:isEmb(x)?10:0;\nconst collPct=list=>")
R("spec:`${FMT[sel.f].en} · ${sel.w}″×${sel.h}″ (custom) · ${FR[sel.fr].en}`,list:usd(ils),ils}","spec:`${FMT[sel.f].en} · ${sel.w}″×${sel.h}″ (custom) · ${FR[sel.fr].en}`,list:usd(ils),ils,f:sel.f}")
R("spec:`${FMT[sel.f].en} · ${sz(sel.s,'in')} (${sz(sel.s,'cm')}) · ${FR[sel.fr].en}`,list:usd(c.ils),ils:c.ils}}","spec:`${FMT[sel.f].en} · ${sz(sel.s,'in')} (${sz(sel.s,'cm')}) · ${FR[sel.fr].en}`,list:usd(c.ils),ils:c.ils,f:sel.f}}")
R("function single(it){const auto=disc==='auto';const pct=it.orig?(auto?0:disc):(auto?collPct(it.list):disc);",
  "function single(it){const auto=disc==='auto';const pct=disc==='show'?showPct(it):it.orig?(auto?0:disc):(auto?collPct(it.list):disc);")
R("return {pct,coll:auto&&pct>0,","return {pct,coll:auto&&pct>0,show:disc==='show'&&pct>0,")
R("const opts=[0].concat(S.coll&&!it.orig?['auto']:[],[10,15,20]);","const opts=[0].concat(showPct(it)?['show']:[],S.coll&&!it.orig?['auto']:[],[10,15,20]);")
R("const dl=disc==='auto'?`−${p.pct}%`:","const dl=disc==='auto'||disc==='show'?`−${p.pct}%`:")
R("""${p.coll?'Collector\\'s ':p.pct?'הנחה ':'הוספת הנחה'}${dl}""","""${p.show?'מבצע כנס ':p.coll?'Collector\\'s ':p.pct?'הנחה ':'הוספת הנחה'}${dl}""")
R("""${d==='auto'?`Collector's ${collPct(it.list)}%`:d?d+'%':'בלי'}</button>""","""${d==='show'?`מבצע כנס −${showPct(it)}%`:d==='auto'?`Collector's ${collPct(it.list)}%`:d?d+'%':'בלי'}</button>""")
R("""${p.pct?`<dt>${p.coll?'Collector\\'s Rate':'הנחה'} ${p.pct}%</dt>""","""${p.pct?`<dt>${p.show?'מבצע כנס':p.coll?'Collector\\'s Rate':'הנחה'} ${p.pct}%</dt>""")
# customer view: the show special named in English for the buyer
R("${p.coll?`<span class=\"cpill\">THE COLLECTOR'S RATE · ${p.pct}% OFF</span>`:''}","${p.show?`<span class=\"cpill\">SHOW SPECIAL · ${p.pct}% OFF</span>`:p.coll?`<span class=\"cpill\">THE COLLECTOR'S RATE · ${p.pct}% OFF</span>`:''}")
# package
R("""[['none','בלי'],['p10','10%'],['p20','20%'],""","""[['none','בלי'],['show','מבצע כנס'],['p10','10%'],['p20','20%'],""")
R("else if(rule==='manual'||rule==='p10'","else if(rule==='show'){items.forEach(x=>x.fin=rnd(x.list*(1-showPct(x)/100)));label='מבצע כנס'}\n  else if(rule==='manual'||rule==='p10'")
R("""pkgRule==='coll'?'המדרגה נקבעת לפי סכום ההדפסים בחבילה. על מקורים אין הנחה.':''""","""pkgRule==='coll'?'המדרגה נקבעת לפי סכום ההדפסים בחבילה. על מקורים אין הנחה.':pkgRule==='show'?'קנייה בכנס: 20% על מקורים, 10% על Embellished. הדפסי קנבס ומיני פרינט במחיר מלא.':''""")
# close deal
R("""${[[0,'בלי הנחה'],[10,'10%'],[20,'20%']].map(""","""${[[0,'בלי הנחה'],['show','מבצע כנס'],[10,'10%'],[20,'20%']].map(""")
R("fin:d?rnd(x.list*(1-d/100)):x.list}","fin:d==='show'?rnd(x.list*(1-showPct(x)/100)):d?rnd(x.list*(1-d/100)):x.list}")
R("if(b.dataset.cdisc!==undefined){setCloseDisc(+b.dataset.cdisc);return}","if(b.dataset.cdisc!==undefined){const v=b.dataset.cdisc;setCloseDisc(v==='show'?'show':+v);return}")
R("disc=b.dataset.disc==='auto'?'auto':+b.dataset.disc","disc=b.dataset.disc==='auto'||b.dataset.disc==='show'?b.dataset.disc:+b.dataset.disc")
open('tpl21.html','w').write(t);print('ok')

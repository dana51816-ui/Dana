t=open('tpl19.html').read()
def R(a,b,n=1):
    global t
    c=t.count(a);assert c>=1,('MISSING',a[:120]);t=t.replace(a,b,n)
# Package: one-tap 10% and 20%
R("""[['coll',"Collector's Rate"],['second',`יצירה נוספת −${S.second}%`],['manual','ידני'],['none','בלי']]""","""[['none','בלי'],['p10','10%'],['p20','20%'],['coll',"Collector's Rate"],['second',`יצירה נוספת −${S.second}%`],['manual','אחר']]""")
R("else if(rule==='manual'){items.forEach(x=>x.fin=rnd(x.list*(1-pkgManual/100)));label=`הנחה של ${pkgManual}%`}",
  "else if(rule==='manual'||rule==='p10'||rule==='p20'){const pc=rule==='p10'?10:rule==='p20'?20:pkgManual;items.forEach(x=>x.fin=rnd(x.list*(1-pc/100)));label=`הנחה של ${pc}%`}")
# Closing the deal: the discount can still be set here, from the full price
R("function openClose(items,fromPkg){CL={items,fromPkg,pay:'אשראי',cust:'',note:''};","function openClose(items,fromPkg){CL={items,fromPkg,pay:'אשראי',cust:'',note:'',base:items.map(x=>x.fin),disc:null};")
R("""    <div class="bigtotal">${$f(tot)}</div></div>""","""    <div class="bigtotal">${$f(tot)}</div>
    <h3>הנחה</h3><div class="seg cdisc">${[[0,'בלי הנחה'],[10,'10%'],[20,'20%']].map(([d,l])=>`<button type="button" data-cdisc="${d}" aria-pressed="${CL.disc===d||(CL.disc===null&&d===0&&CL.items.every(x=>x.fin===x.list))}">${l}</button>`).join('')}</div>
    ${CL.disc===null&&CL.items.some(x=>x.fin!==x.list)?`<p class="note">כבר כוללת הנחה של ${$f(CL.items.reduce((s,x)=>s+x.list-x.fin,0))} שנבחרה קודם.</p>`:''}</div>""")
R("function renderClose(){","""function setCloseDisc(d){CL.disc=d;CL.items=CL.items.map((x,i)=>Object.assign({},x,{fin:d?rnd(x.list*(1-d/100)):x.list}));renderClose()}
function renderClose(){""")
# sync: original prices travel only between devices on the same price list
R("const json=JSON.stringify({v:1,S:shared,ORIG,OS,tour,SALES});","const json=JSON.stringify({v:1,S:shared,ORIG,OS,OSV,tour,SALES});")
R("if(o.ORIG)Object.entries(o.ORIG)","if(o.ORIG&&o.OSV===OSV)Object.entries(o.ORIG)")
R("if(o.OS)OS=o.OS;","if(o.OS&&o.OSV===OSV)OS=o.OS;")
R("$('close').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;","$('close').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;if(b.dataset.cdisc!==undefined){setCloseDisc(+b.dataset.cdisc);return}")
open('tpl20.html','w').write(t);print('ok')

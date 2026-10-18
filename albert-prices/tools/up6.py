import re
t=open('tpl5.html').read()
def R(a,b,n=1):
    global t
    assert a in t,('MISSING',a[:90]); t=t.replace(a,b,n)
def RX(p,b):
    global t
    m=re.search(p,t,re.S); assert m,('NOREGEX',p[:60]); t=t[:m.start()]+b+t[m.end():]
# ---- softer palette ----
RX(r":root\{\n  --wall:#f3f5fb;.*?--shadow:0 1px 2px rgba\(20,30,80,\.06\),0 10px 26px -14px rgba\(20,30,80,\.22\);\n\}",
""":root{
  --wall:#f6f7fa; --card:#ffffff; --ink:#2a3048; --muted:#6c7390; --line:#e6e9f0; --soft:#eef1f6;
  --navy:#3d5a99; --navy-deep:#2e4677; --gold:#e9bd6b; --on-gold:#2e3a5e;
  --cobalt:#5b7bd5; --magenta:#d86b96; --sun:#ebc06a; --teal:#4aa8a0; --tang:#e38b5e;
  --accent:var(--navy); --sel-bg:#3d5a99; --sel-fg:#ffffff;
  --warn:#b0652a; --warn-bg:#fdf3e7; --ok:#3d8a62; --sold:#b5485f;
  --display:"Archivo","Rubik",system-ui,sans-serif;
  --script:"Mrs Saint Delafield",cursive; --thin:"Josefin Sans","Rubik",sans-serif;
  --body:"Rubik",system-ui,-apple-system,"Segoe UI",sans-serif;
  --shadow:0 1px 2px rgba(40,50,90,.05),0 8px 22px -14px rgba(40,50,90,.18);
}""")
t=re.sub(r"  --wall:#0c1233; --card:#151d47; --ink:#eef1fb; --muted:#9aa3c8; --line:#26306a; --soft:#1c2557;\n  --navy:#1d3a8f; --navy-deep:#0a0f2c; --gold:#f5bd52; --on-gold:#14215e;\n  --accent:#9fb3ff; --sel-bg:#f5bd52; --sel-fg:#14215e; --warn:#ffb46b; --warn-bg:#2f2213; --ok:#6fd6a2; --sold:#ff8aa0;",
"""  --wall:#161b2b; --card:#1e2438; --ink:#e9ecf4; --muted:#a2a9c2; --line:#2e3550; --soft:#252c44;
  --navy:#4a67a8; --navy-deep:#2b3b66; --gold:#e3bd78; --on-gold:#26304d;
  --accent:#a9bbef; --sel-bg:#e3bd78; --sel-fg:#26304d; --warn:#f0b07a; --warn-bg:#33281c; --ok:#86cfa8; --sold:#f2a0b0;""",t)
assert t.count('--wall:#161b2b')==2
t=t.replace("font-stretch:118%;font-weight:900","font-stretch:112%;font-weight:800")
R(".promo{background:var(--navy);",".promo{background:var(--navy-deep);")
R(".cust.vrmode{display:block;padding:0;background:#090b12;",".cust.vrmode{display:block;padding:0;background:#151926;")
R(".vr{min-height:100%;display:grid;grid-template-rows:auto auto 1fr;color:#f4f2ee;",".vr{min-height:100%;display:grid;grid-template-rows:auto auto 1fr;color:#eef0f5;")
t=t.replace("radial-gradient(120% 80% at 100% 0%,#2a4bb0 0,transparent 60%),linear-gradient(180deg,#1d3a8f,#0a0f2c)","radial-gradient(120% 80% at 100% 0%,#4a67a8 0,transparent 60%),linear-gradient(180deg,#3d5a99,#1f2a47)")
# ---- native USD + inches ----
R('<button class="pill" id="setBtn" type="button" aria-label="הגדרות"><span class="dot"></span><bdi dir="ltr">$1 = ₪<span id="rateTxt">3.70</span></bdi><span aria-hidden="true">⚙︎</span></button>',
  '<button class="pill" id="setBtn" type="button" aria-label="הגדרות"><span aria-hidden="true">⚙︎</span> הגדרות</button>')
R("const inch=cm=>Math.round(cm/2.54);","const inch=cm=>Math.round(cm/2.54);const toCm=i=>Math.round(i*2.54);")
R("function sz(s,u){const [a,b]=dims(s);return u==='cm'?`${a}×${b} cm`:`${inch(a)}″×${inch(b)}″`}","function sz(s,u){const [a,b]=dims(s);return u==='cm'?`${toCm(a)}×${toCm(b)} cm`:`${a}″×${b}″`}")
R("function rnd(v){if(S.round==='5')return Math.round(v/5)*5;if(S.round==='10')return Math.round(v/10)*10;if(S.round==='9')return Math.max(9,Math.round(v/10)*10-1);return Math.round(v)}\nconst usd=ils=>rnd(ils/S.rate);",
  "// prices come from the store in US dollars; discounts round to the whole dollar\nconst rnd=v=>Math.round(v);\nconst usd=v=>Math.round(v);")
R("renderPromo();$('rateTxt').textContent=S.rate.toFixed(2);$('setBtn').classList.toggle('ok',!!S.verified);","renderPromo();")
R("const k=S.unit==='cm'?1:2.54;\n    let res=''","const k=S.unit==='cm'?1/2.54:1;\n    let res=''")
R("const k=S.unit==='cm'?1:2.54;sel={custom:true,f,fr,w:Math.round(parseFloat(custom.w)*k),h:Math.round(parseFloat(custom.h)*k)}","const k=S.unit==='cm'?1/2.54:1;sel={custom:true,f,fr,w:Math.round(parseFloat(custom.w)*k*10)/10,h:Math.round(parseFloat(custom.h)*k*10)/10}")
R("spec:`${FMT[sel.f].en} · ${inch(sel.w)}″×${inch(sel.h)}″ (custom) · ${FR[sel.fr].en}`","spec:`${FMT[sel.f].en} · ${sel.w}″×${sel.h}″ (custom) · ${FR[sel.fr].en}`")
R("<small>${esc(it.spec)}${it.ils?' · ₪'+Math.round(it.ils).toLocaleString('en-US'):''}</small>","<small>${esc(it.spec)}</small>")
# scene: inches in, cm for drawing, exact inch label
R("function drawMini(){const cv=$('mini');if(!cv||!sel)return;const [w,h]=sel.custom?[sel.w,sel.h]:dims(sel.s);drawScene(cv,{a:cur,w,h,fr:sel.fr,env:'gallery',eve:false,dims:true,t:1})}",
  "function selIn(){return sel.custom?[sel.w,sel.h]:dims(sel.s)}\nfunction inLabel(a,b){return `${a}″ × ${b}″  ·  ${toCm(a)} × ${toCm(b)} cm`}\nfunction drawMini(){const cv=$('mini');if(!cv||!sel)return;const [w,h]=selIn();drawScene(cv,{a:cur,w:w*2.54,h:h*2.54,lbl:inLabel(w,h),fr:sel.fr,env:'gallery',eve:false,dims:true,t:1})}")
R("const lbl=`${inch(o.w)}″ × ${inch(o.h)}″  ·  ${Math.round(o.w)} × ${Math.round(o.h)} cm`;","const lbl=o.lbl||`${inch(o.w)}″ × ${inch(o.h)}″  ·  ${Math.round(o.w)} × ${Math.round(o.h)} cm`;")
R("function vrTarget(){if(kind==='orig'){const m=(origInfo(cur).dim||'').match(/(\\d+(?:\\.\\d+)?)\\s*[x×X*]\\s*(\\d+(?:\\.\\d+)?)/);return m?[+m[1],+m[2]]:[100,120]}return sel.custom?[sel.w,sel.h]:dims(sel",
  "function vrIn(){if(kind==='orig'){const m=(origInfo(cur).dim||'').match(/(\\d+(?:\\.\\d+)?)\\s*[x×X*]\\s*(\\d+(?:\\.\\d+)?)/);return m?[+m[1],+m[2]]:[40,48]}return selIn()}\nfunction vrTarget(){return vrIn().map(v=>v*2.54);return sel.custom?[sel.w,sel.h]:dims(sel")
R("const cv=$('vrc');if(cv)drawScene(cv,{a:cur,w:VR.w,h:VR.h,","const cv=$('vrc');const [li,hi]=vrIn();if(cv)drawScene(cv,{a:cur,w:VR.w,h:VR.h,lbl:inLabel(li,hi),")
R("""<div><h4>מחיר המקור${o.dim?` · <bdi dir="ltr">${esc(o.dim)} cm</bdi>`:''}</h4>""","""<div><h4>מחיר המקור${o.dim?` · <bdi dir="ltr">${esc(o.dim)}″</bdi>`:''}</h4>""")
R("out.push(`${FMT[f].en} · ${k.replace('x','×')} cm · ${FR[fr].en} · ₪${o.p} — ${o.w}`)","out.push(`${FMT[f].en} · ${k.replace('x','″×')}″ · ${FR[fr].en} · $${o.p} — ${o.w}`)")
# settings: drop exchange-rate panel and rounding row
RX(r'  <div class="panel"><h3>שער הדולר</h3>.*?data-act="calib">חישוב השער</button></div></div>\n',"")
R("""<div class="panel"><h3>תצוגה</h3><div class="seg">${[['5','עיגול ל־5$'],['10','ל־10$'],['9','מסתיים ב־9'],['none','לדולר']].map(([k,v])=>`<button type="button" data-round="${k}" aria-pressed="${S.round===k}">${v}</button>`).join('')}</div>""","""<div class="panel"><h3>תצוגה</h3><p class="note">המחירים והמידות נלקחים כמו שהם מהאתר: בדולרים ובאינצ׳ים.</p>""")
R("function readInputs(){const r=parseFloat(($('sRate')||{}).value);if(r>1&&r<10&&r!==S.rate){S.rate=r;S.verified=false}","function readInputs(){")
R("הקוד כולל את השער, ההנחות,","הקוד כולל את ההנחות,")
R("הדפס על קנבס. המחיר זהה לכל היצירות לפי גודל וגימור","המחיר זהה לכל היצירות לפי גודל וגימור, כמו באתר")
open('tpl6.html','w').write(t)
# originals form: inches
o=open('tplO.html').read()
o=o.replace('<label for="dim">מידה מדויקת (ס״מ)</label><input id="dim" value="${esc(o.dim||\'\')}" placeholder="100x120">','<label for="dim">מידה מדויקת (אינץ׳)</label><input id="dim" value="${esc(o.dim||\'\')}" placeholder="40x48">')
o=o.replace("['S','קטן','עד 60 ס״מ'],['M','בינוני','60–100 ס״מ'],['L','גדול','100–150 ס״מ'],['XL','ענק','מעל 150 ס״מ']","['S','קטן','עד 24″'],['M','בינוני','24″–40″'],['L','גדול','40″–60″'],['XL','ענק','מעל 60″']")
o=o.replace("--navy:#1d3a8f; --deep:#14215e; --gold:#f2b33d;","--navy:#3d5a99; --deep:#2e4677; --gold:#e9bd6b;").replace("--wall:#f3f5fb; --card:#ffffff; --ink:#121a3d; --muted:#5f6789; --line:#dfe4f2; --soft:#e9edf8;","--wall:#f6f7fa; --card:#ffffff; --ink:#2a3048; --muted:#6c7390; --line:#e6e9f0; --soft:#eef1f6;")
o=o.replace("--wall:#0c1233;--card:#151d47;--ink:#eef1fb;--muted:#9aa3c8;--line:#26306a;--soft:#1c2557;","--wall:#161b2b;--card:#1e2438;--ink:#e9ecf4;--muted:#a2a9c2;--line:#2e3550;--soft:#252c44;")
assert 'אינץ׳)' in o and '24″–40″' in o
open('tplO.html','w').write(o)
print('ok')

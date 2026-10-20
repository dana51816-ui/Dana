t=open('tplO.html').read()
def R(a,b):
    global t
    assert a in t,('MISSING',a[:100]); t=t.replace(a,b,1)
R(".toggle{display:flex;",""".shapes{display:flex;gap:8px;flex-wrap:wrap}
.shapes button{border:1.5px solid var(--line);background:var(--card);border-radius:14px;padding:8px 12px;display:flex;align-items:center;gap:8px}
.shapes button[aria-pressed="true"]{background:var(--navy);border-color:var(--navy);color:#fff}
.shapes i{display:block;border:2px solid currentColor;border-radius:3px}
.ghead{display:flex;align-items:center;gap:8px;font-weight:700;margin-top:4px}
.ghead i{display:block;border:2px solid var(--navy);border-radius:3px}
.toggle{display:flex;""")
R("let st={OS:[{w:24,h:30,p:null},{w:30,h:40,p:null},{w:36,h:48,p:null},{w:40,h:60,p:null},{w:48,h:60,p:null},{w:60,h:80,p:null}],O:{},i:0,view:'intro'};",
"""// sizes belong to a shape; each painting only gets the sizes of its own shape
const SH=[['sq','מרובע','1:1',14,14],['rect','מלבן','3:4 · 2:3',12,16],['pano','פנורמי','1:2',9,18]];
const bucket=(w,h)=>{const r=Math.max(w,h)/Math.min(w,h);return r<1.15?'sq':r<1.75?'rect':'pano'};
const shIcon=(g,k)=>{const s=SH.find(x=>x[0]===g);return `<i style="width:${s[3]*(k||1)}px;height:${s[4]*(k||1)}px"></i>`};
let st={OS:[{g:'sq',w:24,h:24,p:null},{g:'sq',w:36,h:36,p:null},{g:'sq',w:48,h:48,p:null},
  {g:'rect',w:24,h:30,p:null},{g:'rect',w:30,h:40,p:null},{g:'rect',w:36,h:48,p:null},{g:'rect',w:40,h:60,p:null},{g:'rect',w:48,h:72,p:null},
  {g:'pano',w:20,h:40,p:null},{g:'pano',w:30,h:60,p:null},{g:'pano',w:36,h:72,p:null}],O:{},i:0,view:'intro'};""")
R("try{const s=JSON.parse(localStorage.getItem(KEY));if(s)st=Object.assign(st,s)}catch(e){}",
  "try{const s=JSON.parse(localStorage.getItem(KEY));if(s){st=Object.assign(st,s);st.OS.forEach(r=>{if(!r.g)r.g=r.w&&r.h?bucket(r.w,r.h):'rect'})}}catch(e){}")
R("function info(a){const o=st.O[a.id]||{};const rows=sizes().map(r=>{",
  "function shapeOf(a){return (st.O[a.id]||{}).sh||a.sh||'rect'}\nfunction info(a){const o=st.O[a.id]||{},g=shapeOf(a);const rows=sizes().filter(r=>r.g===g).map(r=>{")
R("return {o,rows,nfs:!!o.nfs,done:!!o.seen,priced:live.length}}","return {o,g,rows,nfs:!!o.nfs,done:!!o.seen,priced:live.length}}")
# intro text
R("<p class=\"note\">רשימה אחת שחלה על כל המקורים. אפשר להוסיף ולמחוק גדלים.</p>","<p class=\"note\">לפי צורה: מרובע, מלבן ופנורמי. כל ציור יקבל רק את הגדלים של הצורה שלו.</p>")
# sizes view grouped by shape
import re
m=re.search(r"    <div class=\"card\" style=\"gap:8px\"><div class=\"shead\">.*?<button class=\"btn\" type=\"button\" data-add>\+ עוד גודל</button></div>\n",t,re.S); assert m
t=t[:m.start()]+"""    ${SH.map(([g,l,rt])=>`<div class="card" style="gap:8px"><div class="ghead">${shIcon(g)}${l} <span class="note">${rt}</span></div><div class="shead"><span>רוחב</span><span></span><span>גובה</span><span>מחיר</span><span></span></div>
    ${st.OS.map((r,i)=>r.g!==g?'':`<div class="srow"><input inputmode="decimal" data-w="${i}" value="${r.w||''}" aria-label="רוחב"><span class="x">×</span><input inputmode="decimal" data-h="${i}" value="${r.h||''}" aria-label="גובה"><div class="money"><input inputmode="numeric" data-p="${i}" value="${r.p||''}" aria-label="מחיר"></div><button class="del" type="button" data-del="${i}" aria-label="מחיקה">✕</button></div>`).join('')}
    <button class="btn" type="button" data-add="${g}">+ גודל ${l}</button></div>`).join('')}
"""+t[m.end():]
R("<p class=\"lead\">רוחב × גובה באינצ׳ים, ומחיר בדולרים. זה המחיר הרגיל לכל המקורים.</p>","<p class=\"lead\">רוחב × גובה באינצ׳ים, ומחיר בדולרים, לכל צורה. ציור יקבל רק את הגדלים של הצורה שלו.</p>")
R("if(d.add!==undefined){st.OS.push({w:null,h:null,p:null});save();return render()}","if(d.add!==undefined){st.OS.push({g:d.add||'rect',w:null,h:null,p:null});save();return render()}")
# item view: shape chips
R("""    <label class="toggle"><span>להציע את הציור הזה כמקור</span>""","""    <div class="q"><h3>צורת הציור</h3><div class="shapes">${SH.map(([g,l])=>`<button type="button" data-sh="${g}" aria-pressed="${x.g===g}">${shIcon(g,.9)}${l}</button>`).join('')}</div></div>
    <label class="toggle"><span>להציע את הציור הזה כמקור</span>""")
R("<p class=\"note\" style=\"padding:12px\">עוד לא הוגדרו גדלים. חוזרים שלב אחד אחורה.</p>","<p class=\"note\" style=\"padding:12px\">אין גדלים לצורה הזאת. מוסיפים אותם בשלב \"מחיר לכל גודל\".</p>")
R("  if(d.jump!==undefined){st.i=+d.jump;return go('item')}","  if(d.jump!==undefined){st.i=+d.jump;return go('item')}\n  if(d.sh){const a=ART[st.i];setO(o=>{if(d.sh===a.sh)delete o.sh;else o.sh=d.sh});return render()}")
# code: include group + shape override
R("const OS=sizes().filter(r=>r.p).map(r=>({s:key(r),p:r.p}));","const OS=sizes().filter(r=>r.p).map(r=>({s:key(r),p:r.p,g:r.g}));")
R("if(o.nfs)r.nfs=true;","if(o.nfs)r.nfs=true;if(o.sh)r.sh=o.sh;")
R("const custom=rows.filter(r=>r.x.rows.some(y=>y.ov||y.off)).length","const custom=rows.filter(r=>r.x.rows.some(y=>y.ov||y.off)||r.x.o.sh).length")
R("rows.filter(r=>r.x.nfs||r.x.rows.some(y=>y.ov||y.off))","rows.filter(r=>r.x.nfs||r.x.o.sh||r.x.rows.some(y=>y.ov||y.off))")
R("${r.x.nfs?'לא מוצע':","${r.x.nfs?'לא מוצע':r.x.o.sh?'צורה: '+SH.find(s=>s[0]===r.x.o.sh)[1]+(r.x.rows.some(y=>y.ov)?' · ':'')+r.x.rows.filter(y=>y.ov).map(y=>`${y.r.w}×${y.r.h}: ${$f(y.ov)}`).join(' · '):")
R("<div class=\"card\" style=\"gap:6px\">${sizes().map(r=>`<div style=\"display:flex;justify-content:space-between\"><span style=\"direction:ltr;font-family:var(--display);font-weight:700\">${r.w}″ × ${r.h}″</span>",
  "<div class=\"card\" style=\"gap:6px\">${sizes().map(r=>`<div style=\"display:flex;justify-content:space-between\"><span style=\"direction:ltr;font-family:var(--display);font-weight:700\">${r.w}″ × ${r.h}″ <small class=\"note\">${SH.find(s=>s[0]===r.g)[1]}</small></span>")
open('tplO.html','w').write(t)

a=open('tpl7.html').read()
o="function origSizes(a){const o=ORIG[a.id]||{};if(o.nfs)return [];return OS.filter(r=>!(o.off||[]).includes(r.s))"
assert o in a
a=a.replace(o,"const bucketOf=s=>{const [w,h]=dims(s),r=Math.max(w,h)/Math.min(w,h);return r<1.15?'sq':r<1.75?'rect':'pano'};\nfunction origSizes(a){const o=ORIG[a.id]||{};if(o.nfs)return [];const g=o.sh||a.sh||'rect';return OS.filter(r=>(r.g||bucketOf(r.s))===g&&!(o.off||[]).includes(r.s))")
open('tpl8.html','w').write(a)
m=open('mk.py').read()
m=m.replace("orig=[{'id':__import__('re').sub(r'[^a-z0-9]+','-',a['k']),'n':a['n'],'os':a.get('os')} for a in arts if a['o']]","orig=[{'id':__import__('re').sub(r'[^a-z0-9]+','-',a['k']),'n':a['n'],'os':a.get('os'),'sh':a.get('sh')} for a in arts if a['o']]")
assert "'sh':a.get('sh')" in m
open('mk.py','w').write(m)
print('ok')

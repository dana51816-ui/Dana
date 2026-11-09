t=open('tpl18.html').read()
def R(a,b,n=1):
    global t
    c=t.count(a);assert c>=1,('MISSING',a[:120]);t=t.replace(a,b,n)
# Mini prints: one general category, three proportions, one price; not every work exists as a mini
R("const THEMES=[['all','הכול','var(--ink)'],","const THEMES=[['all','הכול','var(--ink)'],['mini','מיני פרינט','var(--acc)'],")
R("""  $('grid').innerHTML=items.length?items.map(tileHTML).join(''):`<div class="empty">לא מצאנו יצירה כזאת.<br>נסו חלק מהשם, למשל "tree" או "hamsa".</div>`;""",
"""  $('grid').innerHTML=items.length?items.map(tileHTML).join(''):`<div class="empty">לא מצאנו יצירה כזאת.<br>נסו חלק מהשם, למשל "tree" או "hamsa".</div>`;
  if(theme==='mini'&&!q){$('count').textContent='';$('grid').innerHTML=miniHTML()}""")
R("function renderHome(){","""const MINI={p:120,sizes:['12x9','12x11','11x11']};
function miniHTML(){return `<section class="mini"><p class="note">הדפס קטן במחיר אחד לכל המידות. לא כל היצירות קיימות כמיני פרינט, אז בודקים מה יש לפני שמציעים.</p>
  <div class="minirows">${MINI.sizes.map(s=>`<div class="minirow"><span class="s">${sz(s,'in')}<small>${sz(s,'cm')}</small></span><b class="p">${$f(MINI.p)}</b><button type="button" class="line" data-mini="${s}">+ חבילה</button></div>`).join('')}</div></section>`}
function renderHome(){""")
R("$('qa').addEventListener('click',","""$('grid').addEventListener('click',e=>{const b=e.target.closest('[data-mini]');if(!b)return;const s=b.dataset.mini;
  pkg.push({id:'mini',n:'Mini Print',spec:`Mini print · ${sz(s,'in')} (${sz(s,'cm')})`,list:MINI.p,ils:MINI.p});persist();renderFab();toast('מיני פרינט נוסף לחבילה · '+pkg.length+' פריטים')});
$('qa').addEventListener('click',""")
css=r"""
/* ===================== v9: mini prints ===================== */
.mini{grid-column:1/-1;display:grid;gap:14px}
.mini .note{margin:0}
.minirows{border-top:1.5px solid var(--ink)}
.minirow{display:grid;grid-template-columns:1fr auto auto;align-items:center;gap:16px;padding:14px 0;border-bottom:1px solid var(--line)}
.minirow .s{font-family:var(--serif);font-size:1.25rem;direction:ltr;text-align:right;display:flex;flex-direction:column;align-items:flex-start}
.minirow .s small{font-family:var(--body);font-size:.72rem;color:var(--muted);margin-top:3px}
.minirow .p{font-family:var(--serif);font-weight:400;font-size:1.3rem;font-variant-numeric:tabular-nums}
.minirow .line{border:1px solid var(--line);background:var(--card);padding:10px 14px;min-height:44px;font-size:.88rem;color:var(--ink)}
.minirow .line:active{transform:scale(.97)}
"""
R("</style>",css+"</style>")
open('tpl19.html','w').write(t);print('ok')

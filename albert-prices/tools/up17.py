t=open('tpl16.html').read()
def R(a,b,n=1):
    global t
    c=t.count(a);assert c>=1,('MISSING',a[:120]);t=t.replace(a,b,n if n else c)
I=lambda d,cls='ico':f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{d}</svg>'
X=I('<path d="M6 6l12 12M18 6L6 18"/>');CK=I('<path d="M5 12.5l4.5 4.5L19 7.5"/>');CH=I('<path d="M6 9l6 6 6-6"/>','ico ch')
SUN=I('<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/>')
MOON=I('<path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/>')
RUL=I('<path d="M3 12h18M3 12l3-3M3 12l3 3M21 12l-3-3M21 12l-3 3"/>')
STAR=I('<path d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9 6.8 19.6l1-5.8L3.5 9.7l5.9-.9z"/>','ico st')
# icons: one drawn family instead of text glyphs
R('hidden>✕</button>',f'hidden>{X}</button>')
R('data-rm="${i}" aria-label="הסרה">✕</button>',f'data-rm="${{i}}" aria-label="הסרה">{X}</button>')
R('data-cx="x" aria-label="סגירה">✕</button>',f'data-cx="x" aria-label="סגירה">{X}</button>')
R('data-osdel="${i}" aria-label="מחיקה">✕</button>',f'data-osdel="${{i}}" aria-label="מחיקה">{X}</button>')
R('data-act="pdeal">✓ סגירת עסקה',f'data-act="pdeal">{CK}סגירת עסקה')
R('data-cx="deal">✓ סגירת עסקה',f'data-cx="deal">{CK}סגירת עסקה')
R('data-cx="pdeal">✓ סגירת עסקה',f'data-cx="pdeal">{CK}סגירת עסקה')
R('data-act="save">✓ אישור, נמכר',f'data-act="save">{CK}אישור, נמכר')
R("${dl} ${discOpen?'▴':'▾'}</button>",f"${{dl}}{CH}</button>")
R("$('vrEve').textContent=VR.eve?'☾ Evening':'☀ Day';",f"$('vrEve').innerHTML=VR.eve?'{MOON}Evening':'{SUN}Day';")
R('data-vr="dims" id="vrDims">↔</button>',f'data-vr="dims" id="vrDims" aria-label="Dimensions">{RUL}</button>')
R('<div class="vr-hint">⇠ החליקו להחלפת גודל ⇢</div>','<div class="vr-hint">החליקו להחלפת גודל</div>')
R("<span class=\"star\">★</span>",f"<span class=\"star\" aria-label=\"בטור\">{STAR}</span>")
R("'<em>★ המקור בטור</em>'",f"'<em>{STAR}המקור בטור</em>'")
R("<summary><span>★ בטור · הסיפור של היצירה</span>",f"<summary><span>{STAR}הסיפור של היצירה</span>")
R("<small>${tp?'★ בטור':s}</small>",f"<small>${{tp?'{STAR}בטור':s}}</small>")
R("${r.tour?'★ ':''}",f"${{r.tour?'{STAR}':''}}")
R("ולוחצים ☆ כדי","ולוחצים על הכוכב כדי")
# no kicker above headings
R("""<p class="eyebrow">Albert Levi · ${a.o?'Original & Editions':'Editions'}</p>""","")
R("""<div><div class="vr-ed">${kind==='orig'?'ORIGINAL PAINTING · HAND-PAINTED TO ORDER':esc(FMT[sel.f].en.toUpperCase())}</div><h2 class="vr-title">${esc(a.n)}</h2></div>""",
  """<div><h2 class="vr-title">${esc(a.n)}</h2><p class="vr-sub">${kind==='orig'?(oRow()&&oRow().tour?'One of a kind original · Signed, with Certificate of Authenticity':'Original painting · Hand-painted to order'):esc(FMT[sel.f].en)}</p></div>""")
R('<span class="vr-tag">VIEWING ROOM</span>','<span class="vr-tag"></span>')
# the customer also sees the work in real homes
R("""data-cx="add">+ לחבילה</button></div>`}`;""","""data-cx="add">+ לחבילה</button></div>`}${views(a).length?`<div class="vr-photos" aria-label="In a home">${views(a).map(v=>`<img src="${v}" alt="${esc(a.n)} in a home" loading="lazy">`).join('')}</div>`:''}`;""")
# detector: drop the empty banner image and the dead blue glow
R('<img class="glow" id="bnGlow" alt="" aria-hidden="true">','')
R("background:radial-gradient(120% 80% at 100% 0%,#4a67a8 0,transparent 60%),linear-gradient(180deg,#3d5a99,#1f2a47);","background:var(--wall);")
css=r"""
/* ===================== v7: polish ===================== */
/* Browser surfaces carry the palette; Hebrew labels are never letter-spaced; one drawn icon family; bordeaux is the single action colour. */
::selection{background:color-mix(in srgb,var(--acc) 22%,transparent);color:var(--ink)}
:focus-visible{outline:2px solid var(--acc);outline-offset:2px}
input,textarea{caret-color:var(--acc)}
.pval,.vr-price,.sum .tot b,.sum dd,.pmr button,.tile .tp,.kpi b,.totals,.bigtotal,.qa small,td{font-variant-numeric:tabular-nums lining-nums}
.sec span,th,.kpi small,.panel h3,.sum .h,.wallbox p,.pmh{letter-spacing:normal!important;text-transform:none}
th,.kpi small,.panel h3,.sum .h{font-size:.75rem!important;font-weight:600}
.banner .tag{font-size:.72rem!important}
.ico.ch{width:14px;height:14px;transition:transform .25s}
[aria-expanded="true"]>.ico.ch{transform:rotate(180deg)}
.ico.st{width:12px;height:12px;fill:currentColor;stroke:none;vertical-align:-1px;margin-inline-end:4px}
.tile .star .ico.st{width:13px;height:13px;margin:0}
.pmr.tourrow .s em,.kind button small{display:inline-flex!important;align-items:center}
.story summary span{display:inline-flex;align-items:center}
button .ico{vertical-align:-3px}
.gold .ico,.green .ico{width:17px;height:17px;margin-inline-end:6px}
.clear .ico,.glassbtn .ico{width:18px;height:18px}
#vrEve .ico{width:16px;height:16px;margin-inline-end:6px}
/* settings: quiet remove buttons */
[data-osdel]{border:0!important;background:transparent!important;color:var(--muted)!important;width:40px;height:40px;padding:0!important;display:grid;place-items:center}
[data-osdel]:hover,[data-osdel]:focus-visible{color:var(--acc)!important}
[data-rm]{border:0!important;background:transparent!important;color:var(--muted)}
/* one action colour */
.green,.cbtns .gold{background:var(--acc)!important;color:var(--on-acc)!important;border-color:var(--acc)!important}
/* viewing room */
.vr-title{font-weight:400!important;letter-spacing:0!important;line-height:1.05!important}
.vr-sub{margin:6px 0 0;font-size:.85rem;color:var(--muted);direction:ltr;text-align:left}
.vr-tag{display:none}
.vr-sizes{-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 16px,#000 calc(100% - 28px),transparent);mask-image:linear-gradient(90deg,transparent 0,#000 16px,#000 calc(100% - 28px),transparent)}
.vr-photos{display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;margin-inline:-16px;padding:4px 16px 2px}
.vr-photos::-webkit-scrollbar{display:none}
.vr-photos img{flex:none;width:78%;aspect-ratio:1;object-fit:cover;scroll-snap-align:center;display:block}
.vr-hint{letter-spacing:normal}
"""
R("</style>",css+"</style>")
R('box-shadow:0 8px 16px -14px rgba(40,50,90,.35)}','box-shadow:0 8px 16px -14px rgba(26,24,20,.3)}')
t=t.replace('rgba(40,50,90,','rgba(26,24,20,').replace('rgba(40,60,120,','rgba(26,24,20,')
open('tpl17.html','w').write(t);print('ok')

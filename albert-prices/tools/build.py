import json,sys,re,collections
d=json.load(open(sys.argv[1])); ps=d['products']
SKIP_TYPES={'Accessories','Phone Case','Bags','Paper products','Home Decor','Puzzle'}
SKIP=re.compile(r'(?i)demo product|^test$|add frame|gift card|custom piece|copy of abstract')
ALIAS={'tree of happines pink magic':'tree of happiness pink magic','powerfull stride':'powerful stride',
 'wild majestiy':'wild majesty','wing of freedom':'wings of freedom','am yisral chai tree of life':'am yisrael chai tree of life',
 'noble peacock':'a noble peacock','am israel chai tree of life':'am yisrael chai tree of life',
 'exact geometry precise colorful refined design':'exact geometry','funky frog in square shades':'funky frog',
 'tree of happiness earthy elegance':'tree of happiness earth',
 'bloom of happiness':'the bloom of happiness','blue life':'tree of life blue life','colorful dream':'tree of life colorful dream',
 'colorful life':'tree of life colorful life','everlastig love':'everlasting love','gentle purple':'tree of life gentle purple',
 'glow in the dark dance':'glow in the dark dance celebrate freedom in glow','map of israel':'map of israel never again',
 'smile forever after nova':'after nova smile forever','together we win':'together we will win'}
def base(t):
  t=re.sub(r'(?i)original (artwork|painting)\s*-?','',t)
  t=re.sub(r'(?i)embellished edition print\s*-?','',t)
  t=re.sub(r'(?i)-\s*framed canvas','',t)
  k=re.sub(r'[^a-z0-9]+',' ',t.lower()).strip()
  return ALIAS.get(k,k), t.strip(' -')
def nice(n):
  n=re.sub(r'\s+',' ',n).strip(' -–')
  small={'of','the','in','and','to','a','with','we','my','our'}
  w=n.split(' ')
  return ' '.join(x if (x.lower() in small and i>0) else (x[:1].upper()+x[1:].lower() if x.isupper() or x.islower() else x) for i,x in enumerate(w))
FMT={'canvas prints':'canvas','canvas art':'canvas','embellished':'emb','hand enhanced':'emb','floating framed canvas':'float','framed canvas':'float'}
FR={'stretch canvas':'stretch','stretch frame':'stretch','black frame':'black','white frame':'white','rolled canvas':'rolled',
    'black':'black','white':'white','espresso':'espresso','natural':'natural'}
def parse_size(s):
  m=re.search(r'(\d+(?:\.\d+)?)\s*[″"\'’]*\s*[x×X]\s*(\d+(?:\.\d+)?)\s*(CM|cm|″|"|\'\')?',s)
  if not m: return None
  a,b=float(m.group(1)),float(m.group(2)); unit=m.group(3) or ''
  if unit.lower()!='cm' and ('″' in s or '"' in s): a,b=round(a*2.54),round(b*2.54)
  return (int(round(a)),int(round(b)))
groups=collections.OrderedDict()
for p in ps:
  if p['product_type'] in SKIP_TYPES or SKIP.search(p['title']): continue
  key,disp=base(p['title'])
  g=groups.setdefault(key,{'name':None,'handles':[],'formats':{},'original':None,'tags':set()})
  tg=' '.join(p['tags']).lower()
  if 'animal' in tg: g['tags'].add('an')
  if 'יהודים' in tg or 'jew' in tg or 'chai' in tg: g['tags'].add('jw')
  isorig=bool(re.search(r'(?i)original (artwork|painting)',p['title']))
  if isorig:
    g['original']={'handle':p['handle'],'site':p['variants'][0]['available']}
    if not g['name']: g['name']=nice(disp)
    continue
  isemb=bool(re.search(r'(?i)embellished edition',p['title']))
  if not isemb and not re.search(r'(?i)framed canvas',p['title']): g['name']=nice(disp)
  elif not g['name']: g['name']=nice(disp)
  g['handles'].append(p['handle'])
  names=[o['name'].strip().lower() for o in p['options']]
  for v in p['variants']:
    vals=[v.get('option1'),v.get('option2'),v.get('option3')]
    fmt=None;size=None;frame=None
    for n,val in zip(names,vals):
      if val is None: continue
      lv=val.strip().lower()
      if 'product' in n: fmt=FMT.get(lv)
      elif 'size' in n:
        size=parse_size(val)
        if 'rolled' in lv: frame='rolled'
      elif 'frame' in n or 'color' in n: frame=FR.get(lv)
    if fmt is None:
      if isemb: fmt='emb'
      elif 'color' in names: fmt='float'
      else: fmt='canvas'
    if frame is None: frame='rolled' if fmt=='emb' else 'stretch'
    if not size: continue
    price=float(v['price'])
    if price<=0: continue
    sz='%dx%d'%size
    fm=g['formats'].setdefault(fmt,{})
    ent=fm.setdefault(sz,{})
    # keep first seen (avoid duplicate products overriding)
    if frame not in ent: ent[frame]={'p':price,'a':v['available']}
# flags
std=collections.defaultdict(collections.Counter)
for g in groups.values():
  for f,sz in g['formats'].items():
    for s,fr in sz.items():
      k=tuple(sorted(map(int,s.split('x'))))
      for frm,o in fr.items(): std[(f,k,frm)][o['p']]+=1
out=[];flags=[]
for key,g in groups.items():
  if not g['formats'] and not g['original']: continue
  for f,sz in g['formats'].items():
    items=sorted(sz.items(),key=lambda kv: eval(kv[0].replace('x','*')))
    for frm in {fr for _,e in items for fr in e}:
      seq=[(s,e[frm]) for s,e in items if frm in e]
      for i,(s,o) in enumerate(seq):
        area=eval(s.replace('x','*'))
        smaller=[x for t,x in seq[:i] if eval(t.replace('x','*'))<area]
        reason=None
        if smaller and o['p']<max(x['p'] for x in smaller): reason='מחיר נמוך ממידה קטנה יותר'
        elif frm in('black','white') and 'stretch' in sz[s] and o['p']<sz[s]['stretch']['p']: reason='מסגרת זולה מקנבס ללא מסגרת'
        elif o['p']<250 and area>2000: reason='מחיר נמוך באופן חריג'
        if reason:
          o['w']=reason; flags.append((g['name'],f,s,frm,o['p'],reason))
  out.append({'k':key,'n':g['name'],'h':(g['handles'] or [None])[0],'f':g['formats'],'o':g['original'],'img':(g['handles'] or [None])[0] or (g['original'] or {}).get('handle'),'t':sorted(g['tags'])})
out.sort(key=lambda x:x['n'].lower())
json.dump(out,open(sys.argv[2],'w'),ensure_ascii=False,separators=(',',':'))
print(len(out),'artworks; with original',sum(1 for x in out if x['o']),'; flags',len(flags))
for f in flags: print(f)
print(collections.Counter(f for x in out for f in x['f']))

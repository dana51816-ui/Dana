import json,sys,collections
arts=json.load(open(sys.argv[1]))
def key(s):
  a,b=map(float,s.split('x')); return '%gx%g'%(min(a,b),max(a,b))
area=lambda k: eval(k.replace('x','*'))
cnt=collections.defaultdict(collections.Counter)
for a in arts:
  for f in ('canvas','emb'):
    for s,frs in a['f'].get(f,{}).items():
      for fr,o in frs.items(): cnt[(f,key(s),fr)][o['p']]+=1
std={}
for (f,k,fr),c in cnt.items():
  p,n=c.most_common(1)[0]
  std.setdefault(f,{}).setdefault(k,{})[fr]={'p':p,'n':sum(c.values())}
# flags on std
for f in list(std):
  std[f]={k:{fr:o for fr,o in v.items() if o['n']>=2} for k,v in std[f].items()}
  std[f]={k:v for k,v in std[f].items() if v}
for f,tab in std.items():
  ks=sorted(tab,key=area)
  frames={fr for k in ks for fr in tab[k]}
  for fr in frames:
    sq=lambda k: k.split('x')[0]==k.split('x')[1]
    seq=[(k,tab[k][fr]) for k in ks if fr in tab[k] and tab[k][fr]['n']>=3]
    for i,(k,o) in enumerate(seq):
      sm=[x['p'] for kk,x in seq[:i] if area(kk)<area(k) and sq(kk)==sq(k)]
      if sm and o['p']<max(sm): o['w']='זול יותר ממידה קטנה יותר'
  for k in ks:
    st=tab[k].get('stretch')
    for fr in ('black','white'):
      if st and fr in tab[k] and tab[k][fr]['p']<st['p']: tab[k][fr]['w']='מסגרת זולה מקנבס בלי מסגרת'
out=[]
for a in arts:
  f={}
  for fmt,sz in a['f'].items():
    if fmt in ('canvas','emb'):
      d={}
      for s,frs in sz.items():
        for fr,o in frs.items():
          if fr in std[fmt].get(key(s),{}): d.setdefault(s,{})[fr]=0
          elif fmt=='canvas' and not o.get('w'): d.setdefault(s,{})[fr]=o['p']
      if d: f[fmt]=d
    else:
      f[fmt]={s:{fr:o['p'] for fr,o in frs.items() if not o.get('w')} for s,frs in sz.items()}
      f[fmt]={s:v for s,v in f[fmt].items() if v}
      if not f[fmt]: del f[fmt]
  out.append({'img':a.get('img'),'k':a['k'],'n':a['n'],'h':a['h'],'f':f,'o':bool(a['o']),'os':(a['o'] or {}).get('site'),'t':a.get('t',[])})
json.dump({'std':std,'art':out},open(sys.argv[2],'w'),ensure_ascii=False,separators=(',',':'))
for f,tab in std.items():
  print('==',f)
  for k in sorted(tab,key=area): print(' ',k,{fr:(o['p'],o['n'],o.get('w','')) for fr,o in tab[k].items()})

"""Tag each artwork with its shape: sq (1:1), rect (~3:4 / 2:3), pano (~1:2) — from its store print sizes, else its image."""
import json,sys,re,collections
from PIL import Image
d=json.load(open(sys.argv[1]));thumbs=sys.argv[2]
def bucket(r): return 'sq' if r<1.15 else ('rect' if r<1.75 else 'pano')
for a in d['art']:
  c=collections.Counter()
  for f,sz in a['f'].items():
    for s in sz:
      w,h=map(float,s.split('x'));c[bucket(max(w,h)/min(w,h))]+=1
  if c: a['sh']=c.most_common(1)[0][0];a['shs']='prints'
  else:
    im=Image.open(f"{thumbs}/{re.sub(r'[^a-z0-9]+','-',a['k'])}.webp");w,h=im.size
    a['sh']=bucket(max(w,h)/min(w,h));a['shs']='image'
  a['land']=None
json.dump(d,open(sys.argv[1],'w'),ensure_ascii=False,separators=(',',':'))
o=[a for a in d['art'] if a['o']]
print('originals by shape',collections.Counter((a['sh'],a['shs']) for a in o))
print('image-based:',[(a['n'],a['sh']) for a in o if a['shs']=='image'])
print('pano:',[a['n'] for a in o if a['sh']=='pano'])

import json,sys,re,os
from PIL import Image,ImageChops
d=json.load(open(sys.argv[1]));src=sys.argv[2];dst=sys.argv[3];os.makedirs(dst,exist_ok=True)
for f in os.listdir(dst): os.remove(os.path.join(dst,f))
tot=0
for a in d['art']:
  im=Image.open(f"{src}/{a['img']}.jpg").convert('RGB')
  bg=Image.new('RGB',im.size,(255,255,255));diff=ImageChops.difference(im,bg).convert('L').point(lambda v:255 if v>18 else 0)
  bb=diff.getbbox()
  if bb: im=im.crop(bb)
  im.thumbnail((360,360),Image.LANCZOS)
  slug=re.sub(r'[^a-z0-9]+','-',a['k']).strip('-')
  out=f"{dst}/{slug}.webp";im.save(out,'WEBP',quality=72,method=6);tot+=os.path.getsize(out)
  a['im']=[im.size[0],im.size[1]]
json.dump(d,open(sys.argv[1],'w'),ensure_ascii=False,separators=(',',':'))
print(len(d['art']),'thumbs',tot//1024,'KB')

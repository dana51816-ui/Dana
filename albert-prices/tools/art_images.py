"""From the raw product images, make per-work: the painting itself (frame/margins cropped), a small grid copy, and up to 2 extra views (rooms, close-ups)."""
import os,re,json,sys
from PIL import Image,ImageChops,ImageStat
RAW='tools/raw';OUT=sys.argv[1] if len(sys.argv)>1 else '.'
for d in ('art','art-sm','views'): os.makedirs(f'{OUT}/{d}',exist_ok=True)
def trim_white(im):
    bg=Image.new('RGB',im.size,(255,255,255));diff=ImageChops.difference(im,bg).convert('L').point(lambda v:255 if v>22 else 0)
    bb=diff.getbbox();return im.crop(bb) if bb else im
def dark(im,box):return ImageStat.Stat(im.crop(box).convert('L')).mean[0]
def trim_frame(im,asp=None):
    g=im.convert('L');w,h=im.size;lim=int(min(w,h)*.2)
    col=lambda x:ImageStat.Stat(g.crop((x,int(h*.25),x+1,int(h*.6)))).mean[0]
    row=lambda y:ImageStat.Stat(g.crop((int(w*.25),y,int(w*.75),y+1))).mean[0]
    def scan(get,rng):
        n=None
        for k,i in enumerate(rng):
            v=get(i)
            if v<100:n=k
            elif n is not None and k-n>2:break
        return None if n is None else n+1
    L=scan(col,range(lim));R=scan(lambda i:col(w-1-i),range(lim));T=scan(row,range(lim))
    if None in (L,R,T) or min(L,R,T)<3:return im,False
    th=max(L,R,T)
    if asp:
        # we know the painting's proportions from its print sizes: the bottom edge follows from the width
        H0=round((w-L-R)/asp)
        if T+H0<=h:
            p=int(min(w,h)*.006);return im.crop((L+p,T+p,w-R-p,T+H0-p)),True
    # bottom edge: walk down from the middle and stop at the first dark band as thick as the side frame
    B=None;y=int(h*.45);run=0
    while y<h:
        if row(y)<100:
            run+=1
            if run>=max(3,int(th*.6)):B=y-run+1;break
        else:run=0
        y+=1
    if B is None:return im,False
    p=int(min(w,h)*.006)
    return im.crop((L+p,T+p,w-R-p,B-p)),True
def save(im,path,mx,q):
    im=im.copy();im.thumbnail((mx,mx),Image.LANCZOS);im.save(path,'WEBP',quality=q,method=6)
arts=json.load(open('tools/art-handles.json'));rep=[]
# hand-picked fixes where the automatic crop cannot find the painting (room-only photos, unusual frames)
NOASP={'calm-sunset','family-stride','flowers-in-the-hair','natural-tree-of-life'}
MANUAL={'above-and-within':(0,(.30,.04,.70,.80)),'infinite-power':(1,(.18,.15,.82,.53)),'magic-in-nature':(4,(.277,.142,.582,.582)),
        'rooted-in-the-heavens':(3,(.198,.104,.553,.773)),'dynamic-monochrome-ride':(2,(.205,.195,.78,.595)),'israel-hamsa':(0,(.063,.071,.934,.474)),
        'luminous-tree':(3,(.133,.078,.588,.812)),'deer-in-the-forest':(0,(.06,.205,.94,.785)),'star-of-hope':(2,None),'calm-sunset':(1,(.05,.04,.955,.635))}
_d=json.load(open(sys.argv[2])) if len(sys.argv)>2 else {'art':[]}
ASP={}
for x in _d['art']:
    for f in ('canvas','emb','float'):
        if x['f'].get(f):
            s=next(iter(x['f'][f]));a_,b_=map(float,s.split('x'));ASP[re.sub(r'[^a-z0-9]+','-',x['k'])]=a_/b_;break
for a in arts:
    d=f"{RAW}/{a['id']}";files=sorted([f for f in os.listdir(d) if f.endswith('.jpg')],key=lambda f:int(f.split('.')[0])) if os.path.isdir(d) else []
    ims=[]
    for f in files:
        try: ims.append((f,Image.open(f'{d}/{f}').convert('RGB')))
        except Exception: pass
    if not ims: rep.append((a['id'],'none'));continue
    if a['id'] in MANUAL:
        k,box=MANUAL[a['id']];f,im=next((x for x in ims if x[0]==f'{k}.jpg'),ims[0])
        if box: W,H=im.size;im=im.crop((int(box[0]*W),int(box[1]*H),int(box[2]*W),int(box[3]*H)))
        else: im=trim_white(im)
        save(im,f"{OUT}/art/{a['id']}.webp",800,76);save(im,f"{OUT}/art-sm/{a['id']}.webp",420,72)
        views=[v for g,v in ims if g!=f][:2]
        for i,v in enumerate(views): save(v,f"{OUT}/views/{a['id']}-{i}.webp",760,64)
        rep.append((a['id'],f,len(views),im.size,True));continue
    # the painting: first image that is a framed mock-up on white (crop it), else the first image as is
    art=None;ok_any=False
    for f,im in ims[:3]:
        t=trim_white(im);c,ok=trim_frame(t,None if a['id'] in NOASP else ASP.get(a['id']))
        if ok: art=(f,c);ok_any=True;break
    if not art: art=(ims[0][0],trim_white(ims[0][1]))
    save(art[1],f"{OUT}/art/{a['id']}.webp",800,76);save(art[1],f"{OUT}/art-sm/{a['id']}.webp",420,72)
    views=[im for f,im in ims if f!=art[0]][:2]
    for i,v in enumerate(views): save(v,f"{OUT}/views/{a['id']}-{i}.webp",760,64)
    rep.append((a['id'],art[0],len(views),art[1].size,ok_any))
json.dump({r[0]:(r[2] if len(r)>2 else 0) for r in rep},open('tools/views.json','w'))
print(len(rep),'works');print([r for r in rep if len(r)<3])

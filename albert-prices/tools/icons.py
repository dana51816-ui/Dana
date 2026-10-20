# Branded home-screen icon: "AL" monogram in Frank Ruhl Libre on ink, a bronze hairline frame, and a soft glow of Albert's blue tree behind it.
import sys
from PIL import Image,ImageDraw,ImageFilter,ImageFont,ImageChops
font,art,out=sys.argv[1:4]
S=1024
bg=Image.new('RGB',(S,S),(20,18,15))
p=Image.open(art).convert('RGB').resize((S,S))
from PIL import ImageEnhance
glow=ImageEnhance.Brightness(ImageEnhance.Color(p.filter(ImageFilter.GaussianBlur(80))).enhance(1.4)).enhance(.62)
bg=Image.blend(bg,glow,.55)
# radial vignette toward the ink
import math
v=Image.radial_gradient('L').resize((S,S))  # 0 centre -> 255 edge
v=v.point(lambda x:min(255,int(x*1.15)))
bg=Image.composite(Image.new('RGB',(S,S),(14,12,10)),bg,v)
d=ImageDraw.Draw(bg)
br=(201,166,107)
m=int(S*.115);d.rectangle((m,m,S-m,S-m),outline=br,width=5)
f=ImageFont.truetype(font,int(S*.40))
t='AL';b=d.textbbox((0,0),t,font=f)
d.text(((S-(b[2]-b[0]))/2-b[0],(S-(b[3]-b[1]))/2-b[1]-S*.04),t,font=f,fill=(243,239,232))
fs=ImageFont.truetype(font,int(S*.05));t2='A  SPLASH  OF  ART';b2=d.textbbox((0,0),t2,font=fs)
d.text(((S-(b2[2]-b2[0]))/2-b2[0],S*.70),t2,font=fs,fill=br)
for n in (180,192,512):bg.resize((n,n),Image.LANCZOS).save(f'{out}/icon-{n}.png')
bg.resize((512,512),Image.LANCZOS).save(f'{out}/icon-preview.png')

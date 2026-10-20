import re
t=open('tpl4.html').read()
def R(a,b):
    global t
    assert a in t,('MISSING',a[:90]); t=t.replace(a,b,1)
def RX(pat,b):
    global t
    m=re.search(pat,t,re.S); assert m,('NOREGEX',pat[:60]); t=t[:m.start()]+b+t[m.end():]

# ---------- CSS ----------
R("#close{z-index:55}", r"""#close{z-index:55}
/* micro-interactions */
button{transition:transform .12s ease,background-color .2s ease,color .2s ease,border-color .2s ease,box-shadow .2s ease}
button:active:not(:disabled){transform:scale(.965)}
.tile:active .art{transform:scale(.98)}
/* viewing room */
.cust.vrmode{display:block;padding:0;background:#090b12;overflow-y:auto}
.vr{min-height:100%;display:grid;grid-template-rows:auto auto 1fr;color:#f4f2ee;padding-bottom:env(safe-area-inset-bottom,0px)}
.vr-top{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:calc(10px + env(safe-area-inset-top,0px)) 16px 10px;position:relative;z-index:2}
.vr-top .who{display:flex;align-items:center;direction:ltr}
.vr-top .who .A{font-family:var(--script);font-size:2.6rem;line-height:.6;margin-right:-6px}
.vr-top .who b{font-family:var(--thin);font-weight:300;letter-spacing:.32em;font-size:.95rem}
.vr-tag{font-family:var(--display);font-stretch:125%;font-weight:800;font-size:.62rem;letter-spacing:.28em;color:#c9a35a;border:1px solid rgba(201,163,90,.45);border-radius:999px;padding:5px 10px}
.glassbtn{border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.08);-webkit-backdrop-filter:blur(14px) saturate(1.4);backdrop-filter:blur(14px) saturate(1.4);color:#fff;border-radius:999px;min-width:38px;height:38px;padding:0 12px;font-size:.85rem;display:inline-flex;align-items:center;justify-content:center;gap:6px}
.glassbtn[aria-pressed="true"]{background:rgba(255,255,255,.88);color:#111;border-color:#fff}
.vr-stage{position:relative;height:min(60vh,560px);min-height:320px;touch-action:pan-y}
.vr-stage canvas{display:block;width:100%;height:100%}
.vr-ctl{position:absolute;inset-inline:12px;top:12px;display:flex;justify-content:space-between;gap:8px;pointer-events:none}
.vr-ctl>*{pointer-events:auto}
.vr-env{display:flex;gap:2px;padding:3px;border-radius:999px;border:1px solid rgba(255,255,255,.18);background:rgba(20,20,24,.35);-webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);direction:ltr}
.vr-env button{border:0;background:none;color:#fff;border-radius:999px;padding:7px 12px;font-size:.78rem;font-weight:600;letter-spacing:.02em}
.vr-env button[aria-pressed="true"]{background:#fff;color:#111}
.vr-tools{display:flex;gap:6px}
.vr-hint{position:absolute;bottom:14px;left:50%;transform:translateX(-50%);font-size:.74rem;color:#fff;background:rgba(0,0,0,.4);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);padding:6px 12px;border-radius:999px;white-space:nowrap;animation:hint 3.2s ease forwards;pointer-events:none}
@keyframes hint{0%,70%{opacity:1}100%{opacity:0}}
.vr-info{display:grid;grid-template-columns:minmax(0,1fr);gap:14px;padding:18px 16px 26px;max-width:640px;width:100%;margin:0 auto;direction:ltr;text-align:left}
.vr-ed{font-family:var(--display);font-stretch:125%;font-weight:800;font-size:.64rem;letter-spacing:.24em;color:#c9a35a}
.vr-title{font-family:var(--display);font-stretch:118%;font-weight:900;font-size:clamp(2rem,9vw,3.1rem);line-height:.95;letter-spacing:-.02em;margin:2px 0 0}
.vr-sizes{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;margin-inline:-16px;padding-inline:16px}
.vr-sizes::-webkit-scrollbar{display:none}
.vr-sizes button{flex:none;border:1px solid rgba(255,255,255,.16);background:rgba(255,255,255,.04);color:#f4f2ee;border-radius:14px;padding:9px 13px;text-align:left;font-family:var(--display);font-weight:700;font-variant-numeric:tabular-nums;font-size:.92rem}
.vr-sizes button small{display:block;font-family:var(--body);font-weight:400;font-size:.68rem;color:#9a9caa}
.vr-sizes button[aria-pressed="true"]{background:#f4f2ee;color:#0b0d14;border-color:#f4f2ee}
.vr-sizes button[aria-pressed="true"] small{color:#555}
.vr-fin{display:flex;gap:8px;flex-wrap:wrap}
.vr-fin button{border:1px solid rgba(255,255,255,.16);background:rgba(255,255,255,.04);color:#f4f2ee;border-radius:999px;padding:7px 12px 7px 8px;display:inline-flex;align-items:center;gap:8px;font-size:.84rem}
.vr-fin i{width:18px;height:18px;border-radius:5px;display:block}
.vr-fin button[aria-pressed="true"]{border-color:#c9a35a;box-shadow:0 0 0 1px #c9a35a inset}
.vr-card{border-radius:22px;padding:16px;background:linear-gradient(160deg,rgba(255,255,255,.09),rgba(255,255,255,.03));border:1px solid rgba(255,255,255,.12);display:flex;justify-content:space-between;align-items:flex-end;gap:14px}
.vr-card .cpill{display:inline-block;margin-bottom:8px}
.vr-price{font-family:var(--display);font-stretch:118%;font-weight:900;font-size:clamp(3rem,15vw,4.6rem);line-height:.9;font-variant-numeric:tabular-nums;letter-spacing:-.02em}
.vr-price s{display:block;font-size:.28em;color:#9a9caa;font-weight:600;letter-spacing:0;margin-bottom:4px}
.vr-cta{display:grid;grid-template-columns:1fr auto;gap:8px;direction:rtl}
.vr-cta .gold{padding:15px;font-size:1rem;background:linear-gradient(180deg,#f6c55a,#e0a32e);box-shadow:0 10px 24px -10px rgba(242,179,61,.6)}
.vr-cta .line{border-color:rgba(255,255,255,.25)}
.wallbox canvas{display:block;width:100%;height:220px;border-radius:14px}
""")

# ---------- detail mini preview uses canvas ----------
RX(r"function wallSVG\(\)\{.*?\n", """function wallSVG(){if(!sel)return '';return `<div class="wallbox"><canvas id="mini" aria-label="הדמיה בגלריה בקנה מידה"></canvas><p>הדמיה בקנה מידה · ב"הצג ללקוח" אפשר להחליף סביבה ותאורה</p></div>`}
""")
R("$('detail').innerHTML=h+'</div>';renderBar()}","$('detail').innerHTML=h+'</div>';renderBar();drawMini()}\nfunction drawMini(){const cv=$('mini');if(!cv||!sel)return;const [w,h]=sel.custom?[sel.w,sel.h]:dims(sel.s);drawScene(cv,{a:cur,w,h,fr:sel.fr,env:'gallery',eve:false,dims:true,t:1})}")

# ---------- viewing room ----------
RX(r"function renderCust\(\)\{.*?\n\$\('cust'\)\.addEventListener\('click',e=>\{.*?if\(d\.cx==='x'\)back\(\)\}\);\n", r"""/* ---- scene renderer (canvas) ---- */
const SCN={imgs:{},noise:null};
function getImg(a,cb){let im=SCN.imgs[a.id];if(!im){im=new Image();im.decoding='async';im.src=img(a);SCN.imgs[a.id]=im}if(!im.complete&&cb)im.addEventListener('load',cb,{once:true});return im}
function noise(){if(!SCN.noise){const c=document.createElement('canvas');c.width=c.height=180;const x=c.getContext('2d'),d=x.createImageData(180,180);for(let i=0;i<d.data.length;i+=4){const v=120+Math.random()*135;d.data[i]=d.data[i+1]=d.data[i+2]=v;d.data[i+3]=255}x.putImageData(d,0,0);SCN.noise=c}return SCN.noise}
const ENV={gallery:{wall:['#f5f3ef','#e2ded6'],floor:['#d4d0c8','#9e9a92'],kind:'concrete',spot:.55,base:'#faf8f4',ink:'rgba(20,20,22,.78)',furn:'bench'},
  home:{wall:['#ebe2d4','#d3c6b3'],floor:['#b98d61','#6f4b2b'],kind:'wood',spot:.42,base:'#f6f1e8',ink:'rgba(40,30,20,.78)',furn:'sofa'},
  loft:{wall:['#3b3b3f','#202024'],floor:['#47464a','#18181a'],kind:'concrete',spot:1,base:'#2c2c30',ink:'rgba(255,255,255,.85)',furn:'bench'}};
function rr(x,X,y,w,h,r){x.beginPath();x.moveTo(X+r,y);x.arcTo(X+w,y,X+w,y+h,r);x.arcTo(X+w,y+h,X,y+h,r);x.arcTo(X,y+h,X,y,r);x.arcTo(X,y,X+w,y,r);x.closePath()}
function drawScene(cv,o){const dpr=Math.min(2,window.devicePixelRatio||1),W=cv.clientWidth,H=cv.clientHeight;if(!W||!H)return;
  if(cv.width!==Math.round(W*dpr)||cv.height!==Math.round(H*dpr)){cv.width=Math.round(W*dpr);cv.height=Math.round(H*dpr)}
  const x=cv.getContext('2d');x.setTransform(dpr,0,0,dpr,0,0);const E=ENV[o.env],t=o.t??1,eve=o.eve;
  const fy=Math.round(H*.8),furnH=E.furn==='sofa'?82:45;
  const bottomCm=E.furn==='sofa'?furnH+24:Math.max(furnH+28,148-o.h/2),topCm=bottomCm+o.h;
  const k=Math.min(W/Math.max(250,o.w+110),(fy-40)/(topCm+16)),cx=W/2;
  const aw=o.w*k,ah=o.h*k,ax=cx-aw/2,ay=fy-topCm*k;
  // wall
  let g=x.createLinearGradient(0,0,0,fy);g.addColorStop(0,E.wall[0]);g.addColorStop(1,E.wall[1]);x.fillStyle=g;x.fillRect(0,0,W,fy);
  x.save();x.globalAlpha=E.kind==='concrete'&&o.env==='loft'?.09:.05;x.globalCompositeOperation='multiply';x.fillStyle=x.createPattern(noise(),'repeat');x.fillRect(0,0,W,fy);x.restore();
  if(eve){x.fillStyle='rgba(16,12,28,.5)';x.fillRect(0,0,W,H)}
  // light cone + spot
  const warm=eve?'255,214,160':'255,247,232';
  x.save();x.globalCompositeOperation='lighter';const cone=x.createLinearGradient(0,0,0,ay+ah);cone.addColorStop(0,`rgba(${warm},${(eve?.16:.07)*t})`);cone.addColorStop(1,`rgba(${warm},0)`);
  x.fillStyle=cone;x.beginPath();x.moveTo(cx-14,0);x.lineTo(cx+14,0);x.lineTo(cx+aw*.95+30,ay+ah*1.05);x.lineTo(cx-aw*.95-30,ay+ah*1.05);x.closePath();x.fill();x.restore();
  const sr=Math.max(aw,ah)*.95+70;let rg=x.createRadialGradient(cx,ay+ah*.3,4,cx,ay+ah*.5,sr);rg.addColorStop(0,`rgba(${warm},${E.spot*(eve?.95:.6)*t})`);rg.addColorStop(.55,`rgba(${warm},${E.spot*(eve?.35:.18)*t})`);rg.addColorStop(1,`rgba(${warm},0)`);
  x.save();x.globalCompositeOperation=o.env==='loft'||eve?'lighter':'source-over';x.fillStyle=rg;x.fillRect(0,0,W,fy);x.restore();
  // floor
  g=x.createLinearGradient(0,fy,0,H);g.addColorStop(0,E.floor[0]);g.addColorStop(1,E.floor[1]);x.fillStyle=g;x.fillRect(0,fy,W,H-fy);
  if(E.kind==='wood'){x.save();x.beginPath();x.rect(0,fy,W,H-fy);x.clip();x.strokeStyle='rgba(60,35,15,.22)';x.lineWidth=1;const vp=fy-H*1.4;for(let i=-24;i<=24;i++){const xb=cx+i*W/10;x.beginPath();x.moveTo(cx+(xb-cx)*((fy-vp)/(H-vp)),fy);x.lineTo(xb,H);x.stroke()}
    for(let j=0;j<6;j++){const yy=fy+(H-fy)*Math.pow(j/6,1.6);x.strokeStyle='rgba(60,35,15,.08)';x.beginPath();x.moveTo(0,yy);x.lineTo(W,yy);x.stroke()}x.restore()}
  else{x.save();x.globalAlpha=.06;x.globalCompositeOperation='multiply';x.fillStyle=x.createPattern(noise(),'repeat');x.fillRect(0,fy,W,H-fy);x.restore()}
  const fl=x.createRadialGradient(cx,fy+6,4,cx,fy+10,Math.max(aw,160)*.9);fl.addColorStop(0,`rgba(${warm},${(eve?.28:.18)*t})`);fl.addColorStop(1,`rgba(${warm},0)`);x.fillStyle=fl;x.fillRect(0,fy,W,H-fy);
  if(eve){x.fillStyle='rgba(16,12,28,.35)';x.fillRect(0,fy,W,H-fy)}
  // contact shadow + baseboard
  g=x.createLinearGradient(0,fy-14,0,fy+12);g.addColorStop(0,'rgba(0,0,0,0)');g.addColorStop(.55,'rgba(0,0,0,.16)');g.addColorStop(1,'rgba(0,0,0,0)');x.fillStyle=g;x.fillRect(0,fy-14,W,26);
  const bh=Math.max(4,9*k);x.fillStyle=E.base;x.fillRect(0,fy-bh,W,bh);x.fillStyle='rgba(255,255,255,.35)';x.fillRect(0,fy-bh,W,1);
  // reflection of art on concrete
  const im=getImg(o.a,o.onload);
  if(E.kind==='concrete'&&im.complete&&im.naturalWidth){x.save();x.beginPath();x.rect(0,fy,W,H-fy);x.clip();x.globalAlpha=(o.env==='loft'?.14:.08)*t;x.translate(0,fy*2-(ay+ah)+((fy-(ay+ah))*0));x.scale(1,-1);
    x.translate(0,-(fy-(ay+ah))*0);drawImg(x,im,ax,fy-(fy-(ay+ah))-ah-(fy-(ay+ah)),aw,ah);x.restore();
    const fade=x.createLinearGradient(0,fy,0,H);fade.addColorStop(0,'rgba(0,0,0,0)');fade.addColorStop(1,E.floor[1]);x.fillStyle=fade;x.fillRect(0,fy,W,H-fy)}
  // furniture
  if(E.furn==='sofa')drawSofa(x,cx,fy,k,o.a,eve);else drawBench(x,cx+Math.min(W*.18,aw*.25),fy,k,o.env,eve);
  if(E.furn==='sofa')drawLamp(x,Math.min(W-14,cx+aw/2+Math.max(60*k,40)),fy,k,eve,t);
  // artwork
  drawArt(x,im,ax,ay,aw,ah,o.fr,k,o.a,t);
  // dimensions
  if(o.dims){const c=E.ink;x.save();x.strokeStyle=c;x.fillStyle=c;x.lineWidth=1;const y0=ay-(o.fr==='black'||o.fr==='white'?3.2*k:0)-14;
    x.beginPath();x.moveTo(ax,y0);x.lineTo(ax+aw,y0);x.moveTo(ax,y0-4);x.lineTo(ax,y0+4);x.moveTo(ax+aw,y0-4);x.lineTo(ax+aw,y0+4);x.stroke();
    const lbl=`${inch(o.w)}″ × ${inch(o.h)}″  ·  ${Math.round(o.w)} × ${Math.round(o.h)} cm`;x.font='700 11px Archivo, sans-serif';const tw=x.measureText(lbl).width+18;
    x.fillStyle=o.env==='loft'||eve?'rgba(255,255,255,.92)':'rgba(17,19,30,.86)';rr(x,cx-tw/2,y0-10,tw,20,10);x.fill();x.fillStyle=o.env==='loft'||eve?'#111':'#fff';x.textAlign='center';x.textBaseline='middle';x.fillText(lbl,cx,y0+.5);x.restore()}
  // vignette + lights-on fade
  const vg=x.createRadialGradient(cx,H*.45,Math.min(W,H)*.35,cx,H*.45,Math.max(W,H)*.8);vg.addColorStop(0,'rgba(0,0,0,0)');vg.addColorStop(1,`rgba(0,0,0,${o.env==='loft'||eve?.5:.22})`);x.fillStyle=vg;x.fillRect(0,0,W,H);
  if(t<1){x.fillStyle=`rgba(5,6,10,${(1-t)*.92})`;x.fillRect(0,0,W,H)}}
function drawImg(x,im,X,Y,w,h){if(!(im.complete&&im.naturalWidth))return false;const iw=im.naturalWidth,ih=im.naturalHeight,ins=.085;const sw=iw*(1-2*ins),sh=ih*(1-2*ins);const r=w/h,sr=sw/sh;let cw=sw,ch=sh;if(sr>r)cw=sh*r;else ch=sw/r;x.drawImage(im,(iw-cw)/2,(ih-ch)/2,cw,ch,X,Y,w,h);return true}
function drawArt(x,im,ax,ay,aw,ah,fr,k,a,t){const framed=fr==='black'||fr==='white'||fr==='espresso'||fr==='natural',fw=framed?Math.max(3,3.2*k):0,m=fr==='rolled'?Math.max(3,4*k):0;
  const ox=ax-fw-m,oy=ay-fw-m,ow=aw+2*(fw+m),oh=ah+2*(fw+m);
  x.save();x.shadowColor=`rgba(0,0,0,${.42*t})`;x.shadowBlur=Math.max(10,Math.min(ow,oh)*.08);x.shadowOffsetX=Math.max(2,ow*.012);x.shadowOffsetY=Math.max(5,oh*.045);x.fillStyle='#2a2a2a';x.fillRect(ox,oy,ow,oh);x.restore();
  if(fr==='rolled'){x.fillStyle='#f4f1ea';x.fillRect(ox,oy,ow,oh);const wv=x.createLinearGradient(ox,0,ox+ow,0);for(let i=0;i<=6;i++)wv.addColorStop(i/6,i%2?'rgba(0,0,0,.05)':'rgba(255,255,255,.05)');x.fillStyle=wv;x.fillRect(ox,oy,ow,oh)}
  if(framed){const base={black:'#141416',white:'#f3f2ee',espresso:'#3d271c',natural:'#c39a66'}[fr];x.fillStyle=base;x.fillRect(ox,oy,ow,oh);
    const L=fr==='white'?'rgba(255,255,255,.9)':'rgba(255,255,255,.22)',D=fr==='white'?'rgba(0,0,0,.14)':'rgba(0,0,0,.45)';
    const bev=(pts,c)=>{x.fillStyle=c;x.beginPath();x.moveTo(...pts[0]);pts.slice(1).forEach(p=>x.lineTo(...p));x.closePath();x.fill()};
    bev([[ox,oy],[ox+ow,oy],[ax+aw,ay],[ax,ay]],L);bev([[ox,oy],[ax,ay],[ax,ay+ah],[ox,oy+oh]],L.replace(/[\d.]+\)$/,m=>(parseFloat(m)*.6)+')'));
    bev([[ox,oy+oh],[ax,ay+ah],[ax+aw,ay+ah],[ox+ow,oy+oh]],D);bev([[ox+ow,oy],[ox+ow,oy+oh],[ax+aw,ay+ah],[ax+aw,ay]],D.replace(/[\d.]+\)$/,m=>(parseFloat(m)*.7)+')'))}
  if(!drawImg(x,im,ax,ay,aw,ah)){const g=x.createLinearGradient(ax,ay,ax+aw,ay+ah);a.c.forEach((c,i)=>g.addColorStop(i/2,c));x.fillStyle=g;x.fillRect(ax,ay,aw,ah)}
  x.save();x.globalAlpha=.06;x.globalCompositeOperation='overlay';x.fillStyle=x.createPattern(noise(),'repeat');x.fillRect(ax,ay,aw,ah);x.restore();
  if(fr==='stretch'){const d=Math.max(2,3.8*k*.45);const g=x.createLinearGradient(ax+aw,0,ax+aw+d,0);g.addColorStop(0,'rgba(0,0,0,.55)');g.addColorStop(1,'rgba(0,0,0,.25)');
    x.fillStyle=a.c[0];x.beginPath();x.moveTo(ax+aw,ay);x.lineTo(ax+aw+d,ay+d*.6);x.lineTo(ax+aw+d,ay+ah+d*.6);x.lineTo(ax+aw,ay+ah);x.fill();x.fillStyle=g;x.fill();
    x.fillStyle='rgba(0,0,0,.35)';x.beginPath();x.moveTo(ax,ay+ah);x.lineTo(ax+aw,ay+ah);x.lineTo(ax+aw+d,ay+ah+d*.6);x.lineTo(ax+d,ay+ah+d*.6);x.fill();
    x.fillStyle='rgba(255,255,255,.18)';x.fillRect(ax,ay,aw,1)}
  if(framed){x.strokeStyle='rgba(0,0,0,.35)';x.lineWidth=1;x.strokeRect(ax+.5,ay+.5,aw-1,ah-1);
    const sh=x.createLinearGradient(ax,ay,ax+aw,ay+ah);sh.addColorStop(0,'rgba(255,255,255,0)');sh.addColorStop(.42,'rgba(255,255,255,0)');sh.addColorStop(.5,'rgba(255,255,255,.13)');sh.addColorStop(.62,'rgba(255,255,255,0)');x.fillStyle=sh;x.fillRect(ax,ay,aw,ah)}}
function drawSofa(x,cx,fy,k,a,eve){const w=220*k,h=80*k,sx=cx-w/2,seatY=fy-44*k,col=eve?['#8f8577','#6d6458']:['#d6ccbe','#b7ab9a'];
  x.save();x.fillStyle='rgba(0,0,0,.22)';x.beginPath();x.ellipse(cx,fy-1,w*.55,7*k+3,0,0,Math.PI*2);x.fill();x.restore();
  let g=x.createLinearGradient(0,fy-h,0,fy);g.addColorStop(0,col[0]);g.addColorStop(1,col[1]);x.fillStyle=g;
  rr(x,sx+8*k,fy-h,w-16*k,h*.62,10*k);x.fill();rr(x,sx,seatY-6*k,w,34*k,9*k);x.fill();
  x.fillStyle='rgba(255,255,255,.18)';rr(x,sx+10*k,seatY-5*k,w/2-14*k,10*k,5*k);x.fill();rr(x,cx+4*k,seatY-5*k,w/2-14*k,10*k,5*k);x.fill();
  rr(x,sx-4*k,seatY-16*k,18*k,40*k,8*k);x.fillStyle=col[1];x.fill();rr(x,sx+w-14*k,seatY-16*k,18*k,40*k,8*k);x.fill();
  const pc=(c,X)=>{x.save();x.translate(X,seatY-20*k);x.rotate(-.12);x.fillStyle=c;rr(x,-16*k,-16*k,32*k,30*k,7*k);x.fill();x.fillStyle='rgba(255,255,255,.15)';rr(x,-14*k,-14*k,28*k,8*k,4*k);x.fill();x.restore()};
  pc(a.c[1],sx+34*k);pc(a.c[2],sx+w-34*k);x.fillStyle='#3a2a1c';x.fillRect(sx+12*k,fy-10*k,3*k,10*k);x.fillRect(sx+w-15*k,fy-10*k,3*k,10*k)}
function drawBench(x,bx,fy,k,env,eve){const w=150*k,h=45*k,X=bx-w/2;x.save();x.fillStyle='rgba(0,0,0,.2)';x.beginPath();x.ellipse(bx,fy-1,w*.55,5*k+2,0,0,Math.PI*2);x.fill();x.restore();
  const g=x.createLinearGradient(0,fy-h,0,fy-h+6*k);g.addColorStop(0,eve?'#7a5636':'#b4885a');g.addColorStop(1,eve?'#5b3f27':'#8c6640');x.fillStyle=g;rr(x,X,fy-h,w,6*k,2*k);x.fill();
  x.fillStyle=env==='loft'?'#0e0e10':'#1c1c1e';x.fillRect(X+10*k,fy-h+6*k,3*k,h-6*k);x.fillRect(X+w-13*k,fy-h+6*k,3*k,h-6*k)}
function drawLamp(x,lx,fy,k,eve,t){x.save();x.strokeStyle='#1c1c1e';x.lineWidth=Math.max(1.2,1.6*k);x.beginPath();x.moveTo(lx,fy-2);x.lineTo(lx,fy-150*k);x.quadraticCurveTo(lx,fy-200*k,lx-55*k,fy-190*k);x.stroke();
  x.fillStyle='#1c1c1e';x.beginPath();x.ellipse(lx,fy-1,12*k,2.5*k,0,0,Math.PI*2);x.fill();x.beginPath();x.moveTo(lx-70*k,fy-178*k);x.quadraticCurveTo(lx-55*k,fy-198*k,lx-40*k,fy-178*k);x.closePath();x.fill();
  if(eve){const r=x.createRadialGradient(lx-55*k,fy-176*k,2,lx-55*k,fy-150*k,90*k);r.addColorStop(0,`rgba(255,210,150,${.5*t})`);r.addColorStop(1,'rgba(255,210,150,0)');x.globalCompositeOperation='lighter';x.fillStyle=r;x.fillRect(lx-160*k,fy-200*k,220*k,200*k)}x.restore()}

/* ---- viewing room ---- */
const VR={env:'gallery',eve:false,dims:true,t:0,w:100,h:75,raf:0};
function vrTarget(){if(kind==='orig')return [100,120];return sel.custom?[sel.w,sel.h]:dims(sel.s)}
function vrDraw(){const cv=$('vrc');if(cv)drawScene(cv,{a:cur,w:VR.w,h:VR.h,fr:kind==='orig'?'stretch':sel.fr,env:VR.env,eve:VR.eve,dims:VR.dims&&kind!=='orig',t:VR.t,onload:vrDraw})}
function vrAnimate(toW,toH,lights){cancelAnimationFrame(VR.raf);const fw=VR.w,fh=VR.h,ft=VR.t,t0=performance.now(),d=lights?1100:480,red=matchMedia('(prefers-reduced-motion: reduce)').matches;
  (function step(n){const p=red?1:Math.min(1,(n-t0)/d),e=1-Math.pow(1-p,3);VR.w=fw+(toW-fw)*e;VR.h=fh+(toH-fh)*e;if(lights)VR.t=ft+(1-ft)*Math.min(1,p*1.3);vrDraw();if(p<1)VR.raf=requestAnimationFrame(step)})(t0)}
function renderCust(){const o=CV;$('cust').classList.toggle('vrmode',!!o.single);
  if(o.single){const a=cur,it=current(),p=single(it);const flagged=kind!=='orig'&&!sel.custom&&(cell(a,sel.f,sel.s,sel.fr)||{}).w;
    let sizes='',fins='';if(kind!=='orig'&&!sel.custom){const F=a.f[sel.f];const ss=Object.keys(F).sort((x,y)=>area(x)-area(y)).filter(s=>s===sel.s||Object.keys(F[s]).some(z=>{const c=cell(a,sel.f,s,z);return c&&!c.w}));
      sizes=`<div class="vr-sizes" role="group" aria-label="Size">${ss.map(s=>`<button type="button" data-cs="${s}" aria-pressed="${s===sel.s}">${sz(s,'in')}<small>${sz(s,'cm')}</small></button>`).join('')}</div>`;
      const sw={stretch:'linear-gradient(135deg,#ddd,#999)',black:'#141416',white:'#f3f2ee;box-shadow:inset 0 0 0 1px #bbb',rolled:'repeating-linear-gradient(90deg,#f4f1ea 0 3px,#e2ddd2 3px 6px)',espresso:'#3d271c',natural:'#c39a66'};
      fins=`<div class="vr-fin" role="group" aria-label="Finish">${FRO.filter(z=>F[sel.s][z]!==undefined).map(z=>`<button type="button" data-cf="${z}" aria-pressed="${z===sel.fr}"><i style="background:${sw[z]}"></i>${FR[z].en}</button>`).join('')}</div>`}
    const url=a.h?`https://www.albertlevi.com/products/${a.h}`:'',qr=url&&!flagged?qrSVG(url):'';
    const price=flagged?`<div class="vr-price" style="font-size:2rem">Price on request</div>`:`${p.coll?`<span class="cpill">THE COLLECTOR'S RATE · ${p.pct}% OFF</span>`:''}<div class="vr-price">${p.pct?`<s>${$f(it.list)}</s>`:''}<span data-roll="${p.fin}">${$f(renderCust.last??p.fin)}</span></div>`;
    if(!flagged)renderCust.last=p.fin;
    const fresh=!$('vrc');
    if(fresh){$('cust').innerHTML=`<div class="vr"><div class="vr-top"><div class="who"><span class="A">A</span><b>Albert Levi</b></div><span class="vr-tag">VIEWING ROOM</span><button class="glassbtn" type="button" data-cx="x" aria-label="סגירה">✕</button></div>
      <div class="vr-stage" id="vrStage"><canvas id="vrc" aria-label="Artwork shown on a wall at true scale"></canvas>
      <div class="vr-ctl"><div class="vr-env" id="vrEnv"></div><div class="vr-tools"><button class="glassbtn" type="button" data-vr="eve" id="vrEve"></button><button class="glassbtn" type="button" data-vr="dims" id="vrDims">↔</button></div></div>
      ${kind!=='orig'&&!sel.custom?'<div class="vr-hint">⇠ החליקו להחלפת גודל ⇢</div>':''}</div>
      <div class="vr-info" id="vrInfo"></div></div>`;VR.t=0;[VR.w,VR.h]=vrTarget()}
    $('vrEnv').innerHTML=[['gallery','Gallery'],['home','Home'],['loft','Loft']].map(([k2,l])=>`<button type="button" data-env="${k2}" aria-pressed="${VR.env===k2}">${l}</button>`).join('');
    $('vrEve').textContent=VR.eve?'☾ Evening':'☀ Day';$('vrEve').setAttribute('aria-pressed',VR.eve);$('vrDims').setAttribute('aria-pressed',VR.dims);
    $('vrInfo').innerHTML=`<div><div class="vr-ed">${kind==='orig'?'ORIGINAL PAINTING · ONE OF A KIND':esc(FMT[sel.f].en.toUpperCase())}</div><h2 class="vr-title">${esc(a.n)}</h2></div>${sizes}${fins}
      <div class="vr-card"><div>${price}</div>${qr?`<div class="qr">${qr}<small>SHOP ONLINE</small></div>`:''}</div>
      ${flagged?'<p style="margin:0;color:#ffb46b;direction:rtl;font-size:.85rem">למוכר: המחיר של הגודל הזה באתר נראה שגוי. לבדוק עם אלברט.</p>':`<div class="vr-cta"><button class="gold" type="button" data-cx="deal">✓ סגירת עסקה</button><button class="line" type="button" data-cx="add">+ לחבילה</button></div>`}`;
    roll($('vrInfo'));const [tw,th]=vrTarget();vrAnimate(tw,th,fresh);return}
  let h=`<div class="cc"><div class="who"><span class="A">A</span><b>Albert Levi</b></div>`;
  const c=pkgCalc();h+=`<h2>Your collection</h2><div class="lines">${c.items.map(x=>{const a=ART.find(y=>y.id===x.id);return `<div><span class="li">${a?`<img class="th" src="${img(a)}" alt="">`:''}<span>${esc(x.n)}<br><small style="color:#aab6e6">${esc(x.spec)}</small></span></span><span>${x.fin!==x.list?`<s style="color:#aab6e6;font-weight:500">${$f(x.list)}</s> `:''}${$f(x.fin)}</span></div>`}).join('')}</div>
    <div class="big">${c.fin<c.list?`<s>${$f(c.list)}</s>`:''}${$f(c.fin)}</div><div class="cbtns"><button class="gold" type="button" data-cx="pdeal">✓ סגירת עסקה</button><button class="line" type="button" data-cx="x">סגירה</button></div>`;
  $('cust').innerHTML=h+`</div>`}
function vrSizes(){const F=cur.f[sel.f];return Object.keys(F).sort((x,y)=>area(x)-area(y)).filter(s=>Object.keys(F[s]).some(z=>{const c=cell(cur,sel.f,s,z);return c&&!c.w}))}
function vrSetSize(s){sel={f:sel.f,s,fr:cur.f[sel.f][s][sel.fr]!==undefined?sel.fr:FRO.find(z=>cur.f[sel.f][s][z]!==undefined)};renderCust();renderDetail();const b=$('vrInfo').querySelector(`[data-cs="${s}"]`);b&&b.scrollIntoView({inline:'center',block:'nearest',behavior:'smooth'})}
$('cust').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;const d=b.dataset;
  if(d.env){VR.env=d.env;renderCust();return}
  if(d.vr==='eve'){VR.eve=!VR.eve;renderCust();return}
  if(d.vr==='dims'){VR.dims=!VR.dims;renderCust();return}
  if(d.cs){vrSetSize(d.cs);return}
  if(d.cf){sel=Object.assign({},sel,{fr:d.cf});renderCust();renderDetail();return}
  if(d.cx==='add'){const it=current();if(it){pkg.push(it);persist();toast('נוסף לחבילה · '+pkg.length)}return}
  if(d.cx==='deal'){const it=current();const p=single(it);return openClose([Object.assign({},it,{fin:p.fin})],false)}
  if(d.cx==='pdeal'){return openClose(pkgCalc().items,true)}
  if(d.cx==='x')back()});
(function(){let x0=null;$('cust').addEventListener('pointerdown',e=>{if(e.target.id==='vrc')x0=e.clientX});
  $('cust').addEventListener('pointerup',e=>{if(x0==null)return;const dx=e.clientX-x0;x0=null;if(Math.abs(dx)<40||kind==='orig'||sel.custom)return;const ss=vrSizes(),i=ss.indexOf(sel.s);const n=dx<0?Math.min(ss.length-1,i+1):Math.max(0,i-1);if(n!==i&&ss[n])vrSetSize(ss[n])})})();
window.addEventListener('resize',()=>{if(!$('cust').hidden&&$('vrc'))vrDraw();if(!$('detail').hidden)drawMini()});
""")
R("function showCust(o){CV=o;renderCust();","function showCust(o){CV=o;$('cust').innerHTML='';renderCust();")
open('tpl5.html','w').write(t)
print('ok')

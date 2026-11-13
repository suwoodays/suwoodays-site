# Nelson Bay dolphin cruise: boom net lowered from the boat's side deck
import random, math
random.seed(11)
W,H=1600,1000
o=[]; a=o.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')
a('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3f9be0"/><stop offset="1" stop-color="#bfe6fa"/></linearGradient>
<linearGradient id="sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2b8fb5"/><stop offset=".5" stop-color="#18779c"/><stop offset="1" stop-color="#0c5878"/></linearGradient>
<linearGradient id="netsea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3fb7c4"/><stop offset="1" stop-color="#1f93a6"/></linearGradient>
<linearGradient id="hull" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#d5dde4"/></linearGradient>
<linearGradient id="pole" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4f6f8"/><stop offset="1" stop-color="#9aa6b0"/></linearGradient>
<radialGradient id="sun" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#fffbe0"/><stop offset=".4" stop-color="#fff3a8" stop-opacity=".8"/><stop offset="1" stop-color="#fff3a8" stop-opacity="0"/></radialGradient>
</defs>''')
HZ=330
a(f'<rect width="{W}" height="{HZ}" fill="url(#sky)"/>')
a('<circle cx="1450" cy="90" r="130" fill="url(#sun)"/><circle cx="1450" cy="90" r="38" fill="#fffdf0"/>')
for cx,cy,s in [(1180,70,.8),(250,60,.7),(1500,230,.6)]:
    a(f'<g fill="#fff" opacity=".9" transform="translate({cx},{cy}) scale({s})"><ellipse rx="80" ry="24"/><ellipse cx="-45" cy="8" rx="50" ry="20"/><ellipse cx="50" cy="6" rx="60" ry="22"/><ellipse cx="10" cy="-18" rx="45" ry="26"/></g>')
a(f'<path d="M1180,{HZ} C1250,300 1320,285 1400,290 C1480,295 1550,280 1600,276 L1600,{HZ}Z" fill="#5e9677"/>')
a(f'<path d="M0,{HZ} L0,280 C60,270 120,268 180,285 L240,{HZ}Z" fill="#5e9677"/>')
a(f'<rect y="{HZ-2}" width="{W}" height="{H-HZ+2}" fill="url(#sea)"/>')
a('<ellipse cx="1450" cy="345" rx="130" ry="8" fill="#fff6c8" opacity=".5"/>')
for i in range(130):
    y=HZ+8+(i/130)**1.5*(H-HZ-10); x=random.uniform(-50,W); l=10+(y-HZ)/600*60
    a(f'<path d="M{x:.0f},{y:.0f} q{l/2:.0f},-{l/8:.1f} {l:.0f},0" stroke="#bfe9f7" stroke-width="{1+(y-HZ)/300:.1f}" fill="none" opacity=".5" stroke-linecap="round"/>')
# dolphins
def dolphin(x,y,s,rot=-20):
    a(f'<g transform="translate({x},{y}) rotate({rot}) scale({s})">'
      '<path d="M-60,0 C-40,-28 20,-34 55,-12 C66,-6 78,-4 86,-2 C76,4 62,4 52,6 C30,16 -20,18 -60,0Z" fill="#5d6f80"/>'
      '<path d="M-60,0 C-30,10 20,12 52,6 C30,16 -20,18 -60,0Z" fill="#c9d3dc"/>'
      '<path d="M-6,-26 C0,-46 12,-50 20,-52 C14,-42 14,-34 16,-24Z" fill="#4c5d6d"/>'
      '<path d="M-58,0 C-72,-14 -84,-16 -92,-14 C-82,-6 -82,4 -92,12 C-80,12 -70,8 -58,2Z" fill="#4c5d6d"/>'
      '<circle cx="58" cy="-8" r="2.2" fill="#1d2833"/></g>')
dolphin(1430,385,.7,-28); a('<path d="M1360,398 q30,-8 60,0 q30,8 60,0" stroke="#e8f8ff" stroke-width="3" fill="none"/>')
dolphin(1530,415,.5,12)
# ---------------- boat ----------------
DECK=535; WL=600
a(f'<ellipse cx="720" cy="{WL+8}" rx="700" ry="22" fill="#0a4562" opacity=".45"/>')
# hull
a(f'<path d="M70,{DECK} L1290,{DECK} C1340,{DECK} 1390,{DECK-30} 1420,{DECK-55} L1380,{WL} L110,{WL} Z" fill="url(#hull)" stroke="#8fa3b3" stroke-width="2"/>')
a(f'<path d="M96,{WL-22} L1372,{WL-22}" stroke="#1d5fa8" stroke-width="8"/>')
# main cabin
a(f'<path d="M110,{DECK} L110,400 L1150,400 L1250,{DECK}Z" fill="#f5f8fa" stroke="#8fa3b3" stroke-width="2"/>')
a('<path d="M110,400 L1150,400 L1165,420 L110,420Z" fill="#1d5fa8"/>')
for i in range(11):
    a(f'<rect x="{140+i*90}" y="438" width="70" height="52" rx="5" fill="#2e5f7d" opacity=".9"/>')
# upper deck
a('<path d="M200,400 L240,310 L900,310 L980,400Z" fill="#eef2f5" stroke="#8fa3b3" stroke-width="2"/>')
for i in range(6):
    a(f'<rect x="{280+i*100}" y="330" width="78" height="44" rx="5" fill="#2e5f7d" opacity=".85"/>')
a('<path d="M240,310 L900,310" stroke="#1d5fa8" stroke-width="5"/>')
# top deck railing
a('<path d="M260,310 L260,270 L860,270 L860,310" stroke="#c4ced6" stroke-width="3" fill="none"/>')
for x in range(280,860,30): a(f'<line x1="{x}" y1="270" x2="{x}" y2="310" stroke="#c4ced6" stroke-width="2"/>')
a('<line x1="560" y1="270" x2="560" y2="180" stroke="#9aa6b0" stroke-width="5"/>')
a('<path d="M562,182 L640,182 L640,232 L562,232Z" fill="#1f3b8c"/>')
a('<g fill="#fff"><circle cx="618" cy="195" r="3"/><circle cx="628" cy="210" r="3"/><circle cx="612" cy="220" r="3"/><circle cx="585" cy="220" r="5"/></g>')
a('<path d="M562,182 L600,182 L600,206 L562,206Z" fill="#c8102e" opacity=".0"/>')
a('<rect x="380" y="352" width="0" height="0"/>')
a('<rect x="560" y="410" width="0" height="0"/>')
a('<text x="640" y="415" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="15" font-weight="bold" fill="#fff">DOLPHIN WATCH CRUISE</text>')
# main deck railing (with opening where net hangs)
NL,NR=430,1110
a(f'<path d="M110,{DECK} L110,{DECK-38} L{NL-10},{DECK-38}" stroke="#c4ced6" stroke-width="4" fill="none"/>')
a(f'<path d="M{NR+10},{DECK-38} L1250,{DECK-38} L1250,{DECK}" stroke="#c4ced6" stroke-width="4" fill="none"/>')
for x in list(range(130,NL,28))+list(range(NR+20,1250,28)):
    a(f'<line x1="{x}" y1="{DECK-38}" x2="{x}" y2="{DECK}" stroke="#c4ced6" stroke-width="2"/>')
# deck people
def deckp(x,y,shirt,hair,arm=None,s=1):
    g=f'<g transform="translate({x},{y}) scale({s})"><rect x="-10" y="0" width="20" height="34" rx="6" fill="{shirt}"/><circle cx="0" cy="-10" r="10" fill="#f1c7a0"/><path d="M-10,-12 a10,10 0 0 1 20,0Z" fill="{hair}"/>'
    if arm=='up': g+='<path d="M8,6 L20,-18" stroke="#f1c7a0" stroke-width="5" stroke-linecap="round"/>'
    if arm=='point': g+='<path d="M8,8 L28,14" stroke="#f1c7a0" stroke-width="5" stroke-linecap="round"/>'
    a(g+'</g>')
deckp(330,282,'#e85d75','#3a2a1e','up',.8); deckp(420,282,'#ffd23f','#7a4a22',None,.8); deckp(760,282,'#4caf50','#222','point',.8)
deckp(200,DECK-60,'#ff8a3d','#c08a4a','point'); deckp(1180,DECK-60,'#7e57c2','#2b1d14','up'); deckp(1215,DECK-58,'#26a69a','#d9a441')
# crew on stern near net
deckp(395,DECK-62,'#ffffff','#3a2a1e',None)
# ---------------- boom net ----------------
POLE=850; PL,PR=330,1220
def P(u,v):
    xl=NL+(PL-NL)*v; xr=NR+(PR-NR)*v
    x=xl+(xr-xl)*u
    y=DECK+(POLE-DECK)*v + 70*math.sin(math.pi*v)*(0.55+0.45*math.sin(math.pi*u))
    return x,y
# water seen through net (net sits in the sea)
edge=[P(u/30,0) for u in range(31)]+[P(1,v/30) for v in range(31)]+[P(1-u/30,1) for u in range(31)]+[P(0,1-v/30) for v in range(31)]
# side arms (aluminium frame)
a(f'<line x1="{NL}" y1="{DECK}" x2="{PL}" y2="{POLE}" stroke="url(#pole)" stroke-width="12" stroke-linecap="round"/>')
a(f'<line x1="{NR}" y1="{DECK}" x2="{PR}" y2="{POLE}" stroke="url(#pole)" stroke-width="12" stroke-linecap="round"/>')
# support ropes from upper deck to pole corners
a(f'<path d="M250,320 Q300,600 {PL},{POLE}" stroke="#d9c7a2" stroke-width="3" fill="none"/>')
a(f'<path d="M940,320 Q1150,600 {PR},{POLE}" stroke="#d9c7a2" stroke-width="3" fill="none"/>')
# underwater mesh (faint) + bodies
rows,cols=18,34
def mesh(color,width,op):
    for i in range(rows+1):
        v=i/rows; pts=" ".join(f"{P(j/cols,v)[0]:.1f},{P(j/cols,v)[1]:.1f}" for j in range(cols+1))
        a(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{width*(0.7+v*0.8):.1f}" opacity="{op}"/>')
    for j in range(cols+1):
        u=j/cols; pts=" ".join(f"{P(u,i/rows)[0]:.1f},{P(u,i/rows)[1]:.1f}" for i in range(rows+1))
        a(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{width:.1f}" opacity="{op}"/>')
# dry band near deck: v<0.14 ; water line across net
WV=0.16
a(f'<clipPath id="wet"><polygon points="{" ".join(f"{P(u/30,WV)[0]:.0f},{P(u/30,WV)[1]:.0f}" for u in range(31))} {PR},{POLE+40} {PL},{POLE+40}"/></clipPath>')
a(f'<clipPath id="dry"><polygon points="{NL},{DECK-5} {NR},{DECK-5} {" ".join(f"{P(1-u/30,WV)[0]:.0f},{P(1-u/30,WV)[1]:.0f}" for u in range(31))}"/></clipPath>')
a('<g clip-path="url(#wet)">')
a(f'<polygon points="{" ".join(f"{x:.0f},{y:.0f}" for x,y in edge)}" fill="url(#netsea)" opacity=".55"/>')
mesh('#d8f2ee',1.6,.55)
a('</g>')
# shadow of hull on net water
a(f'<path d="M{NL},{WL} L{NR},{WL} L{NR+20},{WL+30} L{NL-15},{WL+30}Z" fill="#0b4a66" opacity=".25"/>')
a('<g clip-path="url(#dry)">'); mesh('#f6efdc',2.2,.95); a('</g>')
# waterline ripples along net
pts=" ".join(f"{P(u/30,WV)[0]:.0f},{P(u/30,WV)[1]:.0f}" for u in range(31))
a(f'<polyline points="{pts}" fill="none" stroke="#e9fbff" stroke-width="4" opacity=".8" stroke-dasharray="26 10"/>')
# hinge along deck edge
a(f'<line x1="{NL}" y1="{DECK}" x2="{NR}" y2="{DECK}" stroke="#aeb9c2" stroke-width="8" stroke-linecap="round"/>')
# outer pole at surface
a(f'<ellipse cx="{(PL+PR)/2}" cy="{POLE+8}" rx="{(PR-PL)/2+40}" ry="16" fill="none" stroke="#e9fbff" stroke-width="3" opacity=".6"/>')
a(f'<line x1="{PL}" y1="{POLE}" x2="{PR}" y2="{POLE}" stroke="url(#pole)" stroke-width="16" stroke-linecap="round"/>')
a(f'<line x1="{PL}" y1="{POLE-4}" x2="{PR}" y2="{POLE-4}" stroke="#ffffff" stroke-width="3" opacity=".8"/>')
# ---------------- people in the net ----------------
skins=['#f1c7a0','#e0ac80','#c68c5e','#8d5b3c','#f6d2b4']
def swimmer(u,v,cap,hair,suit,pose,sc=1.0):
    x,y=P(u,v); s=(0.62+0.5*v)*sc; sk=random.choice(skins)
    g=f'<g transform="translate({x:.0f},{y-8*s:.0f}) scale({s:.2f})">'
    # submerged body/legs (faint)
    g+=f'<g opacity=".4"><rect x="-17" y="6" width="34" height="34" rx="10" fill="{suit}"/><path d="M-10,36 C-22,44 -28,48 -36,50" stroke="{sk}" stroke-width="10" fill="none" stroke-linecap="round"/><path d="M10,36 C0,46 -6,50 -14,54" stroke="{sk}" stroke-width="10" fill="none" stroke-linecap="round"/></g>'
    g+='<ellipse cx="0" cy="10" rx="40" ry="9" fill="none" stroke="#f0fcff" stroke-width="3" opacity=".9"/>'
    g+='<ellipse cx="0" cy="11" rx="56" ry="13" fill="none" stroke="#f0fcff" stroke-width="2" opacity=".5"/>'
    g+=f'<path d="M-22,10 C-20,-4 20,-4 22,10Z" fill="{sk}"/>'
    if pose=='wave':
        g+=f'<path d="M14,2 C26,-14 30,-34 26,-52" stroke="{sk}" stroke-width="8" fill="none" stroke-linecap="round"/><circle cx="26" cy="-55" r="6" fill="{sk}"/>'
    elif pose=='both':
        g+=f'<path d="M14,2 C24,-14 30,-30 34,-48" stroke="{sk}" stroke-width="8" fill="none" stroke-linecap="round"/><circle cx="35" cy="-51" r="6" fill="{sk}"/>'
        g+=f'<path d="M-14,2 C-24,-14 -30,-30 -34,-48" stroke="{sk}" stroke-width="8" fill="none" stroke-linecap="round"/><circle cx="-35" cy="-51" r="6" fill="{sk}"/>'
    elif pose=='hold':
        g+=f'<path d="M14,4 C24,-2 34,-2 42,4" stroke="{sk}" stroke-width="8" fill="none" stroke-linecap="round"/><path d="M-14,4 C-24,-2 -34,-2 -42,4" stroke="{sk}" stroke-width="8" fill="none" stroke-linecap="round"/>'
    elif pose=='splash':
        g+=f'<path d="M14,4 C30,0 40,-6 48,-14" stroke="{sk}" stroke-width="8" fill="none" stroke-linecap="round"/>'
        g+='<g fill="#fff"><circle cx="58" cy="-26" r="5"/><circle cx="70" cy="-14" r="4"/><circle cx="64" cy="-40" r="3.5"/><circle cx="78" cy="-30" r="3"/></g><path d="M50,-8 C58,-30 68,-40 82,-44" stroke="#fff" stroke-width="3" fill="none" opacity=".8"/>'
    elif pose=='lean':  # leaning back, arms spread on net
        g+=f'<path d="M14,6 C30,6 44,10 56,6" stroke="{sk}" stroke-width="8" fill="none" stroke-linecap="round"/><path d="M-14,6 C-30,6 -44,10 -56,6" stroke="{sk}" stroke-width="8" fill="none" stroke-linecap="round"/>'
    g+=f'<circle cx="0" cy="-14" r="15" fill="{sk}"/>'
    if cap: g+=f'<path d="M-15,-14 a15,15 0 0 1 30,0Z" fill="{cap}"/>'
    else: g+=f'<path d="M-16,-12 C-16,-34 16,-34 16,-12 C10,-22 -6,-24 -16,-12Z" fill="{hair}"/>'
    if pose=='lean': g+='<rect x="-11" y="-17" width="22" height="7" rx="3" fill="#222"/>'
    else: g+='<circle cx="-5" cy="-12" r="1.8" fill="#222"/><circle cx="5" cy="-12" r="1.8" fill="#222"/>'
    g+='<path d="M-6,-5 Q0,1 6,-5" stroke="#8a2b2b" stroke-width="2" fill="#fff"/></g>'
    a(g)
crowd=[(.12,.42,None,'#3a2a1e','#e63946','wave'),(.30,.36,'#ffd166',None,'#118ab2','hold'),(.52,.34,None,'#111','#8338ec','splash'),
       (.74,.38,None,'#c58b4c','#06d6a0','lean'),(.90,.44,'#ef476f',None,'#ef476f','both'),
       (.20,.66,None,'#5a3a22','#ff7f11','lean'),(.42,.62,'#00bbf9',None,'#00bbf9','both'),(.63,.64,None,'#2b1d14','#f15bb5','wave'),
       (.84,.70,None,'#e0b060','#1d3557','splash'),(.08,.84,'#06d6a0',None,'#06d6a0','hold'),(.33,.86,None,'#111','#ffb703','splash'),(.70,.86,None,'#7a4a22','#e63946','hold')]
for u,v,c,h,sut,p in sorted(crowd,key=lambda t:t[1]): swimmer(u,v,c,h,sut,p)
# kid in a ring
x,y=P(.53,.82)
a(f'<g transform="translate({x:.0f},{y+6:.0f})"><ellipse rx="44" ry="17" fill="#ff4d6d"/><ellipse rx="24" ry="8" fill="#2aa3b5"/><path d="M-44,0 a44,17 0 0 0 22,14" stroke="#fff" stroke-width="9" fill="none"/><path d="M30,-13 a44,17 0 0 1 14,8" stroke="#fff" stroke-width="9" fill="none"/></g>')
swimmer(.53,.80,.95,None,None,'both') if False else None
x,y=P(.53,.80); s=1.0
a(f'<g transform="translate({x:.0f},{y-4:.0f}) scale(.8)"><path d="M-20,8 C-18,-4 18,-4 20,8Z" fill="#f1c7a0"/><path d="M14,2 C24,-14 30,-30 34,-46" stroke="#f1c7a0" stroke-width="8" fill="none" stroke-linecap="round"/><path d="M-14,2 C-24,-14 -30,-30 -34,-46" stroke="#f1c7a0" stroke-width="8" fill="none" stroke-linecap="round"/><circle cx="0" cy="-14" r="15" fill="#f1c7a0"/><path d="M-15,-14 a15,15 0 0 1 30,0Z" fill="#ffd166"/><circle cx="-5" cy="-12" r="1.8" fill="#222"/><circle cx="5" cy="-12" r="1.8" fill="#222"/><path d="M-6,-5 Q0,2 6,-5" stroke="#8a2b2b" stroke-width="2" fill="#fff"/></g>')
# person sitting on the dry upper net near the deck, feet dangling into water
x,y=P(.62,.07)
a(f'<g transform="translate({x:.0f},{y:.0f}) scale(.75)"><rect x="-12" y="-30" width="24" height="32" rx="8" fill="#f1c7a0"/><rect x="-12" y="-2" width="24" height="12" rx="4" fill="#264653"/>'
  '<path d="M-6,8 C-8,30 -6,44 -10,58" stroke="#f1c7a0" stroke-width="9" fill="none" stroke-linecap="round"/><path d="M6,8 C10,30 12,44 14,58" stroke="#f1c7a0" stroke-width="9" fill="none" stroke-linecap="round"/>'
  '<path d="M-12,-24 L-26,0" stroke="#f1c7a0" stroke-width="7" stroke-linecap="round"/><path d="M12,-24 L26,0" stroke="#f1c7a0" stroke-width="7" stroke-linecap="round"/>'
  '<circle cx="0" cy="-42" r="13" fill="#f1c7a0"/><path d="M-13,-44 C-13,-62 13,-62 13,-44 C8,-52 -6,-54 -13,-44Z" fill="#3a2a1e"/></g>')
# seagulls
for x,y,s in [(1000,180,1),(1060,210,.7),(160,200,.8)]:
    a(f'<path transform="translate({x},{y}) scale({s})" d="M-18,0 Q-9,-10 0,0 Q9,-10 18,0" stroke="#33414d" stroke-width="3" fill="none"/>')
for i in range(12):
    x=i*150-40; a(f'<path d="M{x},965 q40,-22 80,0 q40,22 80,0" stroke="#d6f3fb" stroke-width="4" fill="none" opacity=".45"/>')
a('<rect x="1150" y="905" width="420" height="64" rx="14" fill="#fff" opacity=".85"/>')
a('<text x="1172" y="947" font-family="Arial,Helvetica,sans-serif" font-size="28" font-weight="bold" fill="#0f5b80">Nelson Bay · Boom Net Fun</text>')
a('</svg>')
open('nelson-bay-boom-net.svg','w').write("\n".join(o))

import random, math
random.seed(7)
W,H=1600,1000
o=[]
a=o.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')
a('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5fb4e8"/><stop offset="1" stop-color="#cdeefb"/></linearGradient>
<linearGradient id="sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a8fb8"/><stop offset=".45" stop-color="#1f7fa8"/><stop offset="1" stop-color="#0f5b80"/></linearGradient>
<linearGradient id="netwater" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4fc3d9" stop-opacity=".55"/><stop offset="1" stop-color="#1b86a8" stop-opacity=".35"/></linearGradient>
<linearGradient id="hull" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#d7dfe6"/></linearGradient>
<radialGradient id="sun" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#fffbe0"/><stop offset=".4" stop-color="#fff3a8" stop-opacity=".9"/><stop offset="1" stop-color="#fff3a8" stop-opacity="0"/></radialGradient>
<clipPath id="netclip"><polygon points="640,560 1420,560 1560,860 470,860"/></clipPath>
</defs>''')
# sky
a(f'<rect width="{W}" height="400" fill="url(#sky)"/>')
a('<circle cx="1330" cy="110" r="150" fill="url(#sun)"/><circle cx="1330" cy="110" r="42" fill="#fffdf0"/>')
for cx,cy,s in [(260,120,1),(620,80,.7),(980,150,.85)]:
    a(f'<g fill="#fff" opacity=".9" transform="translate({cx},{cy}) scale({s})"><ellipse cx="0" cy="0" rx="80" ry="26"/><ellipse cx="-45" cy="8" rx="50" ry="20"/><ellipse cx="50" cy="6" rx="60" ry="22"/><ellipse cx="10" cy="-18" rx="45" ry="26"/></g>')
# headlands (Port Stephens)
a('<path d="M0,395 L0,300 C80,280 150,250 230,262 C300,272 340,320 420,335 C500,350 560,372 640,380 L700,395 Z" fill="#4f8a6a"/>')
a('<path d="M0,395 L0,330 C90,315 180,300 260,318 C330,334 380,360 470,375 L540,395Z" fill="#3e7457"/>')
a('<path d="M1080,395 C1140,370 1200,340 1270,335 C1350,330 1420,352 1500,348 C1550,346 1580,340 1600,336 L1600,395Z" fill="#6a9c80"/>')
a('<path d="M1180,395 C1230,382 1290,372 1360,375 C1440,378 1530,384 1600,380 L1600,395Z" fill="#558a6c"/>')
# sea
a(f'<rect y="392" width="{W}" height="{H-392}" fill="url(#sea)"/>')
a('<ellipse cx="1330" cy="420" rx="160" ry="10" fill="#fff6c8" opacity=".5"/>')
for i in range(140):
    y=400+ (i/140)**1.6*590
    x=random.uniform(-50,W)
    l=10+ (y-400)/590*60
    a(f'<path d="M{x:.0f},{y:.0f} q{l/2:.0f},-{l/8:.1f} {l:.0f},0" stroke="#bfe9f7" stroke-width="{1+(y-400)/300:.1f}" fill="none" opacity=".55" stroke-linecap="round"/>')
# dolphins
def dolphin(x,y,s,flip=False,rot=-20):
    sc=f"scale({-s if flip else s},{s})"
    a(f'<g transform="translate({x},{y}) rotate({rot}) {sc}">'
      '<path d="M-60,0 C-40,-28 20,-34 55,-12 C66,-6 78,-4 86,-2 C76,4 62,4 52,6 C30,16 -20,18 -60,0Z" fill="#5d6f80"/>'
      '<path d="M-60,0 C-30,10 20,12 52,6 C30,16 -20,18 -60,0Z" fill="#c9d3dc"/>'
      '<path d="M-6,-26 C0,-46 12,-50 20,-52 C14,-42 14,-34 16,-24Z" fill="#4c5d6d"/>'
      '<path d="M-58,0 C-72,-14 -84,-16 -92,-14 C-82,-6 -82,4 -92,12 C-80,12 -70,8 -58,2Z" fill="#4c5d6d"/>'
      '<circle cx="58" cy="-8" r="2.2" fill="#1d2833"/></g>')
dolphin(1180,440,.75,rot=-25)
a('<path d="M1100,452 q30,-8 60,0 q30,8 60,0" stroke="#e8f8ff" stroke-width="3" fill="none"/>')
dolphin(1290,470,.55,rot=15)
a('<g fill="#fff" opacity=".8"><circle cx="1255" cy="468" r="3"/><circle cx="1262" cy="458" r="2"/><circle cx="1320" cy="478" r="3"/></g>')
# boat (catamaran) on left
a('<g>')
a('<ellipse cx="400" cy="585" rx="330" ry="24" fill="#0c4a69" opacity=".45"/>')
a('<path d="M90,520 L700,520 L670,578 L140,578 Z" fill="url(#hull)" stroke="#8fa3b3" stroke-width="2"/>')
a('<path d="M118,560 L686,560" stroke="#1e88c7" stroke-width="7"/>')
a('<path d="M128,572 L678,572" stroke="#f2b632" stroke-width="3"/>')
for i in range(9):
    a(f'<circle cx="{180+i*55}" cy="540" r="7" fill="#33586f" stroke="#cfd9e1" stroke-width="2"/>')
# deck & cabin
a('<path d="M150,520 L180,450 L560,450 L610,520Z" fill="#f4f7fa" stroke="#8fa3b3" stroke-width="2"/>')
for i in range(6):
    a(f'<rect x="{205+i*58}" y="465" width="44" height="30" rx="4" fill="#2f6f93" opacity=".85"/>')
a('<path d="M200,450 L215,410 L500,410 L520,450Z" fill="#e9eef3" stroke="#8fa3b3" stroke-width="2"/>')
a('<rect x="255" y="378" width="190" height="32" fill="#1e88c7"/>')
a('<text x="350" y="400" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="18" font-weight="bold" fill="#fff">DOLPHIN CRUISE</text>')
# mast & flag
a('<line x1="350" y1="378" x2="350" y2="300" stroke="#8a9aa8" stroke-width="5"/>')
a('<path d="M350,302 L400,315 L350,328Z" fill="#f2b632"/>')
# railing & stern platform
a('<path d="M560,450 L610,520 L700,520" stroke="#8fa3b3" stroke-width="3" fill="none"/>')
for x in range(600,700,14):
    a(f'<line x1="{x}" y1="505" x2="{x}" y2="520" stroke="#8fa3b3" stroke-width="2"/>')
a('<line x1="600" y1="505" x2="700" y2="505" stroke="#8fa3b3" stroke-width="3"/>')
# booms going back to net
a('<line x1="690" y1="510" x2="1430" y2="560" stroke="#c9a46b" stroke-width="6"/>')
a('<line x1="660" y1="560" x2="660" y2="560" stroke="#c9a46b" stroke-width="6"/>')
a('</g>')
# people on boat deck
def deckperson(x,y,shirt,hair,armup=False):
    a(f'<g transform="translate({x},{y})">'
      f'<rect x="-8" y="0" width="16" height="26" rx="5" fill="{shirt}"/>'
      f'<circle cx="0" cy="-8" r="8" fill="#f1c7a0"/><path d="M-8,-10 a8,8 0 0 1 16,0 Z" fill="{hair}"/>'
      + (f'<path d="M6,4 L16,-14" stroke="#f1c7a0" stroke-width="4" stroke-linecap="round"/>' if armup else '')
      + '</g>')
deckperson(620,478,'#e85d75','#3a2a1e',True)
deckperson(650,480,'#ffd23f','#7a4a22')
deckperson(240,423,'#4caf50','#222',False)
deckperson(470,423,'#ff8a3d','#c08a4a',True)
# NET area
a('<polygon points="640,560 1420,560 1560,860 470,860" fill="url(#netwater)"/>')
# underwater bodies (drawn first, faint)
people=[(760,610,.7,'#e63946','#3a2a1e'),(930,600,.68,'#1d3557','#d9a441'),(1100,605,.68,'#ffb703','#3a2a1e'),(1290,610,.7,'#8338ec','#111'),
        (700,720,.9,'#06d6a0','#5a3a22'),(900,700,.88,'#ef476f','#111'),(1110,715,.9,'#118ab2','#c58b4c'),(1330,705,.88,'#ff7f11','#3a2a1e'),
        (820,815,1.05,'#f15bb5','#2b1d14'),(1210,820,1.05,'#00bbf9','#e0b060')]
a('<g clip-path="url(#netclip)">')
for x,y,s,c,h in people:
    a(f'<g transform="translate({x},{y}) scale({s})" opacity=".45">'
      f'<path d="M-12,10 C-14,40 -10,60 -16,90" stroke="#e7b48c" stroke-width="9" fill="none" stroke-linecap="round"/>'
      f'<path d="M12,10 C16,40 22,60 30,85" stroke="#e7b48c" stroke-width="9" fill="none" stroke-linecap="round"/>'
      f'<rect x="-17" y="5" width="34" height="34" rx="10" fill="{c}"/></g>')
# net mesh
rows=12; cols=22
def P(u,v):
    xl=640+(470-640)*v; xr=1420+(1560-1420)*v
    y=560+300*(v**1.0)
    return xl+(xr-xl)*u, y+math.sin(u*math.pi*3+v*5)*3
for i in range(rows+1):
    v=i/rows; pts=" ".join(f"{P(j/cols,v)[0]:.1f},{P(j/cols,v)[1]:.1f}" for j in range(cols+1))
    a(f'<polyline points="{pts}" fill="none" stroke="#f3e9cf" stroke-width="{1+v*1.5:.1f}" opacity=".75"/>')
for j in range(cols+1):
    u=j/cols; pts=" ".join(f"{P(u,i/rows)[0]:.1f},{P(u,i/rows)[1]:.1f}" for i in range(rows+1))
    a(f'<polyline points="{pts}" fill="none" stroke="#f3e9cf" stroke-width="1.6" opacity=".75"/>')
a('</g>')
# net frame/ropes & floats
a('<polygon points="640,560 1420,560 1560,860 470,860" fill="none" stroke="#e0b46a" stroke-width="7" stroke-linejoin="round"/>')
for t in [i/10 for i in range(11)]:
    for (x1,y1,x2,y2) in [(640,560,1420,560),(470,860,1560,860)]:
        x=x1+(x2-x1)*t; y=y1
        r=7 if y1==560 else 11
        a(f'<ellipse cx="{x:.0f}" cy="{y}" rx="{r*1.4}" ry="{r}" fill="#ff8c1a" stroke="#c45f00" stroke-width="2"/>')
a('<line x1="670" y1="545" x2="640" y2="560" stroke="#e0b46a" stroke-width="5"/>')
a('<line x1="660" y1="560" x2="470" y2="860" stroke="#e0b46a" stroke-width="6"/>')
# swimmers (above water)
skins=['#f1c7a0','#e0ac80','#c68c5e','#8d5b3c','#f6d2b4']
def swimmer(x,y,s,cap,hair,pose):
    sk=random.choice(skins)
    g=f'<g transform="translate({x},{y}) scale({s})">'
    # ripple
    g+='<ellipse cx="0" cy="10" rx="42" ry="9" fill="none" stroke="#e9fbff" stroke-width="3" opacity=".9"/>'
    g+='<ellipse cx="0" cy="10" rx="58" ry="13" fill="none" stroke="#e9fbff" stroke-width="2" opacity=".5"/>'
    # shoulders
    g+=f'<path d="M-22,10 C-20,-4 20,-4 22,10 Z" fill="{sk}"/>'
    if pose=='wave':
        g+=f'<path d="M14,2 C26,-14 30,-34 26,-52" stroke="{sk}" stroke-width="8" fill="none" stroke-linecap="round"/><circle cx="26" cy="-55" r="6" fill="{sk}"/>'
        g+=f'<path d="M-14,4 C-26,-2 -34,4 -40,8" stroke="{sk}" stroke-width="8" fill="none" stroke-linecap="round"/>'
    elif pose=='both':
        g+=f'<path d="M14,2 C24,-14 30,-30 34,-48" stroke="{sk}" stroke-width="8" fill="none" stroke-linecap="round"/><circle cx="35" cy="-51" r="6" fill="{sk}"/>'
        g+=f'<path d="M-14,2 C-24,-14 -30,-30 -34,-48" stroke="{sk}" stroke-width="8" fill="none" stroke-linecap="round"/><circle cx="-35" cy="-51" r="6" fill="{sk}"/>'
    elif pose=='hold':
        g+=f'<path d="M14,4 C24,-2 34,-4 42,2" stroke="{sk}" stroke-width="8" fill="none" stroke-linecap="round"/>'
        g+=f'<path d="M-14,4 C-24,-2 -34,-4 -42,2" stroke="{sk}" stroke-width="8" fill="none" stroke-linecap="round"/>'
    elif pose=='splash':
        g+=f'<path d="M14,4 C30,0 40,-6 48,-14" stroke="{sk}" stroke-width="8" fill="none" stroke-linecap="round"/>'
        g+='<g fill="#fff"><circle cx="58" cy="-26" r="5"/><circle cx="70" cy="-14" r="4"/><circle cx="64" cy="-40" r="3.5"/><circle cx="78" cy="-30" r="3"/><circle cx="52" cy="-46" r="2.5"/></g>'
        g+='<path d="M50,-8 C58,-30 68,-40 82,-44" stroke="#fff" stroke-width="3" fill="none" opacity=".8"/>'
    # head
    g+=f'<circle cx="0" cy="-14" r="15" fill="{sk}"/>'
    if cap:
        g+=f'<path d="M-15,-14 a15,15 0 0 1 30,0 Z" fill="{cap}"/>'
    else:
        g+=f'<path d="M-16,-12 C-16,-34 16,-34 16,-12 C10,-22 -6,-24 -16,-12Z" fill="{hair}"/>'
    g+='<circle cx="-5" cy="-12" r="1.8" fill="#222"/><circle cx="5" cy="-12" r="1.8" fill="#222"/>'
    g+='<path d="M-6,-5 Q0,1 6,-5" stroke="#8a2b2b" stroke-width="2" fill="#fff"/>'
    g+='</g>'
    a(g)
poses=['wave','hold','both','splash','hold','wave','splash','both','hold','wave']
for (x,y,s,c,h),p in zip(people,poses):
    cap = c if p in ('hold','both') and random.random()<.6 else None
    swimmer(x,y,s,cap,h,p)
# kid with goggles on someone's... a floating ring
a('<g transform="translate(1010,790)"><ellipse rx="40" ry="16" fill="#ff4d6d"/><ellipse rx="22" ry="7" fill="#1b86a8" opacity=".9"/><path d="M-40,0 a40,16 0 0 0 20,13" stroke="#fff" stroke-width="9" fill="none"/><path d="M28,-12 a40,16 0 0 1 12,8" stroke="#fff" stroke-width="9" fill="none"/></g>')
swimmer(1010,775,.75,'#ffd166',None,'both')
# foreground waves
for i in range(12):
    x=i*150-40
    a(f'<path d="M{x},960 q40,-22 80,0 q40,22 80,0" stroke="#d6f3fb" stroke-width="4" fill="none" opacity=".5"/>')
# seagulls
for x,y,s in [(820,200,1),(880,230,.7),(560,250,.8)]:
    a(f'<path transform="translate({x},{y}) scale({s})" d="M-18,0 Q-9,-10 0,0 Q9,-10 18,0" stroke="#33414d" stroke-width="3" fill="none"/>')
# caption
a('<rect x="40" y="900" width="430" height="64" rx="14" fill="#ffffff" opacity=".85"/>')
a('<text x="62" y="942" font-family="Arial,Helvetica,sans-serif" font-size="28" font-weight="bold" fill="#0f5b80">Nelson Bay · Boom Net Fun</text>')
a('</svg>')
open('nelson-bay-boom-net.svg','w').write("\n".join(o))

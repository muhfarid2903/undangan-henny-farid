#!/usr/bin/env python3
# Generator SVG cover: hijau moss gelap + bunga juntai + medali emas (emblem dokter & guru)
import math, random
random.seed(716)  # tanggal nikah 16-07

W, H = 1080, 1920

def cubic(p0,p1,p2,p3,t):
    mt=1-t
    x=mt**3*p0[0]+3*mt*mt*t*p1[0]+3*mt*t*t*p2[0]+t**3*p3[0]
    y=mt**3*p0[1]+3*mt*mt*t*p1[1]+3*mt*t*t*p2[1]+t**3*p3[1]
    return x,y

def cubic_tan(p0,p1,p2,p3,t):
    mt=1-t
    dx=3*mt*mt*(p1[0]-p0[0])+6*mt*t*(p2[0]-p1[0])+3*t*t*(p3[0]-p2[0])
    dy=3*mt*mt*(p1[1]-p0[1])+6*mt*t*(p2[1]-p1[1])+3*t*t*(p3[1]-p2[1])
    return math.degrees(math.atan2(dy,dx))

def strand(x0, depth, sway):
    # dua segmen kubik -> kurva S lembut menjuntai
    s1,s2 = sway
    P0=(x0,0)
    P1=(x0+s1*0.4, depth*0.16)
    P2=(x0+s1, depth*0.34)
    P3=(x0+s1*0.7, depth*0.5)
    P4=(x0+s1*0.4, depth*0.64)
    P5=(x0+s2, depth*0.82)
    P6=(x0+s2*0.8, depth)
    return [(P0,P1,P2,P3),(P3,P4,P5,P6)]

def sample(seg_list, step=24):
    pts=[]
    for seg in seg_list:
        # estimasi panjang
        prev=seg[0]; L=0
        for i in range(1,41):
            t=i/40; p=cubic(*seg,t); L+=math.dist(prev,p); prev=p
        n=max(2,int(L/step))
        for i in range(n+1):
            t=i/n
            p=cubic(*seg,t); a=cubic_tan(*seg,t)
            pts.append((p[0],p[1],a,t))
    return pts

def seg_path(seg_list):
    d=f"M{seg_list[0][0][0]:.1f},{seg_list[0][0][1]:.1f} "
    for seg in seg_list:
        _,p1,p2,p3=seg
        d+=f"C{p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f} {p3[0]:.1f},{p3[1]:.1f} "
    return d

# --- definisi strand (juntai dari atas). Sisi kiri & kanan padat, tengah disisakan lapang ---
strands=[]
specs=[
    (40,760,(38,-30)),(115,600,(-26,34)),(205,880,(46,-22)),(295,520,(-30,40)),(90,400,(22,28)),(360,300,(30,-18)),
    (1040,740,(-40,28)),(965,600,(30,-32)),(875,860,(-44,24)),(785,500,(34,-30)),(995,380,(-22,-26)),(720,300,(-28,20)),
    (470,250,(18,-12)),(610,250,(-18,12)),
]
for x0,depth,sw in specs:
    strands.append((x0,depth,sw))

parts=[]
parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')

# ---- defs ----
parts.append('''<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#3a472d"/>
    <stop offset="0.42" stop-color="#2c3a25"/>
    <stop offset="1" stop-color="#1d281a"/>
  </linearGradient>
  <radialGradient id="vig" cx="0.5" cy="0.42" r="0.85">
    <stop offset="0" stop-color="#3c4a30" stop-opacity="0.55"/>
    <stop offset="0.55" stop-color="#2a3623" stop-opacity="0"/>
    <stop offset="1" stop-color="#14190f" stop-opacity="0.6"/>
  </radialGradient>
  <radialGradient id="goldR" cx="0.5" cy="0.4" r="0.7">
    <stop offset="0" stop-color="#f3dca6"/>
    <stop offset="0.6" stop-color="#d8b878"/>
    <stop offset="1" stop-color="#b8965d"/>
  </radialGradient>
  <linearGradient id="leafG" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#8a9c63"/>
    <stop offset="1" stop-color="#5d6e42"/>
  </linearGradient>
  <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.5 0"/></filter>
  <filter id="soft"><feGaussianBlur stdDeviation="0.6"/></filter>
  <g id="leaf"><path d="M0,0 C7,-9 8,-22 0,-32 C-8,-22 -7,-9 0,0 Z" fill="url(#leafG)" stroke="#46552f" stroke-width="0.8"/>
    <path d="M0,-2 L0,-28" stroke="#46552f" stroke-width="0.7" fill="none" opacity="0.7"/></g>
  <g id="blossom">
    <g fill="#efe9d6" stroke="#d8cba6" stroke-width="0.6">
      <ellipse cx="0" cy="-7" rx="4.2" ry="7"/>
      <ellipse cx="0" cy="-7" rx="4.2" ry="7" transform="rotate(72)"/>
      <ellipse cx="0" cy="-7" rx="4.2" ry="7" transform="rotate(144)"/>
      <ellipse cx="0" cy="-7" rx="4.2" ry="7" transform="rotate(216)"/>
      <ellipse cx="0" cy="-7" rx="4.2" ry="7" transform="rotate(288)"/>
    </g>
    <circle r="2.6" fill="#cB9d63"/>
  </g>
  <g id="bud"><circle r="3" fill="#e7dcc0" stroke="#cB9d63" stroke-width="0.6"/></g>
</defs>''')

# ---- background ----
parts.append(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
# plaster blotches lembut
for _ in range(7):
    cx=random.uniform(120,960); cy=random.uniform(300,1700)
    r=random.uniform(180,360); op=random.uniform(0.05,0.12)
    col=random.choice(['#46552f','#3f4e2c','#222d1a'])
    parts.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="{col}" opacity="{op:.2f}"/>')
parts.append(f'<rect width="{W}" height="{H}" fill="url(#vig)"/>')
parts.append(f'<rect width="{W}" height="{H}" filter="url(#grain)" opacity="0.05"/>')

# ---- vinasi bunga juntai ----
parts.append('<g id="vines">')
for x0,depth,sw in strands:
    segs=strand(x0,depth,sw)
    parts.append(f'<path d="{seg_path(segs)}" fill="none" stroke="#5d6e42" stroke-width="2.4" opacity="0.9"/>')
    parts.append(f'<path d="{seg_path(segs)}" fill="none" stroke="#7c8d57" stroke-width="1" opacity="0.8"/>')
    pts=sample(segs, step=23)
    for i,(px,py,ang,t) in enumerate(pts):
        sc=1.05-0.45*t  # mengecil ke ujung
        if i==0: continue
        side=1 if i%2==0 else -1
        if i%4==0:
            parts.append(f'<use href="#blossom" transform="translate({px:.1f},{py:.1f}) scale({0.95*sc:.2f})"/>')
        elif i%7==0:
            parts.append(f'<use href="#bud" transform="translate({px:.1f},{py:.1f}) scale({sc:.2f})"/>')
        else:
            rot=ang+90+side*52
            parts.append(f'<use href="#leaf" transform="translate({px:.1f},{py:.1f}) rotate({rot:.0f}) scale({sc:.2f})"/>')
    # bunga di ujung
    ex,ey,_,_=pts[-1]
    parts.append(f'<use href="#blossom" transform="translate({ex:.1f},{ey:.1f}) scale({1.15:.2f})"/>')
parts.append('</g>')

# ---- medali emas di puncak tengah: emblem dokter (hati+nadi) & guru (buku) ----
cx=540; top=212; ring=86
parts.append(f'<g id="crest">')
# tali gantung
parts.append(f'<path d="M540,46 C 536,120 544,150 540,{top-ring:.0f}" stroke="#caa766" stroke-width="1.6" fill="none" opacity="0.85"/>')
parts.append(f'<circle cx="540" cy="46" r="4" fill="url(#goldR)"/>')
# cincin medali
parts.append(f'<circle cx="{cx}" cy="{top}" r="{ring}" fill="#243019" stroke="url(#goldR)" stroke-width="3"/>')
parts.append(f'<circle cx="{cx}" cy="{top}" r="{ring-7}" fill="none" stroke="#caa766" stroke-width="1" opacity="0.7"/>')
# emblem dalam medali (koordinat lokal, geser ke pusat medali)
em=[]
g0=f'translate({cx},{top})'
# buku terbuka (guru) di bawah
em.append('<path d="M0,34 C-22,22 -44,24 -58,30 L-58,52 C-44,46 -22,44 0,54 Z" fill="none" stroke="url(#goldR)" stroke-width="2.4"/>')
em.append('<path d="M0,34 C22,22 44,24 58,30 L58,52 C44,46 22,44 0,54 Z" fill="none" stroke="url(#goldR)" stroke-width="2.4"/>')
em.append('<path d="M0,34 L0,54" stroke="#caa766" stroke-width="1.4"/>')
for dy in (32,38):  # garis halaman
    em.append(f'<path d="M-50,{dy} C-32,{dy-4} -14,{dy-4} -6,{dy-1}" stroke="#caa766" stroke-width="0.8" fill="none" opacity="0.6"/>')
    em.append(f'<path d="M50,{dy} C32,{dy-4} 14,{dy-4} 6,{dy-1}" stroke="#caa766" stroke-width="0.8" fill="none" opacity="0.6"/>')
# hati (dokter) di atas buku
em.append('<path d="M0,18 C-12,2 -34,-4 -34,-20 C-34,-32 -24,-39 -14,-39 C-7,-39 -2,-34 0,-28 C2,-34 7,-39 14,-39 C24,-39 34,-32 34,-20 C34,-4 12,2 0,18 Z" fill="none" stroke="url(#goldR)" stroke-width="2.6"/>')
# garis denyut nadi (EKG) menembus hati
em.append('<path d="M-30,-16 L-14,-16 L-8,-28 L0,-2 L6,-22 L11,-16 L30,-16" fill="none" stroke="#f3dca6" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/>')
parts.append(f'<g transform="{g0}">' + "".join(em) + '</g>')
# kilau bintang kecil
for sx,sy in [(cx-ring-6,top-30),(cx+ring+6,top+18),(cx,top-ring-10)]:
    parts.append(f'<path d="M{sx},{sy-5} L{sx+1.3},{sy-1.3} L{sx+5},{sy} L{sx+1.3},{sy+1.3} L{sx},{sy+5} L{sx-1.3},{sy+1.3} L{sx-5},{sy} L{sx-1.3},{sy-1.3} Z" fill="#e7d3a0" opacity="0.8"/>')
parts.append('</g>')

# ---- sprig emas kecil di sudut bawah ----
def sprig(x,y,flip):
    f=-1 if flip else 1
    g=[f'<g transform="translate({x},{y}) scale({f},1)">']
    g.append('<path d="M0,0 C30,-8 60,-30 84,-72" stroke="#caa766" stroke-width="1.6" fill="none" opacity="0.8"/>')
    for t in (0.2,0.45,0.7):
        bx=0+ (84)*t; by=0 - (0 if t<0 else 1)* (8*(t)+30*t*t+ ( -0)) # kira-kira sepanjang kurva
    # daun emas sederhana sepanjang kurva
    for px,py,rot in [(20,-7,40),(40,-20,55),(60,-40,70),(74,-58,80)]:
        g.append(f'<path d="M0,0 C5,-7 5,-16 0,-22 C-5,-16 -5,-7 0,0 Z" fill="none" stroke="#caa766" stroke-width="1.2" transform="translate({px},{py}) rotate({rot})" opacity="0.75"/>')
    g.append('</g>')
    return "".join(g)
parts.append(sprig(60, H-70, False))
parts.append(sprig(W-60, H-70, True))

parts.append('</svg>')

open('bg/bgcover.svg','w').write("\n".join(parts))
import os
print("bytes:", os.path.getsize('bg/bgcover.svg'))

FONT = "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Inter, Helvetica, Arial, sans-serif"
P = {
 "light": dict(bg="#FFFFFF", tile="#F5F5F7", title="#1D1D1F", text="#6E6E73", accent="#0071E3", blob=0.35, border="#E5E5EA"),
 "dark":  dict(bg="#000000", tile="#1C1C1E", title="#F5F5F7", text="#A1A1A6", accent="#2997FF", blob=0.55, border="#2C2C2E"),
}

def hero(m, c):
    blobs = [("#0071E3",150,80,"0 0;60 30;0 0"),("#8E5CF7",700,50,"0 0;-70 40;0 0"),
             ("#FF5FA2",580,300,"0 0;50 -40;0 0"),("#34C7F7",250,310,"0 0;-40 -30;0 0")]
    grads = "".join(f'<radialGradient id="g{i}"><stop offset="0" stop-color="{col}" stop-opacity="{c["blob"]}"/><stop offset="1" stop-color="{col}" stop-opacity="0"/></radialGradient>' for i,(col,_,_,_) in enumerate(blobs))
    b = "".join(f'<circle cx="{x}" cy="{y}" r="260" fill="url(#g{i})"><animateTransform attributeName="transform" type="translate" values="{v}" dur="14s" repeatCount="indefinite"/></circle>' for i,(_,x,y,v) in enumerate(blobs))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 300" width="840" height="300">
<defs><clipPath id="r"><rect width="840" height="300" rx="28"/></clipPath>{grads}</defs>
<g clip-path="url(#r)"><rect width="840" height="300" fill="{c["bg"]}"/>{b}</g>
<rect x="0.5" y="0.5" width="839" height="299" rx="27.5" fill="none" stroke="{c["border"]}"/>
<g font-family="{FONT}" text-anchor="middle">
<text x="420" y="112" font-size="14" font-weight="600" letter-spacing="3" fill="{c["accent"]}">QUALITY ENGINEERING</text>
<text x="420" y="172" font-size="54" font-weight="700" letter-spacing="-1" fill="{c["title"]}">Hej, I'm Damilare</text>
<text x="420" y="212" font-size="20" fill="{c["text"]}">Senior QA Engineer · Web, Mobile &amp; Embedded</text>
</g></svg>'''

def tile(x,y,w,h,label,head,body,c,hi=False):
    fill = "url(#g)" if hi else c["tile"]
    lc, hc, bc = ("#FFFFFF","#FFFFFF","#E8E8FF") if hi else (c["accent"],c["title"],c["text"])
    return f'''<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="24" fill="{fill}"/>
<text x="{x+28}" y="{y+44}" font-size="12" font-weight="600" letter-spacing="2" fill="{lc}" opacity="{0.85 if hi else 1}">{label}</text>
<text x="{x+28}" y="{y+h-62}" font-size="{30 if w>400 else 24}" font-weight="700" letter-spacing="-0.5" fill="{hc}">{head}</text>
<text x="{x+28}" y="{y+h-32}" font-size="16" fill="{bc}">{body}</text>'''

def bento(m, c):
    t = [tile(0,0,512,172,"NOW BUILDING","Scalable test frameworks","with Playwright &amp; .NET",c,True),
         tile(528,0,312,172,"CRAFT","Manual + Automation","Test strategy, end to end",c),
         tile(0,188,312,172,"MINDSET","Break it on purpose","So users never do",c),
         tile(328,188,512,172,"LET'S TALK","Software quality","Always learning, always up for a chat",c)]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 360" width="840" height="360">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0071E3"/><stop offset="1" stop-color="#8E5CF7"/></linearGradient></defs>
<g font-family="{FONT}">{"".join(t)}</g></svg>'''

def qcard(x, lines, who, c):
    ts = "".join(f'<text x="{x+32}" y="{100+i*28}" font-size="18" font-weight="500" fill="{c["title"]}">{l}</text>' for i,l in enumerate(lines))
    return f'''<rect x="{x}" y="0" width="412" height="220" rx="24" fill="{c["tile"]}"/>
<text x="{x+28}" y="72" font-size="64" font-weight="700" fill="{c["accent"]}">“</text>{ts}
<text x="{x+32}" y="190" font-size="15" fill="{c["text"]}">— {who}</text>'''

def quotes(m, c):
    a = qcard(0, ["Testing is the process of evaluating a","product by learning about it through","exploration and experimentation."], "Michael Bolton", c)
    b = qcard(428, ["A good tester is a detective,","not a robot."], "Jonathon Wright", c)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 220" width="840" height="220"><g font-family="{FONT}">{a}{b}</g></svg>'

for m,c in P.items():
    for name,fn in [("hero",hero),("about",bento),("quotes",quotes)]:
        open(f"{name}-{m}.svg","w").write(fn(m,c))

# ---- Extra tools not on skillicons.dev, drawn as Apple-style pills ----
EXTRAS = ["Testcontainers"]

def chips(m, c):
    x, parts = 0, []
    for name in EXTRAS:
        w = round(60 + len(name) * 8.5)
        parts.append(f'<rect x="{x}" y="0" width="{w}" height="44" rx="22" fill="{c["tile"]}" stroke="{c["border"]}"/>'
                     f'<circle cx="{x+22}" cy="22" r="5" fill="{c["accent"]}"/>'
                     f'<text x="{x+36}" y="28" font-size="16" font-weight="600" fill="{c["title"]}">{name}</text>')
        x += w + 12
    total = x - 12
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total} 44" width="{total}" height="44"><g font-family="{FONT}">{"".join(parts)}</g></svg>'

for m, c in P.items():
    open(f"chips-{m}.svg", "w").write(chips(m, c))

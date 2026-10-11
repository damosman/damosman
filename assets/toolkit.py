"""Builds toolkit-light.svg / toolkit-dark.svg: one row of skillicons-style tiles.
Run from this folder:  python toolkit.py
Tiles come from icons/ (skillicons.dev originals + custom Playwright/JMeter tiles)."""
import base64, re

# Order = how the row reads: languages, then testing, then DevOps.
# Each entry: (light file, dark file). Custom tiles use the special names "Playwright" and "JMeter".
ROW = [("Java-Light","Java-Dark"), ("CS","CS"), ("DotNet","DotNet"), ("TypeScript","TypeScript"),
       ("JavaScript","JavaScript"), ("Python-Light","Python-Dark"), ("Bash-Light","Bash-Dark"),
       ("Playwright","Playwright"), ("Selenium","Selenium"), ("JMeter","JMeter"), ("Postman","Postman"),
       ("GitLab-Light","GitLab-Dark"), ("Docker","Docker"), ("Jenkins-Light","Jenkins-Dark"),
       ("Kubernetes","Kubernetes")]

TILE_BG = {"light": "#F4F2ED", "dark": "#242938"}   # skillicons' own tile colours
SCALE = 48 / 256                                     # each tile shows at 48px, like skillicons

def custom(name, mode):
    bg = f'<rect width="256" height="256" rx="60" fill="{TILE_BG[mode]}"/>'
    if name == "Playwright":
        data = base64.b64encode(open("icons/Playwright.png", "rb").read()).decode()
        return f'<svg width="256" height="256" viewBox="0 0 256 256">{bg}<image x="18" y="18" width="220" height="220" href="data:image/png;base64,{data}"/></svg>'
    if name == "JMeter":
        leaf = open("icons/JMeter-Leaf.svg").read()
        leaf = re.sub(r'<\?xml[^>]*\?>', '', leaf)
        # Swap the leaf's own size for the box it should fill inside the tile.
        open_tag = re.search(r'<svg\b[^>]*>', leaf).group(0)
        new_tag = re.sub(r'\s(width|height)="[^"]*"', '', open_tag).replace('<svg', '<svg x="68" y="28" width="120" height="200"', 1)
        leaf = leaf.replace(open_tag, new_tag, 1)
        return f'<svg width="256" height="256" viewBox="0 0 256 256">{bg}{leaf}</svg>'

def tile(fname, mode, i):
    svg = custom(fname, mode) if fname in ("Playwright", "JMeter") else open(f"icons/{fname}.svg").read()
    # Give every id a unique prefix so gradients from different tiles don't clash.
    svg = re.sub(r'id="([^"]+)"', rf'id="t{i}_\1"', svg)
    svg = re.sub(r'url\(#([^)]+)\)', rf'url(#t{i}_\1)', svg)
    svg = re.sub(r'href="#([^"]+)"', rf'href="#t{i}_\1"', svg)
    return f'<g transform="translate({i*300},0)">{svg}</g>'

for mode in ("light", "dark"):
    n = len(ROW); w = n*300 - 44
    tiles = "".join(tile(pair[0 if mode == "light" else 1], mode, i) for i, pair in enumerate(ROW))
    out = (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
           f'width="{w*SCALE:.2f}" height="{256*SCALE:.2f}" viewBox="0 0 {w} 256" fill="none">{tiles}</svg>')
    open(f"toolkit-{mode}.svg", "w").write(out)
print("built", len(ROW), "tiles")

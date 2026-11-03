# Follows' marks: one geometry, drawn as SVG.
#   python3 source/marks.py   (needs fonttools and brotli: pip install fonttools brotli)
# Writes logos/ and favicons/ (SVG). The PNG icons are rendered from the
# favicon SVGs by source/png.sh.
#
# The mark is "the follow": a solid disc (you) leaning into a ring (the
# account you follow). The ring gives way where the disc meets it, a gap of
# GAP all round, so the two read as two accounts and one link between them.
import pathlib, sys
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ROOT)
FONT = ROOT / "fonts/schibsted-grotesk-latin.woff2"

INDIGO, INK, WHITE = "#3346d3", "#16181d", "#ffffff"
INDIGO_D, FOG = "#8d9bff", "#ecedf0"

# Master grid: the mark is 40 x 24.
H = 24.0            # mark height
D = H / 2           # disc radius: the unit of clear space ("one disc")
RING_W = 5.0        # ring stroke
GAP = 2.5           # disc-to-ring gap
DISC = (12.0, 12.0) # disc centre
RING = (28.0, 12.0) # ring centre
W = RING[0] + D     # 40

def f(v):
    return ("%.3f" % v).rstrip("0").rstrip(".")

def circle_path(cx, cy, r):
    return (f"M{f(cx - r)} {f(cy)}a{f(r)} {f(r)} 0 1 0 {f(2 * r)} 0"
            f"a{f(r)} {f(r)} 0 1 0 {f(-2 * r)} 0z")

def mark(disc, ring, dx=0.0, dy=0.0, s=1.0, uid="m", ring_w=RING_W):
    """The mark at (dx,dy), scale s. The ring is cut by a mask around the disc."""
    def C(c, r):
        return circle_path(dx + c[0] * s, dy + c[1] * s, r * s)
    annulus = C(RING, D) + C(RING, D - ring_w)
    cut = C(DISC, D + GAP)
    return (f'<mask id="{uid}" maskUnits="userSpaceOnUse">'
            f'<rect x="{f(dx - 1)}" y="{f(dy - 1)}" width="{f(W * s + 2)}" height="{f(H * s + 2)}" fill="#fff"/>'
            f'<path d="{cut}" fill="#000"/></mask>'
            f'<path d="{annulus}" fill="{ring}" fill-rule="evenodd" mask="url(#{uid})"/>'
            f'<path d="{C(DISC, D)}" fill="{disc}"/>')

def svg(w, h, body, title, x0=0.0, y0=0.0, px=None):
    pw, ph = px if px else (w, h)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{f(x0)} {f(y0)} {f(w)} {f(h)}" '
            f'width="{f(pw)}" height="{f(ph)}" role="img" aria-label="{title}"><title>{title}</title>{body}</svg>\n')

# The wordmark: Schibsted Grotesk at 800, outlined; cap height = mark height.
font = TTFont(str(FONT))
font = instantiateVariableFont(font, {"wght": 800})
gs, cmap, hmtx = font.getGlyphSet(), font.getBestCmap(), font["hmtx"]
CAP = font["OS/2"].sCapHeight
SC = H / CAP
TEXT = "Follows"
TRACK = -0.01 * font["head"].unitsPerEm   # -1% tracking, as the display styles

def word(x0, baseline, fill):
    pen = SVGPathPen(gs)
    x = 0.0
    for ch in TEXT:
        g = cmap[ord(ch)]
        gs[g].draw(TransformPen(pen, (SC, 0, 0, -SC, x0 + x * SC, baseline)))
        x += hmtx[g][0] + TRACK
    return f'<path fill="{fill}" d="{pen.getCommands()}"/>'

b = BoundsPen(gs)
x = 0.0
for ch in TEXT:
    g = cmap[ord(ch)]
    gs[g].draw(TransformPen(b, (1, 0, 0, 1, x, 0)))
    x += hmtx[g][0] + TRACK
XMIN, YMIN, XMAX, YMAX = b.bounds
WORD_W = (XMAX - XMIN) * SC
OVER_TOP = max(0.0, (YMAX - CAP) * SC)    # the "l"'s ascender above the cap line
UNDER = max(0.0, -YMIN * SC)              # overshoot below the baseline

def wordmark(fill):
    top, bottom = OVER_TOP, UNDER
    body = word(-XMIN * SC, H, fill)
    return svg(WORD_W, H + top + bottom, body, "Follows", 0, -top)

LOCK_GAP = D   # mark to wordmark: one disc
STACK = 1.75   # the stacked lockup's mark, against the cap height

def lockup(disc, ring, ink, uid):
    top, bottom = OVER_TOP, UNDER
    body = mark(disc, ring, uid=uid) + word(W + LOCK_GAP - XMIN * SC, H, ink)
    return svg(W + LOCK_GAP + WORD_W, H + top + bottom, body, "Follows", 0, -top)

def stacked(disc, ring, ink, uid):
    # the mark at STACK x the cap height, one disc above the word's cap line
    top = OVER_TOP
    width = max(W * STACK, WORD_W)
    mx = (width - W * STACK) / 2
    wx = (width - WORD_W) / 2
    base = H * STACK + D + top + H
    body = mark(disc, ring, dx=mx, s=STACK, uid=uid) + word(wx - XMIN * SC, base, ink)
    return svg(width, base + UNDER, body, "Follows")

def themed_lockup():
    # For inlining in a page: the disc takes the page's --accent and the ring
    # and wordmark its --ink, so it follows the page's theme; on its own the
    # fallbacks draw the two-tone lockup.
    top, bottom = OVER_TOP, UNDER
    body = ('<style>.follows-disc{fill:var(--accent,#3346d3)}.follows-ink{fill:var(--ink,#16181d)}</style>'
            + mark("DISC", "RING", uid="follows-lockup-mask")
            + word(W + LOCK_GAP - XMIN * SC, H, "WORD"))
    body = (body.replace('fill="RING"', 'class="follows-ink"').replace('fill="DISC"', 'class="follows-disc"')
                .replace('fill="WORD"', 'class="follows-ink"'))
    return svg(W + LOCK_GAP + WORD_W, H + top + bottom, body, "Follows", 0, -top)

def mark_svg(disc, ring, uid):
    return svg(W, H, mark(disc, ring, uid=uid), "Follows")

# Favicons and app icons: the mark in white on an indigo tile.
def tile(size, radius_ratio=0.22, mark_ratio=0.72, snap=False, ring_w=RING_W):
    s = size * mark_ratio / W
    mw, mh = W * s, H * s
    dx, dy = (size - mw) / 2, (size - mh) / 2
    if snap:
        dx, dy = round(dx), round(dy)
    r = size * radius_ratio
    body = (f'<rect width="{size}" height="{size}" rx="{f(r)}" fill="{INDIGO}"/>'
            + mark(WHITE, WHITE, dx=dx, dy=dy, s=s, uid=f"t{size}", ring_w=ring_w))
    return svg(size, size, body, "Follows")

def favicon_adaptive():
    # One SVG favicon that follows the browser's theme: indigo tile in both,
    # since a tab bar may be light or dark under either.
    return tile(32, mark_ratio=0.78, ring_w=6)

def write(rel, text):
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
    print(rel, len(text))

write("logos/follows-lockup.svg", lockup(INDIGO, INK, INK, "a"))
write("logos/follows-lockup-reversed.svg", lockup(INDIGO_D, FOG, FOG, "b"))
write("logos/follows-lockup-ink.svg", lockup(INK, INK, INK, "c"))
write("logos/follows-lockup-white.svg", lockup(WHITE, WHITE, WHITE, "d"))
write("logos/follows-lockup-stacked.svg", stacked(INDIGO, INK, INK, "e"))
write("logos/follows-lockup-stacked-reversed.svg", stacked(INDIGO_D, FOG, FOG, "f"))
write("logos/follows-lockup-themed.svg", themed_lockup())
write("logos/follows-wordmark.svg", wordmark(INK))
write("logos/follows-wordmark-reversed.svg", wordmark(FOG))
write("logos/follows-mark.svg", mark_svg(INDIGO, INK, "g"))
write("logos/follows-mark-reversed.svg", mark_svg(INDIGO_D, FOG, "h"))
write("logos/follows-mark-indigo.svg", mark_svg(INDIGO, INDIGO, "i"))
write("logos/follows-mark-ink.svg", mark_svg(INK, INK, "j"))
write("logos/follows-mark-white.svg", mark_svg(WHITE, WHITE, "k"))
write("favicons/favicon.svg", favicon_adaptive())
# At 32px and below the ring is drawn heavier (6 of 24) so it holds a pixel.
write("favicons/favicon-tile-16.svg", tile(16, radius_ratio=0.1875, mark_ratio=0.9, ring_w=6.5))
write("favicons/favicon-tile-32.svg", tile(32, mark_ratio=0.78, ring_w=6))
write("favicons/app-icon.svg", tile(512, radius_ratio=0.2237, mark_ratio=0.62))
print("word width", f(WORD_W), "over", f(OVER_TOP), "under", f(UNDER))

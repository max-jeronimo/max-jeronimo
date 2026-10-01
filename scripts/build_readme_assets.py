"""Generate the pixel-art SVG assets used by README.md.

Run:  python scripts/build_readme_assets.py

Everything is drawn from rectangles, including the text, so the images need
no fonts and render the same on github.com, the mobile app and in light or
dark theme. Edit the content tables near the bottom and re-run.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"

# --- palette ---------------------------------------------------------------
INK = "#1a1035"
PANEL = "#241547"
MID = "#3b1e6d"
PRIMARY = "#6d28d9"
BRIGHT = "#8b5cf6"
SOFT = "#C4B5FD"
PALE = "#E9D5FF"
WHITE = "#ffffff"
SHADOW = "#2e1065"
BOX = "#f8f5ff"
BOX_TEXT = "#2b2140"
BOX_SHADOW = "#cfc6e6"

# --- 5x7 pixel font ----------------------------------------------------------
FONT_SRC = r"""
A
.###.
#...#
#...#
#####
#...#
#...#
#...#

B
####.
#...#
#...#
####.
#...#
#...#
####.

C
.###.
#...#
#....
#....
#....
#...#
.###.

D
####.
#...#
#...#
#...#
#...#
#...#
####.

E
#####
#....
#....
####.
#....
#....
#####

F
#####
#....
#....
####.
#....
#....
#....

G
.###.
#...#
#....
#.###
#...#
#...#
.####

H
#...#
#...#
#...#
#####
#...#
#...#
#...#

I
###
.#.
.#.
.#.
.#.
.#.
###

J
..###
...#.
...#.
...#.
...#.
#..#.
.##..

K
#...#
#..#.
#.#..
##...
#.#..
#..#.
#...#

L
#....
#....
#....
#....
#....
#....
#####

M
#...#
##.##
#.#.#
#.#.#
#...#
#...#
#...#

N
#...#
#...#
##..#
#.#.#
#..##
#...#
#...#

O
.###.
#...#
#...#
#...#
#...#
#...#
.###.

P
####.
#...#
#...#
####.
#....
#....
#....

Q
.###.
#...#
#...#
#...#
#.#.#
#..#.
.##.#

R
####.
#...#
#...#
####.
#.#..
#..#.
#...#

S
.####
#....
#....
.###.
....#
....#
####.

T
#####
..#..
..#..
..#..
..#..
..#..
..#..

U
#...#
#...#
#...#
#...#
#...#
#...#
.###.

V
#...#
#...#
#...#
#...#
#...#
.#.#.
..#..

W
#...#
#...#
#...#
#.#.#
#.#.#
#.#.#
.#.#.

X
#...#
#...#
.#.#.
..#..
.#.#.
#...#
#...#

Y
#...#
#...#
.#.#.
..#..
..#..
..#..
..#..

Z
#####
....#
...#.
..#..
.#...
#....
#####

a
.....
.....
.###.
....#
.####
#...#
.####

b
#....
#....
#.##.
##..#
#...#
#...#
####.

c
.....
.....
.###.
#....
#....
#...#
.###.

d
....#
....#
.##.#
#..##
#...#
#...#
.####

e
.....
.....
.###.
#...#
#####
#....
.###.

f
..##.
.#..#
.#...
###..
.#...
.#...
.#...

g
.....
.....
.####
#...#
.####
....#
.###.

h
#....
#....
#.##.
##..#
#...#
#...#
#...#

i
.#.
...
##.
.#.
.#.
.#.
###

j
...#
....
..##
...#
...#
#..#
.##.

k
#...
#...
#..#
#.#.
##..
#.#.
#..#

l
##.
.#.
.#.
.#.
.#.
.#.
###

m
.....
.....
##.#.
#.#.#
#.#.#
#...#
#...#

n
.....
.....
#.##.
##..#
#...#
#...#
#...#

o
.....
.....
.###.
#...#
#...#
#...#
.###.

p
.....
.....
####.
#...#
####.
#....
#....

q
.....
.....
.##.#
#..##
.####
....#
....#

r
.....
.....
#.##.
##..#
#....
#....
#....

s
.....
.....
.###.
#....
.###.
....#
####.

t
.#...
.#...
###..
.#...
.#...
.#..#
..##.

u
.....
.....
#...#
#...#
#...#
#..##
.##.#

v
.....
.....
#...#
#...#
#...#
.#.#.
..#..

w
.....
.....
#...#
#...#
#.#.#
#.#.#
.#.#.

x
.....
.....
#...#
.#.#.
..#..
.#.#.
#...#

y
.....
.....
#...#
#...#
.####
....#
.###.

z
.....
.....
#####
...#.
..#..
.#...
#####

0
.###.
#...#
#..##
#.#.#
##..#
#...#
.###.

1
.#.
##.
.#.
.#.
.#.
.#.
###

2
.###.
#...#
....#
...#.
..#..
.#...
#####

3
#####
...#.
..#..
...#.
....#
#...#
.###.

4
...#.
..##.
.#.#.
#..#.
#####
...#.
...#.

5
#####
#....
####.
....#
....#
#...#
.###.

6
..##.
.#...
#....
####.
#...#
#...#
.###.

7
#####
....#
...#.
..#..
.#...
.#...
.#...

8
.###.
#...#
#...#
.###.
#...#
#...#
.###.

9
.###.
#...#
#...#
.####
....#
...#.
.##..

.
.
.
.
.
.
.
#

,
..
..
..
..
..
.#
#.

'
#
#
.
.
.
.
.

"
#.#
#.#
...
...
...
...
...

!
#
#
#
#
#
.
#

?
.###.
#...#
....#
...#.
..#..
.....
..#..

:
.
.
#
.
.
#
.

-
...
...
...
###
...
...
...

/
....#
....#
...#.
..#..
.#...
#....
#....

&
.##..
#..#.
#.#..
.#...
#.#.#
#..#.
.##.#

+
.....
..#..
..#..
#####
..#..
..#..
.....

(
..#
.#.
#..
#..
#..
.#.
..#

)
#..
.#.
..#
..#
..#
.#.
#..
"""

SPACE = 3  # width of a space, in font pixels


def parse_font(src):
    glyphs = {}
    for block in src.strip("\n").split("\n\n"):
        lines = block.split("\n")
        ch, rows = lines[0], lines[1:]
        assert len(rows) == 7, f"glyph {ch!r} has {len(rows)} rows"
        width = max(len(r) for r in rows)
        glyphs[ch] = [r.ljust(width, ".") for r in rows]
    return glyphs


FONT = parse_font(FONT_SRC)


def runs(rows, x, y, px):
    """Path data covering every '#' cell of a bitmap, merged into row runs."""
    d = []
    for j, row in enumerate(rows):
        i = 0
        while i < len(row):
            if row[i] != "#":
                i += 1
                continue
            k = i
            while k < len(row) and row[k] == "#":
                k += 1
            w = (k - i) * px
            d.append(f"M{x + i * px} {y + j * px}h{w}v{px}h-{w}z")
            i = k
    return "".join(d)


def text_width(s, px):
    cols = sum((SPACE if ch == " " else len(FONT[ch][0])) + 1 for ch in s) - 1
    return cols * px


class Canvas:
    """Collects SVG fragments for one image."""

    def __init__(self, w, h, label):
        self.w, self.h, self.label = w, h, label
        self.body = []
        self.ids = 0

    def add(self, fragment):
        self.body.append(fragment)

    def rect(self, x, y, w, h, fill, r=0, stroke=None, sw=0, extra=""):
        s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        rx = f' rx="{r}"' if r else ""
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}"{rx} fill="{fill}"{s}{extra}/>')

    def poly(self, points, fill, extra=""):
        pts = " ".join(f"{x},{y}" for x, y in points)
        self.add(f'<polygon points="{pts}" fill="{fill}"{extra}/>')

    def bitmap(self, rows, x, y, px, fill, extra=""):
        self.add(f'<path fill="{fill}" d="{runs(rows, x, y, px)}"{extra}/>')

    def text(self, s, x, y, px, fill, shadow=None, anchor="start"):
        """Draw a string; returns the x coordinate where it ends."""
        w = text_width(s, px)
        if anchor == "end":
            x -= w
        elif anchor == "middle":
            x -= w // 2
        d, cx = [], x
        for ch in s:
            if ch == " ":
                cx += (SPACE + 1) * px
                continue
            g = FONT[ch]
            d.append(runs(g, cx, y, px))
            cx += (len(g[0]) + 1) * px
        d = "".join(d)
        if shadow:
            self.ids += 1
            tid = f"t{self.ids}"
            self.add(f'<defs><path id="{tid}" d="{d}"/></defs>'
                     f'<use href="#{tid}" x="{px}" y="{px}" fill="{shadow}"/>'
                     f'<use href="#{tid}" fill="{fill}"/>')
        else:
            self.add(f'<path fill="{fill}" d="{d}"/>')
        return x + w

    def save(self, name):
        label = self.label.replace("&", "&amp;").replace('"', "&quot;")
        svg = (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
            f'width="{self.w}" height="{self.h}" shape-rendering="crispEdges" role="img" '
            f'aria-label="{label}"><title>{label}</title>{DEFS}{"".join(self.body)}</svg>\n'
        )
        (OUT / name).write_text(svg, encoding="utf-8")
        return len(svg)


DEFS = (
    "<defs>"
    '<pattern id="st" width="16" height="16" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)">'
    '<rect width="8" height="16" fill="#fff" opacity=".045"/></pattern>'
    f'<linearGradient id="gb" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{PRIMARY}"/>'
    f'<stop offset="1" stop-color="{BRIGHT}"/></linearGradient>'
    f'<linearGradient id="gt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{BRIGHT}"/>'
    '<stop offset="1" stop-color="#5b21b6"/></linearGradient>'
    '<linearGradient id="gs" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a78bfa"/>'
    f'<stop offset="1" stop-color="{PRIMARY}"/></linearGradient>'
    f'<linearGradient id="gp" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{MID}"/>'
    f'<stop offset="1" stop-color="{INK}"/></linearGradient>'
    "</defs>"
    "<style>"
    ".blink{animation:blink 1.1s steps(1) infinite}"
    ".bob{animation:bob .9s steps(1) infinite}"
    "@keyframes blink{50%{opacity:0}}"
    "@keyframes bob{50%{transform:translateY(4px)}}"
    "@media (prefers-reduced-motion:reduce){.blink,.bob{animation:none}}"
    "</style>"
)

# --- icons (12x12) -----------------------------------------------------------
ICONS = {
    "person": [
        "....####....",
        "...######...",
        "...######...",
        "...######...",
        "....####....",
        "............",
        "..########..",
        ".##########.",
        "############",
        "############",
        "############",
        "############",
    ],
    "bag": [
        "....####....",
        "...##..##...",
        "...#....#...",
        ".##########.",
        "############",
        "############",
        "#####..#####",
        "#####..#####",
        "############",
        "############",
        "############",
        ".##########.",
    ],
    "dex": [
        "############",
        "#..........#",
        "#.###......#",
        "#.###..###.#",
        "#.###......#",
        "#..........#",
        "############",
        "#..........#",
        "#.########.#",
        "#..........#",
        "#.#####....#",
        "############",
    ],
    "orb": [
        "....####....",
        "..########..",
        ".##########.",
        ".####..####.",
        "####....####",
        "###......###",
        "###......###",
        "####....####",
        ".####..####.",
        ".##########.",
        "..########..",
        "....####....",
    ],
    "case": [
        "....####....",
        "...##..##...",
        "############",
        "############",
        "############",
        "............",
        "#####..#####",
        "############",
        "############",
        "############",
        "############",
        "............",
    ],
    "badge": [
        ".....##.....",
        "...######...",
        ".##########.",
        "###..##..###",
        "##...##...##",
        "##.######.##",
        "##.######.##",
        "##...##...##",
        "###..##..###",
        ".##########.",
        "...######...",
        ".....##.....",
    ],
    "stats": [
        ".........###",
        ".........###",
        ".....###.###",
        ".....###.###",
        ".....###.###",
        ".###.###.###",
        ".###.###.###",
        ".###.###.###",
        ".###.###.###",
        ".###.###.###",
        "............",
        "############",
    ],
    "mail": [
        "............",
        "############",
        "##........##",
        "#.#......#.#",
        "#..#....#..#",
        "#...#..#...#",
        "#....##....#",
        "#..........#",
        "#..........#",
        "#..........#",
        "############",
        "............",
    ],
    "grid": [
        "###.###.###.",
        "###.###.###.",
        "###.###.###.",
        "............",
        "###.###.###.",
        "###.###.###.",
        "###.###.###.",
        "............",
        "###.###.###.",
        "###.###.###.",
        "###.###.###.",
        "............",
    ],
    "target": [
        "....####....",
        "..##....##..",
        ".#........#.",
        ".#..####..#.",
        "#..#....#..#",
        "#..#.##.#..#",
        "#..#.##.#..#",
        "#..#....#..#",
        ".#..####..#.",
        ".#........#.",
        "..##....##..",
        "....####....",
    ],
}

GEMS = [
    [
        ".....##.....",
        "....####....",
        "...######...",
        "..########..",
        ".##########.",
        "############",
        "############",
        ".##########.",
        "..########..",
        "...######...",
        "....####....",
        ".....##.....",
    ],
    [
        "...######...",
        "..########..",
        ".##########.",
        "############",
        "############",
        "############",
        "############",
        "############",
        "############",
        ".##########.",
        "..########..",
        "...######...",
    ],
    [
        ".....##.....",
        ".....##.....",
        "....####....",
        "....####....",
        "..########..",
        "############",
        "############",
        "..########..",
        "....####....",
        "....####....",
        ".....##.....",
        ".....##.....",
    ],
    [
        "############",
        "############",
        "############",
        "############",
        "############",
        "############",
        ".##########.",
        ".##########.",
        "..########..",
        "...######...",
        "....####....",
        ".....##.....",
    ],
]
GEM_COLORS = ["#8b5cf6", "#c084fc", "#818cf8", "#e879f9", "#a78bfa", "#60a5fa", "#f0abfc", "#C4B5FD"]

# Trainer silhouette: cap rows first, then head and shoulders.
CAP = [
    "......########......",
    ".....##########.....",
    "....############....",
    "....############....",
    "....###############.",
    "....################",
]
BUST = [
    "....############....",
    "....############....",
    "....############....",
    ".....##########.....",
    "......########......",
    ".......######.......",
    ".......######.......",
    ".....##########.....",
    "...##############...",
    "..################..",
    ".##################.",
    "####################",
    "####################",
    "####################",
    "####################",
    "####################",
]

ARROW_DOWN = ["#######", ".#####.", "..###..", "...#..."]


# --- images ------------------------------------------------------------------
def slashes(c, x, top, bottom, lean, fill=BRIGHT):
    """The two thin diagonal bars that trail a Gen 5 banner."""
    c.poly([(x + 16, top), (x + 36, top), (x + 36 - lean, bottom), (x + 16 - lean, bottom)], fill, ' opacity=".6"')
    c.poly([(x + 52, top), (x + 64, top), (x + 64 - lean, bottom), (x + 52 - lean, bottom)], fill, ' opacity=".35"')


def trainer_card():
    W, H = 840, 400
    c = Canvas(W, H, "Trainer card: Maxwell Jeronimo, AI Engineer and Full-Stack Developer, WPI, Swansea MA")
    c.add('<clipPath id="cc"><rect x="4" y="4" width="832" height="392" rx="16"/></clipPath>')
    c.rect(4, 4, 832, 392, INK, r=16)
    c.rect(4, 4, 832, 392, "url(#st)", r=16)
    c.add('<g clip-path="url(#cc)">')
    c.poly([(0, 0), (440, 0), (400, 68), (0, 68)], "url(#gb)")
    slashes(c, 440, 0, 68, 40)
    c.add("</g>")
    c.rect(4, 4, 832, 392, "none", r=16, stroke=BRIGHT, sw=4)
    c.rect(12, 12, 816, 376, "none", r=10, stroke=MID, sw=2)
    c.text("TRAINER CARD", 32, 22, 4, WHITE, shadow=SHADOW)
    c.text("ID. max-jeronimo", 808, 26, 3, SOFT, anchor="end")

    rows = [
        ("NAME", "Maxwell Jeronimo"),
        ("CLASS", "AI Engineer / Full-Stack Dev"),
        ("SCHOOL", "WPI - B.S. CS / M.S. AI"),
        ("LOCATION", "Swansea, MA"),
    ]
    for i, (label, value) in enumerate(rows):
        y = 88 + i * 52
        c.rect(32, y, 624, 44, PANEL, r=6)
        c.rect(32, y, 164, 44, MID, r=6)
        c.text(label, 44, y + 12, 3, SOFT)
        end = c.text(value, 204, y + 12, 3, WHITE, shadow=INK)
        assert end <= 650, f"{value!r} overflows its row ({end})"

    # portrait
    c.add('<clipPath id="pc"><rect x="672" y="88" width="136" height="200" rx="8"/></clipPath>')
    c.rect(672, 88, 136, 200, "url(#gp)", r=8)
    c.add('<g clip-path="url(#pc)">')
    c.rect(672, 88, 136, 200, "url(#st)")
    px = 6
    top = 288 - (len(CAP) + len(BUST)) * px
    c.bitmap(CAP, 680, top, px, BRIGHT)
    c.bitmap(BUST, 680, top + len(CAP) * px, px, SOFT)
    c.add("</g>")
    c.rect(672, 88, 136, 200, "none", r=8, stroke=SOFT, sw=3)

    # badge case
    c.rect(32, 304, 776, 72, PANEL, r=8)
    c.text("BADGES", 48, 330, 3, SOFT)
    for i in range(8):
        x = 196 + i * 76
        c.rect(x, 312, 56, 56, INK, r=28, stroke=MID, sw=2)
        c.bitmap(GEMS[i % 4], x + 10, 322, 3, GEM_COLORS[i])
        c.rect(x + 22, 334, 6, 3, WHITE, extra=' opacity=".55"')
        c.rect(x + 22, 337, 3, 3, WHITE, extra=' opacity=".55"')
    return c.save("trainer-card.svg")


def menu_tile(slug, label, icon, selected=False):
    c = Canvas(200, 80, label)
    c.rect(4, 10, 192, 66, "#120a26", r=14, extra=' opacity=".55"')
    c.rect(4, 4, 192, 66, "url(#gs)" if selected else "url(#gt)", r=14)
    c.rect(8, 8, 184, 28, WHITE, r=10, extra=' opacity=".13"')
    c.rect(4, 4, 192, 66, "none", r=14, stroke="#a78bfa", sw=3)
    if selected:
        c.rect(4, 4, 192, 66, "none", r=14, stroke=WHITE, sw=3, extra=' class="blink"')
    c.bitmap(ICONS[icon], 14, 19, 3, WHITE)
    end = c.text(label, 58, 27, 3, WHITE, shadow=SHADOW)
    assert end <= 188, f"{label!r} overflows its tile ({end})"
    return c.save(f"menu-{slug}.svg")


def header(slug, title, tag, icon):
    W, H = 840, 64
    c = Canvas(W, H, title)
    c.add(f'<clipPath id="hc"><rect x="0" y="6" width="{W}" height="52" rx="10"/></clipPath>')
    c.rect(0, 6, W, 52, INK, r=10)
    c.rect(0, 6, W, 52, "url(#st)", r=10)
    edge = 64 + text_width(title, 3) + 56
    c.add('<g clip-path="url(#hc)">')
    c.poly([(0, 6), (edge, 6), (edge - 30, 58), (0, 58)], "url(#gb)")
    slashes(c, edge, 6, 58, 30)
    c.add("</g>")
    c.bitmap(ICONS[icon], 16, 14, 3, WHITE)
    c.text(title, 64, 22, 3, WHITE, shadow=SHADOW)
    start = 820 - text_width(tag, 2)
    assert start > edge + 72, f"{title!r} collides with its tag"
    c.text(tag, 820, 25, 2, SOFT, anchor="end")
    return c.save(f"header-{slug}.svg")


def party_slot(slug, name, sub, tag):
    W, H = 760, 80
    c = Canvas(W, H, f"{name} ({sub})")
    c.rect(2, 8, 756, 70, "#120a26", r=12, extra=' opacity=".55"')
    c.rect(2, 2, 756, 70, "url(#gp)", r=12)
    c.rect(2, 2, 756, 70, "url(#st)", r=12)
    c.rect(2, 2, 756, 70, "none", r=12, stroke=BRIGHT, sw=3)
    c.bitmap(ICONS["orb"], 16, 13, 4, SOFT)
    end = c.text(name, 80, 14, 3, WHITE, shadow="#120a26")
    c.text(sub, 80, 46, 2, SOFT)
    tw = text_width(tag, 3)
    px0 = W - 18 - tw - 28
    assert end < px0 - 12, f"{name!r} collides with its tag"
    c.rect(px0, 20, tw + 28, 34, BRIGHT, r=17)
    c.text(tag, px0 + 14, 27, 3, WHITE, shadow=SHADOW)
    return c.save(f"party-{slug}.svg")


def dialog(lines):
    W, H = 840, 168
    c = Canvas(W, H, " ".join(lines))
    c.rect(4, 4, 832, 160, BOX, r=14, stroke=MID, sw=4)
    c.rect(12, 12, 816, 144, "none", r=8, stroke=SOFT, sw=4)
    for i, line in enumerate(lines):
        end = c.text(line, 40, 36 + i * 36, 3, BOX_TEXT, shadow=BOX_SHADOW)
        assert end <= 770, f"{line!r} overflows the dialog ({end})"
    c.bitmap(ARROW_DOWN, 780, 124, 3, PRIMARY, ' class="bob"')
    return c.save("dialog-quote.svg")


def footer():
    W, H = 840, 40
    c = Canvas(W, H, "")
    c.add(f'<clipPath id="fc"><rect x="0" y="4" width="{W}" height="32" rx="10"/></clipPath>')
    c.rect(0, 4, W, 32, INK, r=10)
    c.rect(0, 4, W, 32, "url(#st)", r=10)
    c.add('<g clip-path="url(#fc)">')
    c.poly([(0, 4), (300, 4), (280, 36), (0, 36)], "url(#gb)")
    slashes(c, 300, 4, 36, 20)
    c.add(f'<g transform="translate({W} 0) scale(-1 1)">')
    c.poly([(0, 4), (300, 4), (280, 36), (0, 36)], "url(#gb)")
    slashes(c, 300, 4, 36, 20)
    c.add("</g></g>")
    c.bitmap(ICONS["orb"], 408, 8, 2, SOFT)
    return c.save("footer.svg")


# --- content -----------------------------------------------------------------
MENU = [
    ("about", "ABOUT", "person"),
    ("tech", "BAG", "bag"),
    ("ai", "DEX", "dex"),
    ("projects", "PARTY", "orb"),
    ("experience", "CAREER", "case"),
    ("achievements", "BADGES", "badge"),
    ("stats", "STATS", "stats"),
    ("connect", "CONNECT", "mail"),
]

HEADERS = [
    ("about", "ABOUT ME", "TRAINER INFO", "person"),
    ("tech", "TECH STACK", "BAG", "bag"),
    ("ai", "AI / ML FOCUS", "DEX", "dex"),
    ("projects", "FEATURED PROJECTS", "PARTY", "orb"),
    ("experience", "EXPERIENCE", "CAREER", "case"),
    ("achievements", "ACHIEVEMENTS & ACTIVITIES", "BADGE CASE", "badge"),
    ("stats", "GITHUB ANALYTICS", "RECORDS", "stats"),
    ("activity", "CONTRIBUTION ACTIVITY", "ADVENTURE LOG", "grid"),
    ("focus", "CURRENT FOCUS", "QUEST", "target"),
    ("connect", "CONNECT", "LINK", "mail"),
]

PARTY = [
    ("workflow-agent", "Integrated Workflow Agent", "Apr. 2026 - Present", "AGENT"),
    ("curriculumgpt", "CurriculumGPT v2.0", "RAG/GraphRAG Research - May 2026 - Present", "RAG"),
    ("mgb", "Mass General Brigham Application", "Mar. 2025 - May 2025", "WEB"),
]

QUOTE = [
    "\"Build things that'll give you back time,",
    "as time is the most precious thing",
    "you will have ever.\"",
]


def main():
    OUT.mkdir(exist_ok=True)
    sizes = {"trainer-card.svg": trainer_card(), "dialog-quote.svg": dialog(QUOTE), "footer.svg": footer()}
    for i, (slug, label, icon) in enumerate(MENU):
        sizes[f"menu-{slug}.svg"] = menu_tile(slug, label, icon, selected=i == 0)
    for slug, title, tag, icon in HEADERS:
        sizes[f"header-{slug}.svg"] = header(slug, title, tag, icon)
    for slug, name, sub, tag in PARTY:
        sizes[f"party-{slug}.svg"] = party_slot(slug, name, sub, tag)
    for name, size in sizes.items():
        print(f"{size / 1024:6.1f} KB  {name}")


if __name__ == "__main__":
    main()

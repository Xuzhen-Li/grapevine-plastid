# Draws the two schematic guide figures (03 and 04) for docs/figures/guide/.
# Deterministic: the same Pillow version and DejaVu fonts give the same PNG bytes.
# Usage: python3 make_guide_figures.py OUTDIR   (licence: MIT, see LICENSE)
# Print size: each figure is 1600 px wide and is meant to be printed 183 mm wide (222 dpi,
# stored in the PNG). Smallest text is 20 px = 6.5 pt at that width.
# The script stops if a text is smaller than 20 px, leaves its frame, or has a contrast
# below 4.5:1 against any background colour behind it.
# All shapes are schematic. The real numbers are the Vitis plastome region lengths and the
# count of 113 unique genes from Jansen et al. 2006 (doi:10.1186/1471-2148-6-32).
import sys, os, math
from PIL import Image, ImageDraw, ImageFont
OUT = sys.argv[1]
F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
MIN_PX = 20
DPI = (222, 222)
def font(s, b=False): return ImageFont.truetype(FB if b else F, s)
GREY = "#555555"
C_LSC, C_IR, C_SSC = "#3f6c9f", "#b34e0b", "#2f7d32"
C_MT, C_PT, C_NUC = "#9a5f8c", "#2f7d32", "#f2f2f2"

def lum(rgb):
    def lin(c):
        c /= 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * lin(rgb[0]) + 0.7152 * lin(rgb[1]) + 0.0722 * lin(rgb[2])
def contrast(a, b):
    la, lb = lum(a), lum(b)
    if la < lb: la, lb = lb, la
    return (la + 0.05) / (lb + 0.05)
def rgb(h):
    if isinstance(h, tuple): return h
    h = h.lstrip("#")
    if h in ("white", "black"): return (255, 255, 255) if h == "white" else (0, 0, 0)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
def rgbn(n): return {"white": (255, 255, 255), "black": (0, 0, 0)}.get(n) or rgb(n)

class Fig:
    def __init__(self, W, H):
        self.W, self.H = W, H
        self.im = Image.new("RGB", (W, H), "white"); self.d = ImageDraw.Draw(self.im)
        self.frame = (20, 20, W - 20, H - 20)
    def T(self, xy, s, size, bold=False, fill="black", anchor="la"):
        assert size >= MIN_PX, (s, size)
        f = font(size, bold)
        bb = self.d.textbbox(xy, s, font=f, anchor=anchor)
        fx0, fy0, fx1, fy1 = self.frame
        assert bb[0] >= fx0 and bb[1] >= fy0 and bb[2] <= fx1 and bb[3] <= fy1, ("outside frame", s, bb, self.frame)
        crop = self.im.crop(bb); n = crop.width * crop.height
        for cnt, col in crop.getcolors(maxcolors=10 ** 6):
            if cnt >= 0.02 * n:
                assert contrast(rgbn(fill), col) >= 4.5, ("contrast", s, fill, col, contrast(rgbn(fill), col))
        self.d.text(xy, s, font=f, fill=fill, anchor=anchor)
        return bb
    def save(self, name):
        p = os.path.join(OUT, name)
        if os.path.exists(p): raise SystemExit("exists " + p)
        self.im.save(p, optimize=False, dpi=DPI); print(p)

def ring(d, cx, cy, r, w, segs):
    # segs: (start_deg, end_deg, colour); Pillow angles: 0 = 3 oclock, clockwise
    bb = [cx - r, cy - r, cx + r, cy + r]
    for a0, a1, c in segs:
        d.arc(bb, a0, a1, fill=c, width=w)
def pol(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arrow(d, p0, p1, col="black", w=4, head=14):
    d.line([p0, p1], fill=col, width=w)
    a = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    for s in (-0.45, 0.45):
        q = (p1[0] - head * math.cos(a + s), p1[1] - head * math.sin(a + s))
        d.line([p1, q], fill=col, width=w)

# ---------------- Figure 3: concepts ----------------
g = Fig(1600, 1480); d = g.d
g.T((40, 22), "Organelle genome concepts on one page (schematic)", 36, True)
g.T((40, 72), "Shapes are not to scale. The real data are the plastome region lengths and the gene count", 22, False, GREY)
g.T((40, 100), "in panel A (Vitis vinifera, Jansen et al. 2006).", 22, False, GREY)
PX, PY, PW, PH = 40, 145, 730, 700
QX = PX + PW + 60
def panel(x, y, w, h, tag, title):
    d.rounded_rectangle([x, y, x + w, y + h], radius=14, outline="#999999", width=2)
    g.frame = (x + 16, y + 16, x + w - 16, y + h - 16)
    g.T((x + 18, y + 12), tag, 32, True)
    g.T((x + 64, y + 18), title, 24, True)

panel(PX, PY, PW, PH, "A", "Plastome: four parts, IR boundaries")
tot = 160928.0
a = -90.0; segs = []
for name, ln, c in (("LSC", 89147, C_LSC), ("IRb", 26358, C_IR), ("SSC", 19065, C_SSC), ("IRa", 26358, C_IR)):
    span = 360.0 * ln / tot; segs.append((a, a + span, c, name, ln)); a += span
cx, cy, r = PX + PW // 2, PY + 300, 150
ring(d, cx, cy, r, 34, [(s[0], s[1], s[2]) for s in segs])
for s in segs:
    p0 = pol(cx, cy, r - 24, s[0]); p1 = pol(cx, cy, r + 24, s[0])
    d.line([p0, p1], fill="black", width=3)
for s in segs:
    mid = (s[0] + s[1]) / 2
    x, y = pol(cx, cy, r + 66, mid)
    g.T((x, y - 13), s[3], 24, True, s[2], "mm")
    g.T((x, y + 15), "{:,} bp".format(s[4]), 20, False, GREY, "mm")
g.T((cx, cy - 34), "160,928 bp", 28, True, "black", "mm")
g.T((cx, cy), "Vitis vinifera", 22, False, GREY, "mm")
g.T((cx, cy + 30), "113 unique genes", 20, False, GREY, "mm")
nx = PX + 28; ny = PY + 530
g.T((nx, ny), "Black ticks mark the four IR / single-copy junctions.", 22)
g.T((nx, ny + 44), "IR shift: a junction moves.", 22, True, C_IR)
g.T((nx, ny + 76), "A gene near it then changes between two copies (IR)", 22)
g.T((nx, ny + 106), "and one copy (LSC or SSC).", 22)

panel(QX, PY, PW, PH, "B", "Plant mitogenome: repeats, recombination")
bx, by, br = QX + 135, PY + 300, 100
d.ellipse([bx - br, by - br, bx + br, by + br], outline=C_MT, width=10)
for ang in (-90, 90):
    x, y = pol(bx, by, br, ang)
    d.rectangle([x - 10, y - 10, x + 10, y + 10], fill="black")
g.T((bx, by - 16), "master circle", 22, True, "black", "mm")
g.T((bx, by + 16), "(one view)", 20, False, GREY, "mm")
g.T((bx, by - br - 32), "repeat R1", 22, False, "black", "mm")
g.T((bx, by + br + 32), "repeat R2", 22, False, "black", "mm")
ax0 = bx + br + 28
arrow(d, (ax0, by), (ax0 + 90, by), w=5)
g.T((ax0 + 45, by - 62), "recombination", 22, False, "black", "mm")
g.T((ax0 + 45, by - 34), "at R1 / R2", 22, False, "black", "mm")
for (qx, qy, qr, lab) in ((QX + 470, PY + 235, 60, "sub-circle 1"), (QX + 470, PY + 375, 46, "sub-circle 2")):
    d.ellipse([qx - qr, qy - qr, qx + qr, qy + qr], outline=C_MT, width=9)
    x, y = pol(qx, qy, qr, 90); d.rectangle([x - 8, y - 8, x + 8, y + 8], fill="black")
    g.T((qx + qr + 14, qy), lab, 22, False, "black", "lm")
g.T((QX + 28, PY + 560), "Alternative arrangements (isoforms) and sub-circles", 22)
g.T((QX + 28, PY + 592), "can all be present in one individual.", 22)

CY = PY + PH + 30; CH = 570
panel(PX, CY, PW, CH, "C", "NUPT and NUMT: organelle DNA in the nucleus")
d.rounded_rectangle([PX + 300, CY + 90, PX + 690, CY + 350], radius=30, fill=C_NUC, outline="#777777", width=3)
g.T((PX + 495, CY + 120), "nucleus", 24, True, "black", "mm")
for yy in (185, 235, 285):
    d.rounded_rectangle([PX + 325, CY + yy, PX + 665, CY + yy + 18], radius=9, fill="#cfcfcf", outline="#888888")
d.rectangle([PX + 410, CY + 185, PX + 440, CY + 203], fill=C_PT)
d.rectangle([PX + 555, CY + 235, PX + 585, CY + 253], fill=C_MT)
d.rectangle([PX + 485, CY + 285, PX + 501, CY + 303], fill=C_PT)
d.ellipse([PX + 40, CY + 100, PX + 180, CY + 240], outline=C_PT, width=9)
g.T((PX + 110, CY + 170), "plastid", 22, True, "black", "mm")
d.ellipse([PX + 40, CY + 290, PX + 180, CY + 430], outline=C_MT, width=9)
g.T((PX + 110, CY + 345), "mito-", 22, True, "black", "mm")
g.T((PX + 110, CY + 375), "chondrion", 20, True, "black", "mm")
arrow(d, (PX + 188, CY + 170), (PX + 295, CY + 185), col=C_PT, w=4)
arrow(d, (PX + 188, CY + 360), (PX + 295, CY + 285), col=C_MT, w=4)
d.rectangle([PX + 300, CY + 385, PX + 325, CY + 405], fill=C_PT); g.T((PX + 337, CY + 395), "NUPT (plastid origin)", 22, False, "black", "lm")
d.rectangle([PX + 300, CY + 425, PX + 325, CY + 445], fill=C_MT); g.T((PX + 337, CY + 435), "NUMT (mitochondrial origin)", 22, False, "black", "lm")
g.T((PX + 28, CY + 485), "Reads from such segments can map to,", 20, False, GREY)
g.T((PX + 28, CY + 513), "or assemble with, the organelle genomes.", 20, False, GREY)

panel(QX, CY, PW, CH, "D", "RNA editing and heteroplasmy")
x0 = QX + 28; y1 = CY + 90
g.T((x0, y1), "DNA", 24, True)
g.T((x0 + 110, y1 - 2), "5  A  C  G  3", 28)
arrow(d, (x0 + 200, y1 + 44), (x0 + 200, y1 + 98), w=4)
g.T((x0 + 216, y1 + 56), "transcription", 20, False, GREY)
g.T((x0, y1 + 108), "RNA", 24, True)
g.T((x0 + 110, y1 + 106), "5  A  U  G  3", 28)
g.T((x0, y1 + 160), "C-to-U edit: here it makes AUG", 22, True, C_IR)
g.T((x0, y1 + 198), "The edit is made on the RNA. The DNA keeps C,", 20, False, GREY)
g.T((x0, y1 + 226), "so RNA-seq is needed to find it.", 20, False, GREY)
g.T((x0, y1 + 285), "Heteroplasmy", 24, True)
d.rectangle([x0, y1 + 325, x0 + 400, y1 + 369], fill=C_LSC); d.rectangle([x0 + 400, y1 + 325, x0 + 600, y1 + 369], fill=C_IR)
g.T((x0 + 200, y1 + 347), "haplotype 1", 22, True, "white", "mm")
g.T((x0 + 500, y1 + 347), "haplotype 2", 22, True, "white", "mm")
g.T((x0, y1 + 385), "Two organelle sequence variants in one individual;", 20, False, GREY)
g.T((x0, y1 + 413), "the shares here are illustrative.", 20, False, GREY)
g.save("03_organelle_concepts_schematic.png")

# ---------------- Figure 4: reference route ----------------
g = Fig(1600, 1040); d = g.d
g.T((40, 22), "Reference route for an organelle genome project (eight steps)", 36, True)
g.T((40, 72), "Tools named here are examples with a paper or repository listed in the knowledge map;", 22, False, GREY)
g.T((40, 100), "the order is a guide, not a fixed pipeline.", 22, False, GREY)
steps = [
 ("1", "Data and question", ["short reads, HiFi or ONT", "RNA-seq if editing matters", "plastome, mitogenome", "or both"], "#dce6f2"),
 ("2", "Plastome assembly", ["GetOrganelle", "NOVOPlasty", "ptGAUL (long reads)"], "#dce6f2"),
 ("3", "Mitogenome assembly", ["Oatk, PMAT, TIPPo, HiMT", "GetOrganelle (short reads)", "MitoHiFi (finish a contig)"], "#e8dcef"),
 ("4", "Check the graph", ["Bandage", "SAGBAC, GSAT", "keep alternative forms"], "#e8dcef"),
 ("5", "Annotate", ["plastome: GeSeq, PGA", "mitogenome: PMGA, MFannot", "also CPGAVAS2, AGORA"], "#dcefdc"),
 ("6", "Maps and IR junctions", ["OGDRAW, Chloroplot", "IRscope, CPGView", "compare with Vitis genomes"], "#dcefdc"),
 ("7", "Nuclear insertions", ["BLASTN against the nucleus", "Chlomito, ODNA", "label NUPT and NUMT"], "#fbe8d4"),
 ("8", "RNA editing and heteroplasmy", ["REDO, RES-Scanner", "REDItools, PREP suite", "Deepred-Mt, PREPACT", "NOVOPlasty, Oatk variants"], "#fbe8d4"),
]
bw, bh, step = 360, 340, 400
xs = [40 + i * step for i in range(4)]
def wrap(s, f, maxw):
    words = s.split(); out = []; cur = ""
    for w in words:
        t = (cur + " " + w).strip()
        if f.getlength(t) <= maxw: cur = t
        else: out.append(cur); cur = w
    out.append(cur); return out
for i, (n, t, lines, col) in enumerate(steps):
    x = xs[i % 4]; y = 135 + (i // 4) * 450
    d.rounded_rectangle([x, y, x + bw, y + bh], radius=16, fill=col, outline="black", width=2)
    g.frame = (x + 6, y + 6, x + bw - 6, y + bh - 6)
    d.ellipse([x + 14, y + 14, x + 62, y + 62], fill="black")
    g.T((x + 38, y + 38), n, 28, True, "white", "mm")
    tl = wrap(t, font(22, True), bw - 74 - 16)
    ty = y + 38 - (len(tl) - 1) * 15
    for k, ln in enumerate(tl):
        g.T((x + 74, ty + k * 30), ln, 22, True, "black", "lm")
    for j, ln in enumerate(lines):
        g.T((x + 24, y + 100 + j * 50), ln, 22, False, "black")
g.frame = (20, 20, 1580, 1020)
ya, yb = 135 + 170, 135 + 450 + 170
for i in range(3):
    arrow(d, (xs[i] + bw + 6, ya), (xs[i + 1] - 6, ya), w=5, head=16)
    arrow(d, (xs[i] + bw + 6, yb), (xs[i + 1] - 6, yb), w=5, head=16)
ym = 135 + bh + 55
d.line([(xs[3] + bw // 2, 135 + bh + 8), (xs[3] + bw // 2, ym)], fill="black", width=5)
d.line([(xs[3] + bw // 2, ym), (xs[0] + bw // 2, ym)], fill="black", width=5)
arrow(d, (xs[0] + bw // 2, ym), (xs[0] + bw // 2, 135 + 450 - 8), w=5, head=16)
g.T((40, 962), "Each step is explained under Reference workflow in docs/KNOWLEDGE_MAP.md;", 20, False, GREY)
g.T((40, 988), "the chapters docs/02 to docs/06 hold the detail.", 20, False, GREY)
g.save("04_reference_route.png")

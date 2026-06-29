# -*- coding: utf-8 -*-
"""MyKilo ikon/logo ureteci (PIL ile). 4x cizip kuculterek anti-alias."""
import math
from PIL import Image, ImageDraw

OUT = __file__.rsplit("/", 1)[0].replace("\\", "/") + "/.."  # mykilo kok klasoru

# Tema renkleri
BG_TOP    = (15, 23, 42)     # #0f172a koyu lacivert
BG_BOT    = (2, 6, 23)       # #020617 neredeyse siyah
ORANGE    = (249, 115, 22)   # #f97316 turuncu vurgu
ORANGE_LT = (251, 146, 60)   # #fb923c
TEAL      = (45, 212, 191)   # #2dd4bf
WHITE     = (248, 250, 252)  # #f8fafc
TICK      = (71, 85, 105)    # #475569 silik tikler


def lerp(a, b, t):
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))


def v_gradient(size, top, bot):
    img = Image.new("RGB", (1, size), top)
    for y in range(size):
        img.putpixel((0, y), lerp(top, bot, y / max(1, size - 1)))
    return img.resize((size, size))


def rounded_mask(size, radius):
    m = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill=255)
    return m


def draw_logo(canvas, full_bleed=False):
    """canvas: kenar uzunlugu (cizim cozunurlugu)."""
    S = canvas
    img = v_gradient(S, BG_TOP, BG_BOT)
    d = ImageDraw.Draw(img, "RGBA")
    cx = cy = S / 2

    # Kadran disindaki tikler (kantar/terazi hissi)
    r_tick = S * 0.40
    for i in range(60):
        ang = math.radians(i * 6 - 90)
        big = (i % 5 == 0)
        r1 = r_tick
        r2 = r_tick - (S * 0.045 if big else S * 0.025)
        x1, y1 = cx + r1 * math.cos(ang), cy + r1 * math.sin(ang)
        x2, y2 = cx + r2 * math.cos(ang), cy + r2 * math.sin(ang)
        col = ORANGE if big else TICK
        d.line([x1, y1, x2, y2], fill=col + (255,), width=max(2, int(S * (0.010 if big else 0.006))))

    # Turuncu gauge halkasi (alt tarafta acik, hiz gostergesi gibi)
    r_ring = S * 0.30
    bbox = [cx - r_ring, cy - r_ring, cx + r_ring, cy + r_ring]
    ring_w = int(S * 0.055)
    # arka silik halka
    d.arc(bbox, start=135, end=45, fill=(51, 65, 85, 255), width=ring_w)
    # dolu turuncu yay (135 -> 360 -> ~10) ilerlemeyi temsil eder
    d.arc(bbox, start=135, end=375, fill=ORANGE + (255,), width=ring_w)

    # Ic kisim: asagi yonlu trend cizgisi (kilo dususu / takip)
    pts_n = [(-0.16, -0.10), (-0.05, 0.02), (0.03, -0.05), (0.16, 0.12)]
    pts = [(cx + p[0] * S, cy + p[1] * S) for p in pts_n]
    d.line(pts, fill=WHITE + (255,), width=max(3, int(S * 0.018)), joint="curve")
    # ucta marker nokta
    last = pts[-1]
    rr = S * 0.028
    d.ellipse([last[0] - rr, last[1] - rr, last[0] + rr, last[1] + rr], fill=TEAL + (255,))
    d.ellipse([last[0] - rr, last[1] - rr, last[0] + rr, last[1] + rr], outline=WHITE + (255,), width=max(2, int(S * 0.006)))
    # ilk nokta
    first = pts[0]
    r0 = S * 0.016
    d.ellipse([first[0] - r0, first[1] - r0, first[0] + r0, first[1] + r0], fill=ORANGE_LT + (255,))

    return img


def render(size, name, full_bleed):
    scale = 4
    big = draw_logo(size * scale, full_bleed=full_bleed)
    img = big.resize((size, size), Image.LANCZOS).convert("RGBA")
    if not full_bleed:
        radius = int(size * 0.22)
        mask = rounded_mask(size, radius).resize((size, size), Image.LANCZOS)
        out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        out.paste(img, (0, 0), mask)
        img = out
    img.save(f"{OUT}/{name}", "PNG")
    print("yazildi:", name, size)


if __name__ == "__main__":
    render(512, "icon-512.png", full_bleed=False)
    render(192, "icon-192.png", full_bleed=False)
    render(180, "apple-touch-icon.png", full_bleed=False)
    render(512, "icon-maskable.png", full_bleed=True)
    render(32, "favicon-32.png", full_bleed=False)

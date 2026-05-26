import math
import random as rnd

_angle = 0.0
_stars = []
_sparks = []

BH_R = 90
DISK_INNER = BH_R + 10
DISK_OUTER = 275
DISK_STEP = 3

def setup():
    global _stars, _sparks
    size(960, 700)
    color_mode(HSB, 360, 100, 100, 100)
    frame_rate(60)
    hint(ENABLE_STROKE_PURE)

    rnd.seed(7)

    for _ in range(600):
        x = rnd.uniform(0, width)
        y = rnd.uniform(0, height)
        sz = abs(rnd.gauss(0.9, 0.6))
        h = rnd.choice([210, 220, 50, 30, 0])
        _stars.append([x, y, max(0.3, sz), h])

    for _ in range(180):
        r = rnd.uniform(DISK_INNER, DISK_OUTER)
        phi = rnd.uniform(0, TWO_PI)
        speed = 1.8 / math.sqrt(r / DISK_INNER)
        bri = rnd.uniform(0.6, 1.4)
        _sparks.append([r, phi, speed, bri])

def draw():
    global _angle, _sparks
    background(235, 35, 4)

    cx = width // 2
    cy = height // 2

    _draw_stars(cx, cy)
    _draw_nebula(cx, cy)
    _draw_disk_back(cx, cy)
    _draw_black_hole(cx, cy)
    _draw_disk_front(cx, cy)
    _draw_photon_ring(cx, cy)
    _draw_sparks(cx, cy)
    _draw_lens_corona(cx, cy)
 
    _angle += 0.38
    for sp in _sparks:
        sp[1] = (sp[1] + math.radians(sp[2])) % TWO_PI

def _doppler(offset=0.0):
    return 0.75 + 0.65 * math.cos(math.radians(_angle * 2.1) + offset)


def _disk_color(t, doppler):
    if t < 0.12:
        h, s, b = 52,  8, 100
    elif t < 0.30:
        h, s, b = 40, 55, 100
    elif t < 0.58:
        h, s, b = 22, 90, 90
    else:
        h, s, b = 10, 97, 44

    b_d = min(100.0, b  * doppler)
    a   = min(100.0, (1.0 - t * 0.62) * 65.0 * doppler)
    return h, s, b_d, a


def _ring_squash(r):
    return r * 0.35 + (r - DISK_INNER) * 0.005

def _draw_stars(cx, cy):
    no_stroke()
    for sx, sy, sz, sh in _stars:
        dx  = sx - cx
        dy  = sy - cy
        d   = math.sqrt(dx*dx + dy*dy)

        if d < BH_R + 2:
            continue

        if d < BH_R * 5.5:
            strength = (BH_R ** 2) / (d * d)
            ang  = math.atan2(dy, dx) + strength * 0.18
            new_d = max(BH_R + 3, d * (1 + strength * 0.09))
            sx   = cx + math.cos(ang) * new_d
            sy   = cy + math.sin(ang) * new_d
            if math.sqrt((sx - cx)**2 + (sy - cy)**2) < BH_R:
                continue
            
            if d < BH_R * 2.5:
                stroke(sh, 20, 90, 40)
                stroke_weight(0.6)
                line(sx, sy,
                     cx + math.cos(ang + 0.05) * new_d * 0.98,
                     cy + math.sin(ang + 0.05) * new_d * 0.98)
                no_stroke()

        fill(sh, 18, 100, 80)
        ellipse(sx, sy, sz, sz)


def _draw_nebula(cx, cy):
    no_stroke()
    for i in range(40):
        r = 520 - i * 8
        if r < 140:
            break
        fill(20, 55, 28, 1.6)
        ellipse(cx, cy, r * 2.3, r * 0.7)
    for i in range(18):
        r = 480 - i * 14
        if r < 200:
            break
        fill(255, 45, 22, 1.0)
        ellipse(cx, cy, r * 2, r * 0.52)


def _draw_disk_back(cx, cy):
    no_fill()
    dop = _doppler(math.pi)

    for r in range(DISK_OUTER, DISK_INNER, -DISK_STEP):
        t = (r - DISK_INNER) / float(DISK_OUTER - DISK_INNER)
        h, s, b, a = _disk_color(t, dop)
        stroke(h, s, b, a * 0.42)
        stroke_weight(DISK_STEP * 0.85)
        arc(cx, cy, r * 2, _ring_squash(r) * 2, PI, TWO_PI)


def _draw_black_hole(cx, cy):
    no_stroke()

    for i in range(35, 0, -1):
        r   = BH_R + i
        alp = max(0.0, 30.0 - i * 0.88)
        fill(24, 88, 100, alp)
        ellipse(cx, cy, r * 2, r * 2)

    for i in range(6, 0, -1):
        r   = BH_R + i
        alp = max(0.0, 55.0 - i * 8.0)
        fill(45, 40, 100, alp)
        ellipse(cx, cy, r * 2, r * 2)

    fill(0, 0, 0, 100)
    ellipse(cx, cy, BH_R * 2, BH_R * 2)


def _draw_disk_front(cx, cy):
    no_fill()
    dop = _doppler(0.0)

    for r in range(DISK_OUTER, DISK_INNER, -DISK_STEP):
        t = (r - DISK_INNER) / float(DISK_OUTER - DISK_INNER)
        h, s, b, a = _disk_color(t, dop)
        stroke(h, s, b, a)
        stroke_weight(DISK_STEP * 0.85)
        arc(cx, cy, r * 2, _ring_squash(r) * 2, 0, PI)


def _draw_photon_ring(cx, cy):
    no_fill()
    dop = _doppler(math.pi) * 1.35

    for i in range(50):
        t   = i / 49.0
        r_x = BH_R + 6  + i * 1.55
        r_y = BH_R * 0.50 + i * 0.72

        if i < 10:
            h, s, b = 62, 10, 100
        elif i < 24:
            h, s, b = 40, 62, 98
        elif i < 38:
            h, s, b = 22, 88, 72
        else:
            h, s, b = 12, 95, 38

        b   = min(100.0, b * dop)
        alp = max(0.0, (44.0 - i) * 3.1) * dop
        sw  = max(0.4, 3.2 - t * 2.6)

        stroke(h, s, b, min(100.0, alp))
        stroke_weight(sw)
        arc(cx, cy, r_x * 2, r_y * 2, PI, TWO_PI)


def _draw_sparks(cx, cy):
    no_stroke()
    dop = _doppler(0.0)

    for r, phi, speed, bri in _sparks:
        screen_xValue = cx + r * math.cos(phi)
        screen_yValue = cy + r * math.sin(phi) * 0.35

        if math.sin(phi) < 0.0:
            continue
        if math.sqrt((screen_xValue - cx)**2 + (screen_yValue - cy)**2) < BH_R + 2:
            continue

        t   = (r - DISK_INNER) / float(DISK_OUTER - DISK_INNER)
        h, s, b, a = _disk_color(t, dop * bri)
        sz  = max(0.5, 4.5 - t * 3.5)

        fill(h, s, min(100, b * 1.2), min(100, a * 1.4))
        ellipse(screen_xValue, screen_yValue, sz, sz)


def _draw_lens_corona(cx, cy):
    no_stroke()
    for i in range(1, 12):
        r   = BH_R + 35 + i * 5
        alp = max(0.0, 7.0 - i * 0.65)
        fill(28, 70, 100, alp)
        ellipse(cx, cy, r * 2, r * 2)
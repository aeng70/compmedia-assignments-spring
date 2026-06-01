import math
import random
 
angle = 0.0
ships = []
stars = []
 
CX, CY = 480, 350
BH_R = 80
 
def setup():
    size(960, 700)
    color_mode(HSB, 360, 100, 100, 100)
    frame_rate(60)
    random.seed(42)
    for _ in range(500):
        stars.append([random.uniform(0, 960), random.uniform(0, 700), random.uniform(0.8, 2.5)])
 
def draw():
    global angle
    background(228, 30, 5)
    draw_stars()
    draw_disk(back = True)
    draw_black_hole()
    draw_photon_ring()
    draw_disk(back = False)
    update_ships()
    angle += 0.6
 
def disk_color(t, mult):
    if t < 0.20: h, s, b = 50, 10, 100
    elif t < 0.50: h, s, b = 32, 68, 100
    elif t < 0.72: h, s, b = 16, 92,  82
    else: h, s, b =  8, 96,  38
    return h, s, min(100, b * mult), min(100, max(0, (1 - t) * 52 * mult))
 
def draw_stars():
    no_stroke()
    for sx, sy, sz in stars:
        fill(220, 15, 100, 75)
        ellipse(sx, sy, sz, sz)
 
def draw_disk(back):
    no_fill()
    phase = math.pi if back else 0
    dop = 0.65 + 0.55 * math.cos(math.radians(angle * 1.8) + phase)
    mult = dop * (0.40 if back else 1.0)
    for r in range(260, 85, -3):
        t = (r - 85) / 175.0
        h, s, b, a = disk_color(t, mult)
        stroke(h, s, b, a)
        stroke_weight(2.5)
        if back:
            arc(CX, CY, r * 2, r * 0.38, PI, TWO_PI)
        else:
            arc(CX, CY, r * 2, r * 0.38, 0, PI)
 
def draw_black_hole():
    no_stroke()
    for i in range(50, 0, -1):
        fill(22, 78, 96, 1.6)
        ellipse(CX, CY, (BH_R + i) * 2, (BH_R + i) * 2)
    for i in range(10, 0, -1):
        fill(40, 40, 100, 5)
        ellipse(CX, CY, (BH_R + i) * 2, (BH_R + i) * 2)
    fill(0, 0, 0, 100)
    ellipse(CX, CY, BH_R * 2, BH_R * 2)
 
def draw_photon_ring():
    no_fill()
    dop = 0.65 + 0.55 * math.cos(math.radians(angle * 1.8) + math.pi)
    for i in range(20, 0, -1):
        alp = max(0, (60 - i * 3) * dop)
        stroke(48, 22, 100, alp)
        stroke_weight(max(0.4, 2.5 - i * 0.1))
        arc(CX, CY, (BH_R + i * 3) * 2, (BH_R + i * 1.8) * 2, PI, TWO_PI)
 
def update_ships():
    global ships
    alive = []
    for x, y, vx, vy in ships:
        dx = CX - x
        dy = CY - y
        d = math.sqrt(dx * dx + dy * dy)
        if d < BH_R:
            continue
        g = 3500.0 / (d * d)
        vx += dx / d * g
        vy += dy / d * g
        x += vx
        y += vy
        draw_rocket(x, y, math.atan2(CY - y, CX - x), d)
        alive.append([x, y, vx, vy])
    ships = alive
 
def draw_rocket(x, y, facing, dist):
    sz = max(3, 18 * min(1.0, dist / 180.0))
    stretch = min(3.5, max(0.4, 90.0 / max(1.0, dist - BH_R)))
    push_matrix()
    translate(x, y)
    rotate(facing + HALF_PI)
    scale(1.0, stretch)
    no_stroke()
    for i in range(7):
        fill(28 + i * 5, 88, 100, 55 - i * 7)
        ellipse(0, sz * (1.1 + i * 0.35), sz * 0.45, sz * 0.55)
    fill(210, 15, 92, 95)
    rect(-sz * 0.28, -sz * 0.75, sz * 0.56, sz * 1.5, sz * 0.2)
    fill(0, 5, 98, 95)
    triangle(-sz * 0.28, -sz * 0.75, sz * 0.28, -sz * 0.75, 0, -sz * 1.55)
    fill(215, 55, 72, 95)
    triangle(-sz * 0.28, sz * 0.25, -sz * 0.95, sz * 0.80, -sz * 0.28, sz * 0.80)
    triangle( sz * 0.28, sz * 0.25,  sz * 0.95, sz * 0.80,  sz * 0.28, sz * 0.80)
    pop_matrix()
 
def mouse_pressed():
    ships.append([float(mouse_x), float(mouse_y), 0.0, 0.0])

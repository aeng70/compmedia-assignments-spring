import math
import random
import numpy as np # Skill 12: numpy for pixel manipulation
 
# Global variables (Skill 4)
angle = 0.0
planet_angle = 0.0
ships = []
asteroids = []
stars = []
paused = False
planet_pg = None
vignette = None
 
CX, CY = 480, 350
BH_R = 80
 
# Skill 10: Rocket class
class Rocket:
    def __init__(self, x, y):
        self.x, self.y   = float(x), float(y)
        self.vx, self.vy = 0.0, 0.0
 
    def update(self):
        # Distance formula:
        # d = √((x₂ - x₁)² + (y₂ - y₁)²)
        dx, dy = CX - self.x, CY - self.y
        d = math.sqrt(dx*dx + dy*dy)
        
        if d < BH_R:
            return False
        # Inverse-square gravity equation:
        # g = k / d²
        g = 3500.0 / (d*d)
        
        # Velocity update
        self.vx += dx/d * g
        self.vy += dy/d * g
        
        # Position update
        self.x  += self.vx
        self.y  += self.vy
        return True
 
    def draw(self):
        dx, dy = CX - self.x, CY - self.y
        d = math.sqrt(dx*dx + dy*dy)
        # Angle equation:
        # θ = atan2(dy, dx)
        draw_rocket_shape(self.x, self.y, math.atan2(dy, dx), d)
 
# Skill 10: Asteroid class
class Asteroid:
    def __init__(self):
        self.x = random.uniform(0, 960)
        self.y = random.uniform(0, 700)
        self.vx = random.uniform(-0.7, 0.7)
        self.vy = random.uniform(-0.7, 0.7)
        self.sz = random.uniform(5, 12)
        self.spin = 0.0
        self.spin_speed = random.uniform(-0.02, 0.02)
        n = random.randint(5, 8)
        self.verts = []
        # Polygon vertex equations:
        # x = cos(a) * r
        # y = sin(a) * r
        for i in range(n):
            a = math.pi * 2 * i / n + random.uniform(-0.3, 0.3)
            r = self.sz * random.uniform(0.55, 1.0)
            self.verts.append((math.cos(a) * r, math.sin(a) * r))
 
    def update(self):
        # Screen wrapping
        self.x = (self.x + self.vx) % width   # Skill 9: wrap around screen edges
        self.y = (self.y + self.vy) % height
        
        # Rotation
        self.spin += self.spin_speed
 
    def draw(self):
        color_mode(RGB, 255) # Skill 3: switch to RGB color mode
        push_matrix() # Skill 11: save transform state
        translate(self.x, self.y)
        rotate(self.spin) # Skill 11: rotation transform
        stroke(185, 140, 85, 190) # Skill 2: stroke color (RGB values)
        stroke_weight(1) # Skill 2: stroke weight
        fill(90, 65, 40, 150) # Skill 2: fill color (RGB values)
        begin_shape() # Skill 1: advanced drawing function
        for vx, vy in self.verts:
            vertex(vx, vy)
        end_shape(CLOSE)
        pop_matrix() # Skill 11: restore transform state
        color_mode(HSB, 360, 100, 100, 100) # Skill 3: restore HSB color mode
 
# Setup (Skill 4)
def setup():
    global planet_pg, vignette
    size(960, 700)
    color_mode(HSB, 360, 100, 100, 100) # Skill 3: HSB color mode
    frame_rate(60)
    random.seed(42)
 
    for _ in range(500):
        stars.append([random.uniform(0, 960), random.uniform(0, 700), random.uniform(0.8, 2.5)])
 
    for _ in range(12):
        asteroids.append(Asteroid()) # Skill 10: create Asteroid objects
 
    planet_pg = make_planet() # Skill 8: create off-screen image
 
    # Skill 12: precompute vignette mask using numpy
    # Distance field equation:
    # d = √(((x - CX)/(960*0.65))² + ((y - CY)/(700*0.65))²)
    y_i = np.arange(700, dtype=np.float32).reshape(-1, 1)
    x_i = np.arange(960, dtype=np.float32).reshape(1, -1)
    d = np.sqrt(((x_i - CX) / (960 * 0.65))**2 + ((y_i - CY) / (700 * 0.65))**2)
    
    # Clamp equation:
    # vignette = clip(1.3 - d, 0.15, 1.0)
    vignette = np.clip(1.3 - d, 0.15, 1.0)[:, :, np.newaxis].astype(np.float32)
 
# Skill 8: create planet as an off-screen image
def make_planet():
    pg = create_graphics(80, 80) # Skill 8: off-screen drawing surface
    pg.begin_draw()
    pg.color_mode(pg.HSB, 360, 100, 100, 100)
    pg.no_stroke()
    pg.background(0, 0, 0, 0)
    for i in range(36, 0, -1):
        t = i / 36.0
        pg.fill(200 + t * 20, 65, 75, 210)
        pg.ellipse(40, 40, i * 2, i * 2)
    pg.fill(210, 20, 100, 160)
    pg.ellipse(32, 32, 18, 14)
    pg.end_draw()
    return pg
 
# Draw loop (Skill 4)
def draw():
    global angle, planet_angle
    if paused:
        return
    background(228, 30, 5)
    draw_stars()
    draw_disk(back=True)
    draw_black_hole()
    draw_photon_ring()
    draw_disk(back=False)
    draw_planet()
    for a in asteroids: # Skill 10: call methods on objects
        a.update()
        a.draw()
    update_ships()
    apply_vignette() # Skill 12: numpy pixel effect
    angle += 0.6
 
# Skill 12: apply vignette using numpy pixel manipulation
def apply_vignette():
    # Pixel shading equation:
    # pixel = pixel × vignette
    load_np_pixels()
    np_pixels[:, :, :3] = (np_pixels[:, :, :3].astype(np.float32) * vignette).clip(0, 255).astype(np.uint8)
    update_np_pixels()
 
# Skill 8 + 11: draw orbiting planet
def draw_planet():
    global planet_angle
    planet_angle += 0.25
    px = int(CX + math.cos(math.radians(planet_angle)) * 340) # Skill 11: cos orbit
    py = int(CY + math.sin(math.radians(planet_angle)) * 110) # Skill 11: sin orbit
    image(planet_pg, px - 30, py - 30, 60, 60) # Skill 8: display + resize + move
 
# Color helper
def disk_color(t, mult):
    if t < 0.20: h, s, b = 50, 10, 100
    elif t < 0.50: h, s, b = 32, 68, 100
    elif t < 0.72: h, s, b = 16, 92,  82
    else: h, s, b =  8, 96,  38
    return h, s, min(100, b * mult), min(100, max(0, (1 - t) * 52 * mult))
 
def draw_stars():
    no_stroke() # Skill 2: controlling color state
    for sx, sy, sz in stars:
        fill(220, 15, 100, 75) # Skill 3: HSB color values
        ellipse(sx, sy, sz, sz) # Skill 1: basic drawing function
 
def draw_disk(back):
    no_fill() # Skill 2: controlling color state
    
    # Doppler brightness equation:
    # dop = 0.65 + 0.55cos(θ + phase)
    phase = math.pi if back else 0
    dop = 0.65 + 0.55 * math.cos(math.radians(angle * 1.8) + phase)
    mult = dop * (0.40 if back else 1.0)
    for r in range(260, 85, -3):
        t = (r - 85) / 175.0
        h, s, b, a = disk_color(t, mult)
        stroke(h, s, b, a) # Skill 2: stroke color
        stroke_weight(2.5) # Skill 2: stroke weight
        if back:
            arc(CX, CY, r * 2, r * 0.38, PI, TWO_PI) # Skill 1: arc (advanced)
        else:
            arc(CX, CY, r * 2, r * 0.38, 0, PI)
 
def draw_black_hole():
    no_stroke() # Skill 2: controlling color state
    for i in range(50, 0, -1):
        fill(22, 78, 96, 1.6)
        ellipse(CX, CY, (BH_R + i) * 2, (BH_R + i) * 2) # Skill 1: ellipse
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
    for ship in ships: # Skill 10: call methods on Rocket objects
        if ship.update():
            ship.draw()
            alive.append(ship)
    ships = alive
 
def draw_rocket_shape(x, y, facing, dist):
    # Size scaling
    sz = max(3, 18 * min(1.0, dist / 180.0))
    
    stretch = min(3.5, max(0.4, 90.0 / max(1.0, dist - BH_R)))
    
    push_matrix() # Skill 11: save transform state
    translate(x, y) # Skill 11: translate
    rotate(facing + HALF_PI) # Skill 11: rotate to face black hole
    scale(1.0, stretch) # Skill 11: scale (spaghettification)
    no_stroke()
    for i in range(7):
        fill(28 + i * 5, 88, 100, 55 - i * 7)
        ellipse(0, sz * (1.1 + i * 0.35), sz * 0.45, sz * 0.55)
    fill(210, 15, 92, 95)
    rect(-sz * 0.28, -sz * 0.75, sz * 0.56, sz * 1.5, sz * 0.2) # Skill 1: rect
    fill(0, 5, 98, 95)
    triangle(-sz * 0.28, -sz * 0.75, sz * 0.28, -sz * 0.75, 0, -sz * 1.55) # Skill 1: triangle
    fill(215, 55, 72, 95)
    triangle(-sz * 0.28, sz * 0.25, -sz * 0.95, sz * 0.80, -sz * 0.28, sz * 0.80)
    triangle( sz * 0.28, sz * 0.25,  sz * 0.95, sz * 0.80,  sz * 0.28, sz * 0.80)
    pop_matrix() # Skill 11: restore transform state
 
 
# Skill 5: Mouse and keyboard events
def mouse_pressed(): # Skill 5: mouse event function
    ships.append(Rocket(mouse_x, mouse_y)) # Skill 5: mouse_x, mouse_y variables
 
def key_pressed(): # Skill 5: keyboard event function
    global paused
    if key == 'r' or key == 'R': # Skill 5: key variable
        ships.clear()
    elif key == ' ':
        paused = not paused
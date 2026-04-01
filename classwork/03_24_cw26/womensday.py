# International Women's Day Celebration Card
# py5 Imported Mode (run in Thonny with py5 plugin)
#
# Controls:
#   CLICK  → launch a burst of floating flowers from cursor
#   SPACE  → toggle falling confetti on/off
#   R      → randomise petal colours
# ─────────────────────────────────────────────────────────────

import math, random

# ── Palette ────────────────────────────────────────────────────
PURPLE   = (138,  43, 226)
MAGENTA  = (220,  20, 100)
GOLD     = (255, 200,  40)
CREAM    = (255, 245, 230)
LAVENDER = (200, 160, 240)

# ══════════════════════════════════════════════════════════════
#  CLASS: FloatingFlower
#  Each flower drifts upward, rotates, and oscillates side-to-side.
# ══════════════════════════════════════════════════════════════
class FloatingFlower:
    def __init__(self, x, y, size=None, colour=None, speed=None):
        self.x      = x
        self.y      = y
        self.size   = size   if size   else random.uniform(18, 42)
        self.colour = colour if colour else random.choice([PURPLE, MAGENTA, GOLD, LAVENDER])
        self.speed  = speed  if speed  else random.uniform(0.6, 2.0)
        self.angle  = random.uniform(0, TWO_PI)
        self.spin   = random.uniform(-0.04, 0.04)
        # oscillation
        self.phase  = random.uniform(0, TWO_PI)
        self.amp    = random.uniform(20, 55)
        self.freq   = random.uniform(0.018, 0.04)
        self.petals = random.randint(5, 8)
        self.alive  = True

    def update(self):
        self.y     -= self.speed                          # float upward
        self.angle += self.spin                           # rotate
        # sine oscillation for horizontal drift
        self.x     += math.sin(frame_count * self.freq + self.phase) * 1.2
        if self.y < -self.size * 2:
            self.alive = False

    def draw(self):
        push_matrix()
        translate(self.x, self.y)
        rotate(self.angle)
        r, g, b = self.colour
        # centre glow
        no_stroke()
        fill(r, g, b, 60)
        ellipse(0, 0, self.size * 2.6, self.size * 2.6)
        # petals
        fill(r, g, b, 210)
        stroke(255, 255, 255, 90)
        stroke_weight(0.8)
        for i in range(self.petals):
            a  = TWO_PI / self.petals * i
            px = math.cos(a) * self.size * 0.75
            py = math.sin(a) * self.size * 0.75
            ellipse(px, py, self.size * 0.9, self.size * 0.55)
        # centre dot
        fill(255, 220, 60, 240)
        no_stroke()
        ellipse(0, 0, self.size * 0.55, self.size * 0.55)
        pop_matrix()

    def recolour(self):
        self.colour = random.choice([PURPLE, MAGENTA, GOLD, LAVENDER])


# ══════════════════════════════════════════════════════════════
#  CLASS: ConfettiPiece
#  Colourful rectangles that fall and tumble.
# ══════════════════════════════════════════════════════════════
class ConfettiPiece:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x      = random.uniform(0, width)
        self.y      = random.uniform(-height, 0)
        self.w      = random.uniform(6, 18)
        self.h      = random.uniform(4, 10)
        self.colour = random.choice([PURPLE, MAGENTA, GOLD, LAVENDER, (255,255,255)])
        self.speed  = random.uniform(1.5, 4.5)
        self.angle  = random.uniform(0, TWO_PI)
        self.spin   = random.uniform(-0.08, 0.08)
        self.drift  = random.uniform(-0.8, 0.8)

    def update(self):
        self.y     += self.speed
        self.x     += self.drift
        self.angle += self.spin
        if self.y > height + 20:
            self.reset()

    def draw(self):
        push_matrix()
        translate(self.x, self.y)
        rotate(self.angle)
        r, g, b = self.colour
        fill(r, g, b, 200)
        no_stroke()
        rect(-self.w/2, -self.h/2, self.w, self.h, 2)
        pop_matrix()


# ══════════════════════════════════════════════════════════════
#  Globals
# ══════════════════════════════════════════════════════════════
flowers   = []
confetti  = []
show_conf = True
bg_offset = 0      # slow background pulse via sine


def setup():
    size(700, 520)
    text_font(create_font("Georgia", 32))
    # seed initial flowers
    for _ in range(14):
        flowers.append(FloatingFlower(
            random.uniform(60, width - 60),
            random.uniform(60, height - 60)
        ))
    # confetti pool
    for _ in range(120):
        confetti.append(ConfettiPiece())


def draw():
    global bg_offset
    bg_offset += 0.012

    # ── Animated gradient background ──────────────────────────
    # Interpolate between deep violet and dark plum using sine
    t   = (math.sin(bg_offset) + 1) / 2          # 0..1
    bg1 = lerp_color(color(30, 0, 60), color(80, 0, 80), t)
    bg2 = lerp_color(color(10, 0, 40), color(50, 10, 70), t)
    for y in range(0, height + 1, 4):
        inter = map(y, 0, height, 0, 1)
        c     = lerp_color(bg1, bg2, inter)
        stroke(c)
        stroke_weight(4)
        line(0, y, width, y)

    # decorative ring of small circles (cosine/sine orbit)
    no_fill()
    stroke(255, 255, 255, 25)
    stroke_weight(1)
    for i in range(36):
        a  = TWO_PI / 36 * i + frame_count * 0.004
        rx = width/2  + math.cos(a) * 230
        ry = height/2 + math.sin(a) * 165
        r2 = math.sin(a * 3 + frame_count * 0.01) * 6 + 8
        ellipse(rx, ry, r2, r2)

    # ── Confetti ───────────────────────────────────────────────
    if show_conf:
        for c in confetti:
            c.update()
            c.draw()

    # ── Flowers ───────────────────────────────────────────────
    for f in flowers[:]:
        f.update()
        f.draw()
    flowers[:] = [f for f in flowers if f.alive]

    # Maintain a minimum of 10 ambient flowers
    while len(flowers) < 10:
        flowers.append(FloatingFlower(
            random.uniform(40, width - 40),
            random.uniform(height * 0.4, height + 10)
        ))

    # ── Venus / female symbol (centre, pulsing) ───────────────
    pulse = math.sin(frame_count * 0.05) * 6
    _draw_venus_symbol(width/2, height/2 - 30, 70 + pulse)

    # ── Text ──────────────────────────────────────────────────
    _draw_text()

    # ── HUD hint ──────────────────────────────────────────────
    fill(255, 255, 255, 110)
    text_size(12)
    text_align(LEFT, BOTTOM)
    text("CLICK -> flowers  |  SPACE -> confetti  |  R -> recolour", 12, height - 8)


# ─────────────────────────────────────────────────────────────
def _draw_venus_symbol(cx, cy, r):
    """Draw the female symbol as a circle + cross."""
    stroke(255, 210, 80, 200)
    stroke_weight(3.5)
    no_fill()
    ellipse(cx, cy - r * 0.25, r * 1.4, r * 1.4)
    line(cx, cy - r * 0.25 + r * 0.7, cx, cy + r * 0.75)
    line(cx - r * 0.35, cy + r * 0.45, cx + r * 0.35, cy + r * 0.45)


def _draw_text():
    text_align(CENTER, CENTER)

    # Gold shadow
    fill(255, 180, 20, 160)
    text_size(46)
    text("International Women's Day", width/2 + 2, 72)

    # White highlight
    fill(255, 255, 255, 240)
    text("International Women's Day", width/2, 70)

    # Subtitle
    text_size(22)
    fill(220, 160, 255, 230)
    text("March 8  *  #IWD2025", width/2, 118)

    # Fact / message
    text_size(15)
    fill(255, 240, 200, 210)
    text(
        "Women hold 10% of Fortune 500 CEO positions.",
        width/2, height - 88
    )
    text(
        "Equal pay. Equal rights. Equal opportunities.",
        width/2, height - 62
    )


# ══════════════════════════════════════════════════════════════
#  Interaction
# ══════════════════════════════════════════════════════════════
def mouse_pressed():
    """Burst of 10 flowers from the click position."""
    for _ in range(10):
        flowers.append(FloatingFlower(
            mouse_x + random.uniform(-30, 30),
            mouse_y + random.uniform(-30, 30),
            size  = random.uniform(14, 34),
            speed = random.uniform(1.0, 2.5)
        ))


def key_pressed():
    global show_conf
    if key == ' ':
        show_conf = not show_conf
    if key in ('r', 'R'):
        for f in flowers:
            f.recolour()
        for c in confetti:
            c.colour = random.choice([PURPLE, MAGENTA, GOLD, LAVENDER, (255,255,255)])
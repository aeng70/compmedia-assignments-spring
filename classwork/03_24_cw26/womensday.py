import math, random

PURPLE   = (138,  43, 226)
MAGENTA  = (220,  20, 100)
GOLD     = (255, 200,  40)
CREAM    = (255, 245, 230)
LAVENDER = (200, 160, 240)

flowers   = []
confetti  = []
show_conf = True
bg_offset = 0 # slow background pulse via sine


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

    t   = (math.sin(bg_offset) + 1) / 2          # 0..1
    bg1 = lerp_color(color(30, 0, 60), color(80, 0, 80), t)
    bg2 = lerp_color(color(10, 0, 40), color(50, 10, 70), t)
    for y in range(0, height + 1, 4):
        inter = map(y, 0, height, 0, 1)
        c     = lerp_color(bg1, bg2, inter)
        stroke(c)
        stroke_weight(4)
        line(0, y, width, y)

    # decoration
    no_fill()
    stroke(255, 255, 255, 25)
    stroke_weight(1)
    for i in range(36):
        a  = TWO_PI / 36 * i + frame_count * 0.004
        rx = width/2  + math.cos(a) * 230
        ry = height/2 + math.sin(a) * 165
        r2 = math.sin(a * 3 + frame_count * 0.01) * 6 + 8
        ellipse(rx, ry, r2, r2)

    if show_conf:
        for c in confetti:
            c.update()
            c.draw()

    for f in flowers[:]:
        f.update()
        f.draw()
    flowers[:] = [f for f in flowers if f.alive]

    while len(flowers) < 10:
        flowers.append(FloatingFlower(
            random.uniform(40, width - 40),
            random.uniform(height * 0.4, height + 10)
        ))

    pulse = math.sin(frame_count * 0.05) * 6
    _draw_venus_symbol(width/2, height/2 - 30, 70 + pulse)

    _draw_text()

    fill(255, 255, 255, 110)
    text_size(12)
    text_align(LEFT, BOTTOM)
    text("CLICK -> flowers  |  SPACE -> confetti  |  R -> recolour", 12, height - 8)


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

    fill(255, 180, 20, 160)
    text_size(46)
    text("International Women's Day", width/2 + 2, 72)

    fill(255, 255, 255, 240)
    text("International Women's Day", width/2, 70)

    text_size(22)
    fill(220, 160, 255, 230)
    text("March 8  *  #IWD2025", width/2, 118)

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
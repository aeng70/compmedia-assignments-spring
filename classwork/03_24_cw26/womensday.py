# PY5 IMPORTED MODE CODE
import math, random
from FloatingFlower import FloatingFlower
from ConfettiPiece import ConfettiPiece

flowers = []
confetti = []
show_conf = True

def setup():
    size(700, 520)
    text_font(create_font("Georgia", 32))
    for _ in range(120):
        confetti.append(ConfettiPiece())

def draw():
    background(30, 0, 60)
    if show_conf:
        for c in confetti:
            c.update()
            c.draw()
    for f in flowers[:]:
        f.update()
        f.draw()
    flowers[:] = [f for f in flowers if f.alive]
    draw_symbol(width/2, height/2 - 30)
    draw_text()
    fill(255, 255, 255, 110)
    text_size(12)
    text_align(LEFT, BOTTOM)
    text("CLICK -> flowers  |  SPACE -> confetti", 12, height - 8)

def draw_symbol(cx, cy):
    r = 70 + math.sin(frame_count * 0.05) * 6
    no_fill()
    stroke(255, 210, 80, 200)
    stroke_weight(3.5)
    ellipse(cx, cy - r * 0.25, r * 1.4, r * 1.4)
    line(cx, cy - r * 0.25 + r * 0.7, cx, cy + r * 0.75)
    line(cx - r * 0.35, cy + r * 0.45, cx + r * 0.35, cy + r * 0.45)

def draw_text():
    text_align(CENTER, CENTER)
    text_size(46)
    fill(255, 180, 20, 160)
    text("International Women's Day", width/2 + 2, 72)
    fill(255, 255, 255, 240)
    text("International Women's Day", width/2, 70)
    text_size(22)
    fill(220, 160, 255, 230)
    text("March 8 2026", width/2, 118)
    text_size(15)
    fill(255, 240, 200, 210)
    text("Fight for Feminism!", width/2, height - 62)

def mouse_pressed():
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
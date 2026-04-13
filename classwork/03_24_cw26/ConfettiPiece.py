# PY5 IMPORTED MODE CODE
import random

COLOURS = [(138, 43, 226), (220, 20, 100), (255, 200, 40), (200, 160, 240), (255, 255, 255)]

class ConfettiPiece:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.uniform(0, width)
        self.y = random.uniform(-height, 0)
        self.w = random.uniform(6, 18)
        self.h = random.uniform(4, 10)
        self.colour = random.choice(COLOURS)
        self.speed = random.uniform(1.5, 4.5)
        self.angle = random.uniform(0, TWO_PI)
        self.spin = random.uniform(-0.08, 0.08)
        self.drift = random.uniform(-0.8, 0.8)

    def update(self):
        self.x += self.drift
        self.y += self.speed
        self.angle += self.spin
        if self.y > height + 20:
            self.reset()

    def draw(self):
        r, g, b = self.colour
        push_matrix()
        translate(self.x, self.y)
        rotate(self.angle)
        no_stroke()
        fill(r, g, b, 200)
        rect(-self.w/2, -self.h/2, self.w, self.h, 2)
        pop_matrix()
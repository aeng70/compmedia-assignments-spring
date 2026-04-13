# PY5 IMPORTED MODE CODE
import math, random

COLOURS = [(138, 43, 226), (220, 20, 100), (255, 200, 40), (200, 160, 240)]

class FloatingFlower:
    def __init__(self, x, y, size=None, speed=None):
        self.x = x
        self.y = y
        self.size = size  or random.uniform(18, 42)
        self.speed = speed or random.uniform(0.6, 2.0)
        self.colour = random.choice(COLOURS)
        self.angle = random.uniform(0, TWO_PI)
        self.spin = random.uniform(-0.04, 0.04)
        self.phase = random.uniform(0, TWO_PI)
        self.freq = random.uniform(0.018, 0.04)
        self.petals = random.randint(5, 8)
        self.alive = True

    def update(self):
        self.y -= self.speed
        self.angle += self.spin
        self.x += math.sin(frame_count * self.freq + self.phase) * 1.2
        if self.y < -self.size * 2:
            self.alive = False

    def draw(self):
        r, g, b = self.colour
        push_matrix()
        translate(self.x, self.y)
        rotate(self.angle)
        # glow
        no_stroke()
        fill(r, g, b, 60)
        ellipse(0, 0, self.size * 2.6, self.size * 2.6)
        # petals
        fill(r, g, b, 210)
        stroke(255, 255, 255, 90)
        stroke_weight(0.8)
        for i in range(self.petals):
            a = TWO_PI / self.petals * i
            ellipse(math.cos(a) * self.size * 0.75,
                    math.sin(a) * self.size * 0.75,
                    self.size * 0.9, self.size * 0.55)
        # center
        no_stroke()
        fill(255, 220, 60, 240)
        ellipse(0, 0, self.size * 0.55, self.size * 0.55)
        pop_matrix()
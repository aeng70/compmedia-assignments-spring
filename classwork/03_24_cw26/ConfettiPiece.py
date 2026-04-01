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
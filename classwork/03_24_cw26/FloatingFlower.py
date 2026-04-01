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
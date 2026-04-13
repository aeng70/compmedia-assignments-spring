# PY5 IMPORTED MODE CODE
class Pet:
    def __init__(self, col, size):
        self.x = random(width)
        self.y = random(height)
        self.health = 100
        self.hunger = 0
        self.col = col
        self.size = size
        self.xSpd = random(-3, 3)
        self.ySpd = random(-3, 3)

    def display(self):
        fill(self.col)
        no_stroke()
        ellipse(self.x, self.y, self.size, self.size)
        fill(0)
        circle(self.x-7,self.y-5,3)
        circle(self.x+7,self.y-5,3)
        no_fill()
        stroke(0)
        arc(self.x,self.y+5,14,7,0,PI)
        

    def bounceOnEdge(self):
        r = self.size / 2
        # Right / left
        if self.x > width - r:
            self.x = width - r
            self.xSpd *= -1
        elif self.x < r:
            self.x = r
            self.xSpd *= -1
        # Bottom / top
        if self.y > height - r:
            self.y = height - r
            self.ySpd *= -1
        elif self.y < r:
            self.y = r
            self.ySpd *= -1

    def move(self):
        self.x += self.xSpd
        self.y += self.ySpd

    def animate(self):
        self.move()
        self.bounceOnEdge()
        self.display()
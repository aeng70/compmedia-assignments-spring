class Pet:
    def __init__(self, color, size):
        self.x = random(width)
        self.y = random(height)
        self.health = 100
        self.hunger = 0
        self.color = color
        self.size = size
        self.xSpd = random(-3,3)
        self.ySpd = random(-3,3)
        
    def display(self):
        rect(self.health, self.hunger, self.size)
        
    def bounceOnEdge(self):
      if self.x > width or self.x < 0:
        self.xSpd*=-1
      if self.y > height or self.y < 0:
        self.ySpd*=-1
        
    def animate(self):
      self.display()
      self.move()
      self.bounceOnEdge()

    def move(self):
        self.x += self.xSpd
        self.y += self.ySpd
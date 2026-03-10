# PY5 IMPORTED MODE CODE
class Wiggler:
    def __init__(self, w, h):
        self.x = random(width) 		# will appear anywhere on canvas
        self.y = random(height) 		# will appear anywhere on canvas
        self.w = w
        self.h = h
        self.xSpd = random(-3, 3) 	# create random movement
        self.ySpd = random(-3,3) 	# create random movement
    
    def display(self):
        rect(self.x, self.y, self.w, self.h)
    
    def move(self):
        self.x += self.xSpd
        self.xSpd = random(-3, 3) #pick a new speed so it looks 'wiggly'
        self.y += self.ySpd
        self.ySpd = random(-3, 3) #pick a new speed so it looks 'wiggly'
        
    def bounceOnEdge(self):
      if self.x > width or self.x < 0:
        self.xSpd*=-1
      if self.y > height or self.y < 0:
        self.ySpd*=-1
        
    def animate(self):
      self.display()
      self.move()
      self.bounceOnEdge()

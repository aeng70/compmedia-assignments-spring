def setup():
    size(200,400)
    background(150)
    
def draw():
    color_mode(HSB,360,100,100)
    fill(0,100,50)
    circle(100,75,100)
    
    fill(60,100,50)
    circle(100,200,100)
    
    fill(120,100,50)
    circle(100,325,100)
    
    mouse_pressed()
    
def collidePointCircle(pointX, pointY, circX, circY, diameter):
  """Input coordinates for the point and x, y, and diameter (the width/height) of the circle.
  Returns true if the point and circle are touching.

  Does not work for ellipse/oval shapes."""

  distance = dist(pointX, pointY, circX, circY)
  radius = diameter/2
  
  if(distance <= radius):
    return True
  else:
    return False
    
def mouse_pressed():
    if collidePointCircle(mouse_x, mouse_y, 100, 75, 100):
        fill(0,100,100)
        circle(100,75,100)
    if collidePointCircle(mouse_x, mouse_y, 100, 200, 100):
        fill(60,100,100)
        circle(100,200,100)
    if collidePointCircle(mouse_x, mouse_y, 100, 325, 100):
        fill(120,100,100)
        circle(100,325,100)
    
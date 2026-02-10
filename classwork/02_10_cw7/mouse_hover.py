def setup():
    size(400,600)
def draw():
    fill(255)
    background(220)
    #text(str(mouseX) + ", " + str(mouseY), 20, 20)
    circle(100, 200, 75) #top left
    circle(200, 200, 75) #top middle
    circle(300, 200, 75) #top right
    circle(100, 300, 75) #bottom left
    circle(200, 300, 75) #bottom middle
    circle(300, 300, 75) #bottom right
    
    color_mode(HSB,360,100,100)
    if collidePointCircle(mouse_x, mouse_y, 100, 200, 75):
        fill(240,40,100)
        circle(100,200,75)
        
    if collidePointCircle(mouse_x, mouse_y, 200, 200, 75):
        fill(270,100,100)
        circle(100,300,75)
        circle(300,300,75)
        
    if collidePointCircle(mouse_x, mouse_y, 300, 200, 75):
        fill(0,0,0)
        circle(300,200,75)
        circle(200,300,75)
        
    if collidePointCircle(mouse_x, mouse_y, 100, 300, 75):
        fill(0,100,100)
        for i in range(1,4):
            circle(i*100,200,75)
            
    if collidePointCircle(mouse_x, mouse_y, 200, 300, 75):
        fill(120,100,100)
        circle(100,200,75)
        
    if collidePointCircle(mouse_x, mouse_y, 300, 300, 75):
        fill(30,100,100)
        circle(100, 300, 75)
    
    color_mode(RGB,255,255,255)
    
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
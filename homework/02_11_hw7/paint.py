colors = {}

def setup():
    size(800,800)
    color_mode(HSB,360,100,100)
    background(0,0,100)
    global colors
    colors = {
        "red":0,
        "orange":30,
        "yellow":60,
        "green":120,
        "blue":240,
        "purple":270 }
    
    global key_functions
    key_functions = {
        "clear":'c',
        "small":'1',
        "medium":'2',
        "large":'3' }
    
def draw():
    fill(0,0,75)
    rect(0,0,60,285)
    
    fill(colors["red"], 100, 100)
    circle(30,30,30)
    
    fill(colors["orange"], 100, 100)
    circle(30,75,30)
    
    fill(colors["yellow"], 100, 100)
    circle(30,120,30)
    
    fill(colors["green"], 100, 100)
    circle(30,165,30)
    
    fill(colors["blue"], 100, 100)
    circle(30,210,30)
    
    fill(colors["purple"], 100, 100)
    circle(30,255,30)
    
    if is_mouse_pressed:
        line(pmouse_x, pmouse_y, mouse_x, mouse_y)
        
    if is_key_pressed:
        if key == key_functions["clear"]:
            background(0,0,100)
        if key == key_functions["small"]:
            stroke_weight(1)
        if key == key_functions["medium"]:
            stroke_weight(10)
        if key == key_functions["large"]:
            stroke_weight(20)
        
def mouse_pressed():
    if collidePointCircle(mouse_x, mouse_y, 30, 30, 30):
        stroke(colors["red"], 100, 100)
        
    if collidePointCircle(mouse_x, mouse_y, 30, 75, 30):
        stroke(colors["orange"], 100, 100)
        
    if collidePointCircle(mouse_x, mouse_y, 30, 120, 30):
        stroke(colors["yellow"], 100, 100)
        
    if collidePointCircle(mouse_x, mouse_y, 30, 165, 30):
        stroke(colors["green"], 100, 100)
        
    if collidePointCircle(mouse_x, mouse_y, 30, 210, 30):
        stroke(colors["blue"], 100, 100)
        
    if collidePointCircle(mouse_x, mouse_y, 30, 255, 30):
        stroke(colors["purple"], 100, 100)
    
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
    
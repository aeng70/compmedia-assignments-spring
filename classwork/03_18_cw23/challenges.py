angle = 15

def setup():
    size(400,400)
    
def draw():
    background(220)
    global angle
    cos_value = cos(radians(angle))
    sin_value = sin(radians(angle) + PI/2)
    circle(cos_value*50+200, height/2, 50)
    
    circle(cos_value*50+200, sin_value*50+200, 50)
    
    circle(100,100,sin(radians(angle))*50)
    
    circle(300, sin(radians(angle))*50+125, 50)
    
    angle += 1
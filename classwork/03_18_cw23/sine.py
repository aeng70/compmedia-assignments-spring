angle = 15

def setup():
    size(510,350)
    
def draw():
    background(220)
    global angle
    sine_value = sin(radians(angle))
    circle(width/2, sine_value*50+100, 50)
    angle += 1
angle = 15
offset = 1

def setup():
    size(400,400)
    
def draw():
    global angle, offset
    cos_value = cos(radians(angle))
    sin_value = sin(radians(angle))
    circle(cos_value*(50+offset)+200, sin_value*50+200, 50)
    angle += 1
    offset += 1
    if offset > 50:
        offset *= -1
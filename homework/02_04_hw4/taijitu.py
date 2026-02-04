def setup():
    size(400,400)
    
def draw():
    background(255)
    # text(str(mouse_x) + ", " + str(mouse_y), 20, 20)
    
    fill(0)
    circle(199,199,354)
    
    fill(255)
    arc(199,199,350,350, radians(-90), radians(90))
    
    fill(0)
    circle(199,111.5,175)
    
    fill(255)
    stroke(255)
    circle(199,286.6,175)
    
    circle(199,111.5,40)
    
    fill(0)
    stroke(0)
    circle(199,286.5,40)

    stroke(0)
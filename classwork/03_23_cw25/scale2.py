x = 1

def setup():
    size(400,400)
    
def draw():
    color_mode(HSB,360,100,100)
    background(0)
    fill(0,100,100)
    global x
    scale(1)
    circle(200, 75, 50*sin(x)+50)
    x += 0.05
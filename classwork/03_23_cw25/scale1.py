x = 0

def setup():
    size(400,400)
    
def draw():
    frame_rate(60)
    global x
    background(255)
    fill(0,100,0)
    rect_mode(CENTER)
    scale(1)
    square(200,200,50 * sin(x) + 100)
    x += 0.05
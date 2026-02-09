def setup():
    size(400,400)
    background(220)
    
def draw():
    fill(0)
    line(mouse_x, mouse_y, pmouse_x, pmouse_y)
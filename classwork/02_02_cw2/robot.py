def setup():
    size(400,400)
    
def draw():
    background(220)
    displayCoordinates()
    grid()
    
    fill(220)
    circle(200,120,60)
    rect(120,120,160,80)
    
    circle(160,160,40)
    
def grid():
    stroke(255)
    for x in range(width):
        if x % 20 == 0:
            for y in range(height):
                if y % 20 == 0:
                    line(x, 0, x, height)
                    line(0, y, width, y)
    stroke(0)
    
def displayCoordinates():
    fill(0)
    text(str(mouse_x) + ", " + str(mouse_y), 20, 20)
def setup():
    size(400,500)
    
def draw():
    background(220)
    displayCoordinates()
    grid()
    
    #antenna
    line(200,100,200,40)
    fill(220)
    circle(200,120,60)
    rect(120,120,160,80)
    circle(200,40,20)
    
    # eyes
    circle(160,160,60)
    circle(240,160,60)
    circle(160,160,40)
    circle(240,160,40)
    
    #neck
    rect(195,200,10,20)
    
    #body
    rect(150,220,100,80)
    rect(160,240,80,20)
    circle(200,280,20)
    
    #legs
    line(180,300,180,400)
    line(220,300,220,400)
    circle(180,400,30)
    circle(220,400,30)
    
    #layer
    stroke(220)
    rect(160,400,80,20)
    stroke(0)
    line(165,400,195,400)
    line(205,400,235,400)
    
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
def setup():
    size(500,500)
    
def draw():
    background(255)
    
    circle(150, 150, 100)
    circle(130, 130, 10)
    circle(170, 130, 10)
    arc(150, 170, 50, 20, 0, PI, OPEN)
    
    circle(350, 150, 100)
    circle(330, 130, 10)
    circle(370, 130, 10)
    arc(350, 170, 30, 30, PI, 2*PI, OPEN)
    line(320, 115, 340, 120)
    line(380, 115, 360, 120)
    
    circle(250, 350, 100)
    circle(230, 330, 10)
    circle(270, 330, 10)
    line(230, 365, 270, 375)
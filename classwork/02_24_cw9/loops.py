def setup():
    size(600,600)
    background(255)

def draw():
    color_mode(RGB,255,255,255)
    x = 100
    fill(255,0,0)
    while x < width:
        circle(x,60,40)
        x += 100
        
    x = 100
    fill(0,255,0)
    while x < width:
        circle(x,60,30)
        x += 100
        
    x = 100
    fill(0,0,255)
    while x < width:
        circle(x,60,20)
        x += 100
        
    x = 100
    fill(255,0,255)
    while x < width:
        circle(x,60,10)
        x += 100
        
    for x in range(100,600,100):
        color_mode(HSB,360,100,100)
        fill(240,100,x/4)
        circle(x,300,x)
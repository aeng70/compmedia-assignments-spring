def setup():
    size(400,400)
    
def draw():
    background(220)
    fill(0)
    #text(str(mouse_x) + ", " + str(mouse_y), 20, 20)
    
    color_mode(HSB,360,100,100)
    
    d = 60
    dp5 = d + 5
    
    for x in range(d+1,width-dp5,dp5):
        for y in range(d+1,height-dp5,dp5):
            fill(random(360,100,100))
            circle(x,y,d)
            
    color_mode(RGB,255,255,255)
stuff = {}

def setup():
    size(600,600)
    color_mode(HSB,360,100,100)
    background(0,0,100)
    
    global stuff
    stuff = {
        "random_range":360,
        "upper":30,
        "mid":20,
        "lower":10
    }
    
def draw():
    if mouse_y < 200:
        circle(mouse_x,mouse_y,(stuff["upper"]))
    if mouse_y < 400:
        circle(mouse_x,mouse_y,(stuff["mid"]))
    if mouse_y < 600 :
        circle(mouse_x,mouse_y,(stuff["lower"]))
        
    h = random(stuff["random_range"])
        
    stroke(h,100,100)
stuff = {}

def setup():
    size(600,600)
    color_mode(HSB,360,100,100)
    background(0,0,100)
    
    global stuff
    stuff = {
        "upper":30,
        "mid":20,
        "lower":10
    }
    
def draw():
    if mouse_y < 200:
        stroke_weight(stuff["upper"])
    if mouse_y < 400:
        stroke_weight(stuff["mid"])
    if mouse_y < 600 :
        stroke_weight(stuff["lower"])
        
    h = random(360)
        
    stroke(h,100,100)
    line(mouse_x,mouse_y,pmouse_x,pmouse_y)
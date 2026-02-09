theLine = {}

def setup():
    size(400,400)
    background(220)
    
    global theLine
    theLine = {
        "weight":5,
        "red":255,
        "green":0,
        "blue":255,
        "opacity":100
    }
    
def draw():
    if mouse_x > 200:
        stroke_weight(theLine["weight"])
    else:
        stroke_weight(1)
        
    if dist(mouse_x,mouse_y,width/2,height/2) < 100:
        stroke(theLine["red"],theLine["green"],theLine["blue"])
    else:
        stroke(0,0,255)
        
    line(mouse_x,mouse_y,pmouse_x,pmouse_y)
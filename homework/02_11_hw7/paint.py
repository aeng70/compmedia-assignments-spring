colors = {}

def setup():
    size(600,400)
    color_mode(HSB,360,100,100)
    global colors
    colors = {
        "red":0,
        "orange":30,
        "yellow":60,
        "green":120,
        "blue":240,
        "indigo":270,
        "violet":300 }
    
def draw():
    background(0,0,100)
    rect(0,0,60,399)
    circle(30,30,30)
    circle(30,75,30)
    circle(30,120,30)
    circle(30,165,30)
    circle(30,210,30)
    circle(30,255,30)
    circle(30,300,30)
        
circ1 = {
    "x": 339,
    "xSpeed": 2
}

circ2 = {
    "y": 20,
    "ySpeed": 2
}

def setup():
    size(520,360)
    frame_rate(2)
    
def draw():
    global circ1, circ2
    background(220)
    circle(circ1["x"],50,20)
    circ1["x"] -= circ1["xSpeed"]
    
    circle(200,circ2["y"],20)
    circ2["y"] += circ2["ySpeed"]
    
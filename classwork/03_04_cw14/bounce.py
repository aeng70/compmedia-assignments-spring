circ = {
    "x": 1,
    "x_spd": 5
}

circ4 = {
    "x": width/2,
    "y": height/2,
    "x_spd": random(-200,200),
    "y_spd": random(-200,200)
}

def setup():
    size(400,400)
    frame_rate(60)
    
def draw():
    background(220)
    global circ, circ4
    
    circle(circ["x"],200,20)
    if circ["x"] <= 10:
        circ["x_spd"] = abs(circ["x_spd"])
    if circ["x"] >= 389:
        circ["x_spd"] *= -1
    circ["x"] += circ["x_spd"]
    
    circle(circ4["x"],circ4["y"],20)
    if circ4["x"] <= 10:
        circ4["x_spd"] = abs(circ4["x_spd"])
    if circ4["x"] >= 389:
        circ4["x_spd"] *= -1
    if circ4["y"] <= 10:
        circ4["y_spd"] = abs(circ4["y_spd"])
    if circ4["y"] >= 389:
        circ4["y_spd"] *= -1
    circ4["x"] += circ4["x_spd"]
    circ4["y"] += circ4["y_spd"]
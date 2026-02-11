circ1 = {}
def setup():
    size(400,600)
    global circ1
    circ1 = {
        "size":200 }
def draw():
    background(220)
    
    if is_key_pressed:
        if key == 'b' and circ1["size"] < width:
            circ1["size"] += 5
        if key == 's' and circ1["size"] > 5:
            circ1["size"] -= 5
    
    circle(200,200,circ1["size"])
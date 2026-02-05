def setup():
    size(400,400)
    fill(230,150,150)
    
def draw():
    background(220)
    rect(100,100,200,100)
    
def mouse_pressed():
    if collidePointRect(mouse_x, mouse_y, 100, 100, 200, 100):
        fill(random(255), random(255), random(255))
        
def collidePointRect(pX, pY, rX, rY, rW, rH):
    if pX >= rX and pX <= rX + rW and pY >= rY and pY <= rY + rH:
        return True
    else:
        return False
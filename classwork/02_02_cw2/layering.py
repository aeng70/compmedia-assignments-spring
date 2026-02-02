def setup(): #runs once
    size(400, 400)
 
def draw(): #runs like in forever loop in Netlogo
    background(220) #make the background grey
    
    fill(255)
    stroke(0)
    circle(120,120,200)
    
    fill(220)
    no_stroke()
    rect(10,100,220,150)
    
    stroke(0)
    line(20,100,220,100)
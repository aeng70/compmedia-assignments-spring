def setup(): #runs once
    size(400, 400)
    print("width =", width, "\nheight =", height) #system variables
 
def draw(): #runs like in a Netlogo forever loop
    background(220) #make the background grey
    #text(str(mouse_x) + ", " + str(mouse_y), 20, 20)
    
    #rectangle: rect(xcor, ycor, width, height)
    rect(200, 50, 70, 10)
def setup():
    size(400,400)
    
def draw():
    triangle(50,25,125,50,75,75)
    quad(275,50,350,75,300,125,250,75)
    begin_shape()
    vertex(175,100)
    vertex(225,125)
    vertex(225,175)
    vertex(175,200)
    vertex(125,175)
    vertex(175,150)
    vertex(150,125)
    end_shape(CLOSE) # connects the last vertex to the first
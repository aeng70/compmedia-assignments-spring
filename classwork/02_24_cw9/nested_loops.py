def setup():
    size(600,600)
    background(255)
    
def draw():
    for i in range(100,600,100):
        for j in range(100,600,100):
            circle(i,j,50)
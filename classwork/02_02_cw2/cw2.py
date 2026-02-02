def setup():
    size(400,400)
  
def draw():
    # corners
    background(220)
    square(1,1,50)
    square(348,1,50)
    square(1,348,50)
    square(348,348,50)
    
    # middle
    square(149,149,50)
    square(199,149,50)
    square(149,199,50)
    square(199,199,50)

    # inscribed circles
    circle(26,26,50)
    circle(373,26,50)
    circle(26,373,50)
    circle(373,373,50)
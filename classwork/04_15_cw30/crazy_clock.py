# idea: 60x60 grids shaded by a diff color each hour
# x is mins, y is secs, colors is hours

def setup():
    size(800, 600)
    background(220)
    
def draw():
    for i in range(0, 600, 10):
        for j in range(0, 600, 10):
            line(0, j, 600, j)
        line(i, 0, i, 600)
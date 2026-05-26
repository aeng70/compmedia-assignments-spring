import numpy as np

def setup_pixels():
    #code for initial state
    for x in range(width):
        for y in range(height):
            chance = (int)(random(10))
            if chance == 0:
                np_pixels[y, x, 2] = 255
            
    update_np_pixels()
    
def setup():
    global s
    size(200,200)
    s = [[[[0, 0, 0] for i in range(8)] for x in range(width)] for y in range(height)]  # state
    background(0) # black
    load_np_pixels()
    setup_pixels()

def evaluate_neighbors():
    global s
    #code to update neighbors-state
    for x in range(1, width-1):
        for y in range(1, height-1):
            s[x][y] = [list(c) for pxls in np_pixels[y-1:y+2, x-1:x+2, 1:] for c in pxls]            
            s[x][y].pop(4)
    
def transition():
    #code to apply the rules from neighbors’ state
    count = 0
    
    for x in range(1, width-1):
        for y in range(1, height-1):
            for clr in s[x][y]:
                if clr[1] == 255:
                    count += 1
                    
            if count == 3:
                np_pixels[y, x, 1:] = [0, 255, 0]
            else:
                np_pixels[y, x, 1:] = [0, 0, 0]
    
    update_np_pixels()

def draw(): # driver
    evaluate_neighbors()
    transition()


import numpy as np
colors = [[0, 255, 0], [0, 0, 0], [165, 42, 42], [255, 255, 0]]

def setup_pixels():    
    for x in range(width):
        for y in range(height):
            random_color_index = (int)(random(4))
            np_pixels[y, x, 1:] = colors[random_color_index]
        
    update_np_pixels()
    
def setup():
    global p
    size(200,200)
    p = [[[[0, 0, 0] for i in range(8)] for x in range(width)] for y in range(height)]
    background(0)
    load_np_pixels()
    setup_pixels()
    # code
    
def evaluate_neighbors():
    global p
    # code to update neighbors-state
    for x in range(1, width-1):
        for y in range(1, height-1):
            p[x][y] = [list(c) for pxls in np_pixels[y-1:y+2, x-1:x+2, 1:] for c in pxls]            
            p[x][y].pop(4)
            
def transition():
    # code to apply the rules from neighbors' state
    for x in range(1, width-1):
        for y in range(1, height-1):
            inx = [0] * len(colors)
            for clr in p[x][y]:
                for i in range(4):
                    if clr == colors[i]:
                        inx[i] += 1
                        
            clr_mode = inx.index(max(inx))
            np_pixels[y, x, 1:] = colors[clr_mode]
            
    update_np_pixels()
    
def draw():
    # driver
    evaluate_neighbors()
    transition()
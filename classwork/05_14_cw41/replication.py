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
    s = [ [ ] ]  # state
    background(0) # black
    load_np_pixels()
    setup_pixels()

def evaluate_neighbors():
    global s 
    #code to update neighbors-state
    

def transition():
    #code to apply the rules from neighbors’ state
    update_np_pixels()

def draw(): # driver
    evaluate_neighbors()
    transition()


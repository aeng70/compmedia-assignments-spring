import numpy as np

def setup_pixels():
    colors = [[0, 255, 0], [0, 0, 0], [165, 42, 42], [255, 255, 0]]
    random_color_index = (int)(random(4))
    
    for x in range(width):
        for y in range(height):
            np_pixels[y, x, 1:] = colors[random_color_index]
        
    update_np_pixels()
    
def setup():
    global p
    size(200,200)
    p = [[]]
    background(0)
    load_np_pixels()
    setup_pixels()
    # code
    
def evaluate_neighbors():
    global p
    # code to update neighbors-state
    
def transition():
    # code to apply the rules from neighbors' state
    update_np_pixels()
    
def draw():
    # driver
    evaluate_neighbors()
    transition()
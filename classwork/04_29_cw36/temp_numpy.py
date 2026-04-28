import numpy as np

def setup():
    global original
    size(800, 400)
    img = load_image("mountain-3.jpg")
    img.resize(width, 0)    
    image(img, 0, 0)
    load_pixels()
    for i in pixels:
        for j in pixels[i]

def mouse_clicked():
    temp = remap(mouse_x, 0, width, -100, 100)
    apply_temp(temp)

def limit(value):
  # keeps color values between 0 and 255
  return max(0, min(255, int(value)))

def apply_temp(temp):
    global original
    # Temperature adjustment
    # positive = warm (more red, less blue)
    # negative = cool (more blue, less red)      
    for x in range(width):
        for y in range(height):
            clr = original[x][y]        
            nr = limit(red(clr) + temp) # modify red
            ng = limit(green(clr) + temp * 0.3) # modify green a little
            nb = limit(blue(clr) - temp) # modify blue       
            pixels[x + y * width] = color(nr, ng, nb)
    update_pixels()
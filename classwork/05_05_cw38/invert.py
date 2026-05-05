def setup():
    global img
    size(800, 400)
    img = load_image("mountain-3.jpg")
    img.resize(width, 0)
    image(img, 0, 0)

def invert():
    global img
    img.load_pixels()
    for i in range(len(img.pixels)):
        pixel = img.pixels[i]
        
        newRed = 255 - red(pixel)
        newGreen = 255 - green(pixel)
        newBlue = 255 - blue(pixel)
        
        newColor = color(newRed, newGreen, newBlue)
        img.pixels[i] = newColor
        
    img.update_pixels()
    image(img, 0, 0)
    
def mouse_pressed():
    invert()
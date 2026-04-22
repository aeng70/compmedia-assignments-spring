pixelList = {}

def setup():
    size(350, 250)
    global pixelList, img
    
    img = load_image("mountain-3.jpg")
    
    img.resize(width // 2, 0)
    image(img, 20, 20)
    
    load_pixels()
    
    for x in range(width):
        for y in range(height):
            newKey = str(x) + "," + str(y)
            pixelList[newKey] = pixels[x + y * width]
            
    background(220)
    
def draw():
    pixelKey = str(mouse_x) + "," + str(mouse_y)
    pixel = pixelList[pixelKey]
    pixelColor = color(pixel)
    
    no_stroke()
    fill(pixelColor)
    
    circle(mouse_x, mouse_y, 10)
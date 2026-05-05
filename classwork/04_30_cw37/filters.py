import numpy as np
filter1 = {
    "1" : THRESHOLD,
    "2" : GRAY,
    "3" : INVERT,
    "4" : POSTERIZE,
    "5" : BLUR,
    "6" : ERODE,
    "7" : DILATE
}

def setup():
    global original
    size(800, 400)
    img = load_image("mountain-3.jpg")
    img.resize(width, 0)    
    image(img, 0, 0)

def key_pressed():
    global filter1
    for i in range(0, 8):
        if is_key_pressed:
            if key == str(i):
                if i == 0:
                    img = load_image("mountain-3.jpg")
                    img.resize(width, 0)    
                    image(img, 0, 0)
                elif i == 4:
                    apply_filter(filter1[str(i)], 4)
                else:
                    apply_filter(filter1[str(i)])

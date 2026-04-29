import numpy as np

def setup():
    global original
    size(800, 400)
    img = load_image("mountain-3.jpg")
    img.resize(width, 0)    
    image(img, 0, 0)
    load_np_pixels()
    original = np_pixels.copy()

def draw():
    temp = remap(mouse_x, 0, width, -100, 100)
    apply_temp(temp)

def apply_temp(temp):
    global original
    A, r, g, b = 0, 1, 2, 3
    np_pixels[:, :, r] = np.clip(original[:, :, r] + temp, 0, 255)
    np_pixels[:, :, g] = np.clip(original[:, :, g] + temp * 0.4, 0, 255)
    np_pixels[:, :, b] = np.clip(original[:, :, b] - temp, 0, 255)
    update_np_pixels()
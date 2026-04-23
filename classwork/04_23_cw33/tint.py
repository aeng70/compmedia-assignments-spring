def setup():
    size(400, 160)
    
    img = load_image("mountain-3.jpg")
    
    img.resize(width, 0)
    image(img, 0, 0)
    
    load_pixels()
    h1 = get_pixels(0, 0, width // 2, height)
    tint(255, 0, 0)
    image(h1, 0, 0)
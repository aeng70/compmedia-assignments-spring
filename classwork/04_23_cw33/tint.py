def setup():
    size(400, 160)
    
    img = load_image("mountain-3.jpg")
    
    img.resize(width, 0)
    image(img, 0, 0)
    
    load_pixels()
    h1 = get_pixels(0, 0, width // 2, height // 2)
    tint(255, 0, 0, 100)
    image(h1, 0, 0)
    
    h2 = get_pixels(width //2, 0, width, height // 2)
    tint(0, 255, 0, 100)
    image(h2, width // 2, 0)
    
    h3 = get_pixels(0, height // 2, width // 2, height)
    tint(0, 0, 255, 100)
    image(h3, 0, height // 2)
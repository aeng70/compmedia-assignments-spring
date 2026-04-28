def setup():
    size(800, 400)
    
    img = load_image("mountain-3.jpg")
    img.resize(width, 0)
    
    background(0)
    
    edges = create_image(img.width, img.height, RGB)
    edges.load_pixels()
    img.load_pixels()
    
    for y in range(1, img.height - 1):
        for x in range(1, img.width - 1):
            gx = 0
            gy = 0
            
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    idx = (y + dy) * img.width + (x + dx)
                    r = red(img.pixels[idx])
                    g = green(img.pixels[idx])
                    b = blue(img.pixels[idx])
                    br = (r + g + b) / 3
                    
                    kernel_x = dx
                    kernel_y = dy
                    
                    gx += br * kernel_x
                    gy += br * kernel_y
            
            edge_strength = sqrt(gx * gx + gy * gy)
            
            if edge_strength > 50:
                edges.pixels[y * img.width + x] = color(255, 255, 255)
            else:
                edges.pixels[y * img.width + x] = color(0, 0, 0)
    
    edges.update_pixels()
    
    image(edges, 0, 0)
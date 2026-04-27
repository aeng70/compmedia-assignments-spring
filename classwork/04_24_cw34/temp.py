def setup():
    size(800, 400)
    
    img = load_image("mountain-3.jpg")
    img.resize(width, 0)
    image(img, 0, 0)
    
    cooler_temp = -50
    warmer_temp = 50
    
    h1 = get_pixels(0, 0, width // 2, height // 2)
    h1 = adjust_temperature(h1, cooler_temp, "cooler")
    image(h1, 0, 0)
    
    h2 = get_pixels(width // 2, 0, width, height // 2)
    image(h2, width // 2, 0)
    
    h3 = get_pixels(0, height // 2, width // 2, height)
    h3 = adjust_temperature(h3, warmer_temp, "warmer")
    image(h3, 0, height // 2)
    
    h4 = get_pixels(width // 2, height // 2, width, height)
    mixed_temp = (cooler_temp + warmer_temp) / 2
    if mixed_temp < 0:
        h4 = adjust_temperature(h4, mixed_temp, "cooler")
    else:
        h4 = adjust_temperature(h4, mixed_temp, "warmer")
    image(h4, width // 2, height // 2)

def adjust_temperature(pixels_img, temp_value, effect_type):
    pixels_img.load_pixels()
    temp_abs = abs(temp_value)
    
    for i in range(len(pixels_img.pixels)):
        c = pixels_img.pixels[i]
        r = red(c)
        g = green(c)
        b = blue(c)
        
        if effect_type == "cooler":
            r = max(0, min(255, r - temp_abs))
            b = max(0, min(255, b + temp_abs))
        elif effect_type == "warmer":
            r = max(0, min(255, r + temp_abs))
            b = max(0, min(255, b - temp_abs))
        
        pixels_img.pixels[i] = color(r, g, b)
    
    pixels_img.update_pixels()
    return pixels_img
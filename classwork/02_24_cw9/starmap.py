stars = []
num_stars = 200
twinkle_speed = 0.05

def setup():
    py5.size(800, 600)
    py5.smooth()
    py5.no_stroke()
    
    # Create random stars
    for i in range(num_stars):
        star = {
            'x': py5.random(py5.width),
            'y': py5.random(py5.height),
            'base_size': py5.random(1, 3),
            'brightness': py5.random(50, 255),
            'twinkle_offset': py5.random(py5.TWO_PI),
            'color_variation': py5.random(0.5, 1.5),
            'twinkle_speed': py5.random(0.02, 0.08)
        }
        stars.append(star)

def draw():
    py5.background(0)  # Black background
    
    # Calculate time for twinkling effect
    t = py5.frame_count * twinkle_speed
    
    # Draw each star
    for star in stars:
        # Twinkling effect using sine wave
        twinkle = (py5.sin(t + star['twinkle_offset']) + 1) / 2
        brightness = int(star['brightness'] * (0.5 + twinkle * 0.5))
        
        # Slight color variation for some stars (blue-white to warm white)
        if star['color_variation'] > 1.2:
            # Blue-white stars
            py5.fill(180, 180, brightness)
        elif star['color_variation'] < 0.7:
            # Warm/yellowish stars
            py5.fill(brightness, brightness, 180)
        else:
            # White stars
            py5.fill(brightness)
        
        # Size also twinkles slightly
        size = star['base_size'] * (0.8 + twinkle * 0.4)
        py5.circle(star['x'], star['y'], size)

def mouse_pressed():
    """Add a new star where you click"""
    new_star = {
        'x': py5.mouse_x,
        'y': py5.mouse_y,
        'base_size': py5.random(1, 4),
        'brightness': py5.random(150, 255),
        'twinkle_offset': py5.random(py5.TWO_PI),
        'color_variation': py5.random(0.5, 1.5),
        'twinkle_speed': py5.random(0.02, 0.08)
    }
    stars.append(new_star)

def key_pressed():
    """Press 'c' to clear, 'r' to regenerate stars"""
    global stars
    if py5.key == 'c':
        stars.clear()
    elif py5.key == 'r':
        stars.clear()
        for i in range(num_stars):
            star = {
                'x': py5.random(py5.width),
                'y': py5.random(py5.height),
                'base_size': py5.random(1, 3),
                'brightness': py5.random(50, 255),
                'twinkle_offset': py5.random(py5.TWO_PI),
                'color_variation': py5.random(0.5, 1.5),
                'twinkle_speed': py5.random(0.02, 0.08)
            }
            stars.append(star)

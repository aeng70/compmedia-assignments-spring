stars = []
num_stars = 200
twinkle_speed = 0.05

def setup():
    size(800, 600)
    smooth()
    no_stroke()
    
    # Create random stars
    for i in range(num_stars):
        star = {
            'x': random(width),
            'y': random(height),
            'base_size': random(1, 3),
            'radiance': random(50, 255),
            'twinkle_offset': random(TWO_PI),
            'color_variation': random(0.5, 1.5),
            'twinkle_speed': random(0.02, 0.08)
        }
        stars.append(star)

def draw():
    background(0)  # Black background
    
    # Calculate time for twinkling effect
    t = frame_count * twinkle_speed
    
    # Draw each star
    for star in stars:
        # Twinkling effect using sine wave
        twinkle = (sin(t + star['twinkle_offset']) + 1) / 2
        radiance = int(star['radiance'] * (0.5 + twinkle * 0.5))
        
        # Slight color variation for some stars (blue-white to warm white)
        if star['color_variation'] > 1.2:
            # Blue-white stars
            fill(180, 180, radiance)
        elif star['color_variation'] < 0.7:
            # Warm/yellowish stars
            fill(radiance, radiance, 180)
        else:
            # White stars
            fill(radiance)
        
        # Size also twinkles slightly
        star_size = star['base_size'] * (0.8 + twinkle * 0.4)
        circle(star['x'], star['y'], size)

def mouse_pressed():
    """Add a new star where you click"""
    new_star = {
        'x': mouse_x,
        'y': mouse_y,
        'base_size': random(1, 4),
        'radiance': random(150, 255),
        'twinkle_offset': random(TWO_PI),
        'color_variation': random(0.5, 1.5),
        'twinkle_speed': random(0.02, 0.08)
    }
    stars.append(new_star)

def key_pressed():
    """Press 'c' to clear, 'r' to regenerate stars"""
    global stars
    if key == 'c':
        stars.clear()
    elif key == 'r':
        stars.clear()
        for i in range(num_stars):
            star = {
                'x': random(width),
                'y': random(height),
                'base_size': random(1, 3),
                'radiance': random(50, 255),
                'twinkle_offset': random(TWO_PI),
                'color_variation': random(0.5, 1.5),
                'twinkle_speed': random(0.02, 0.08)
            }
            stars.append(star)

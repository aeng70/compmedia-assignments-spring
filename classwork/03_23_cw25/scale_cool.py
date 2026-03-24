angle = 0

def setup():
    size(600, 600)
    color_mode(HSB, 360, 100, 100)

def draw():
    global angle

    background(0, 0, 15)
    translate(width / 2+50, height / 2)

    for i in range(12):
        rotate(TWO_PI / 12)

        # Scale pulses in and out over time
        pulse = 1 + 0.3 * sin(angle + i * 0.5)
        scale(pulse)

        clr = (angle * 30 + i * 30) % 360
        fill(clr, 80, 95, 180)
        no_stroke()
        ellipse(80, 0, 60, 30)

    angle += 0.03
def setup():
    size(600, 600)
    no_loop()

def draw():
    background(240)
    translate(width / 2, height / 2)
    rect_mode(CENTER)

    for i, s in enumerate([1.0, 0.75, 0.5, 0.25]):
        gray = int(255 * (1 - s))
        # comment the push matrix() and pop_matrix() calls.  What happens?
        # push_matrix()
        scale(s)
        fill(gray)
        no_stroke()
        rect(0, 0, 400, 400)
        # comment the push matrix() and pop_matrix() calls.  What happens?
        # pop_matrix()
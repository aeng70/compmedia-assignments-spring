timer = 300
countdown = 5
face_order = [0, 1, 2]

def setup():
    size(500, 500)

def draw_happy(x, y):
    circle(x, y, 100)
    circle(x - 20, y - 20, 10)
    circle(x + 20, y - 20, 10)
    arc(x, y + 20, 50, 20, 0, PI, OPEN)

def draw_angry(x, y):
    circle(x, y, 100)
    circle(x - 20, y - 20, 10)
    circle(x + 20, y - 20, 10)
    arc(x, y + 20, 30, 30, PI, 2 * PI, OPEN)
    line(x - 30, y - 35, x - 10, y - 30)
    line(x + 30, y - 35, x + 10, y - 30)

def draw_neutral(x, y):
    circle(x, y, 100)
    circle(x - 20, y - 20, 10)
    circle(x + 20, y - 20, 10)
    line(x - 20, y + 15, x + 20, y + 25)

faces = [draw_happy, draw_angry, draw_neutral]
x_positions = [150, 350, 250]
y_positions = [150, 150, 350]

def draw():
    global timer, countdown, face_order

    background(255)

    text_size(20)
    fill(0)
    text_align(CENTER)
    text(f"Swapping in: {countdown}s", 250, 480)

    stroke(0)
    fill(255)
    for i in range(3):
        faces[face_order[i]](x_positions[i], y_positions[i])

    timer -= 1
    if timer <= 0:
        import random
        random.shuffle(face_order)
        timer = 300
        countdown = 5
    else:
        countdown = (timer // 60) + 1
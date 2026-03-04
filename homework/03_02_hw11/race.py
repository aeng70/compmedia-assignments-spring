circs = [
    {"x": 50,  "y": 80,  "xSpeed": 2,  "radius": 12, "color": (255, 80, 80)},   # red
    {"x": 50,  "y": 160, "xSpeed": 3,  "radius": 12, "color": (80, 80, 255)},   # blue
    {"x": 50,  "y": 240, "xSpeed": 4,  "radius": 12, "color": (80, 200, 80)},   # green
    {"x": 50,  "y": 320, "xSpeed": 1.5,"radius": 12, "color": (200, 160, 80)}   # orange
]

def setup():
    size(520, 400)
    frame_rate(60)
    no_stroke()
    text_align(LEFT, BOTTOM)

def draw():
    background(220)

    # update, wrap, and draw each circle
    for i, c in enumerate(circs, start=1):
        fill(c["color"][0], c["color"][1], c["color"][2])
        circle(c["x"], c["y"], c["radius"] * 2)

        # label the racer with its number
        fill(0)
        text_size(12)
        text(f"#{i}", c["x"] - 4, c["y"] + 4)

        # move horizontally
        c["x"] += c["xSpeed"]

        # wrap around right -> left
        if c["x"] - c["radius"] > width:
            c["x"] = -c["radius"]
        # wrap around left -> right (in case of negative speeds)
        elif c["x"] + c["radius"] < 0:
            c["x"] = width + c["radius"]
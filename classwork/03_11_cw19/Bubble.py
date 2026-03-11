from BubbleClass import *

bubbles = []

def setup():
    size(800, 600)
    global bubbles
    for i in range(20):
        bubbles.append(Bubble(color(random(256), random(256), random(256), 75), 75))

def draw():
    background(255)
    for i in bubbles:
        i.animate()
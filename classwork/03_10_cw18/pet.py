from Pet import *

def setup():
    size(800, 600)
    global pet
    pet = Pet(color(200, 100, 150), 50)

def draw():
    background(255)
    pet.animate()
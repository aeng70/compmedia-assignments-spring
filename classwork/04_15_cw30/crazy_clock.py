# idea: 60x60 grids shaded by a diff color each hour
# x is mins, y is secs, colors is hours

from datetime import datetime

def setup():
    size(800, 600)
    background(220)
    
def draw():
    now = datetime.now()
    formatted_time = now.strftime("%H:%M:%S")
    time_array = formatted_time.split(":")
    
    hours = time_array[0]
    mins = time_array[1]
    secs = time_array[2]
    
    # grid
    for i in range(0, 610, 10):
        for j in range(0, 600, 10):
            line(0, j, 600, j)
        line(i, 0, i, 600)
        
    if mins == "00" and secs == "00":
        setup()
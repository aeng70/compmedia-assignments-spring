# idea: 60x60 grid shaded by a diff color each hour
# x is mins, y is secs, colors is hours

from datetime import datetime

grid = [[0 for _ in range(60)] for _ in range(60)]
last_hour = -1

def setup():
    size(800, 600)
    color_mode(HSB, 360, 100, 100)
    frame_rate(60)
    initialize_grid()
    
def initialize_grid():
    global grid, last_hour
    
    now = datetime.now()
    current_hour = now.hour
    current_min = now.minute
    current_sec = now.second
    
    last_hour = current_hour
    grid = [[0 for _ in range(60)] for _ in range(60)]
    
    for min in range(60):
        for sec in range(60):
            if min < current_min:
                grid[min][sec] = 1
            elif min == current_min and sec <= current_sec:
                grid[min][sec] = 1

def draw():
    global grid, last_hour
    
    now = datetime.now()
    current_hour = now.hour
    current_min = now.minute
    current_sec = now.second
    
    if current_hour != last_hour:
        last_hour = current_hour
        grid = [[0 for _ in range(60)] for _ in range(60)]
        for min in range(60):
            for sec in range(60):
                if min < current_min:
                    grid[min][sec] = 1
                elif min == current_min and sec <= current_sec:
                    grid[min][sec] = 1
    else:
        if grid[current_min][current_sec] == 0:
            grid[current_min][current_sec] = 1
    
    draw_grid(current_hour, current_min, current_sec)
    draw_info_panel(current_hour)

def draw_grid(current_hour, current_min, current_sec):
    cell_size = 600.0 / 60
    hour_hue = (current_hour * 15) % 360
    background(0, 0, 86)
    no_stroke()
    
    for min in range(60):
        for sec in range(60):
            x = sec * cell_size
            y = min * cell_size
            
            if grid[min][sec]:
                if min == current_min and sec == current_sec:
                    fill(hour_hue, 100, 100)
                else:
                    fill(hour_hue, 90, 80)
            else:
                fill(0, 0, 86)
            
            rect(x, y, cell_size, cell_size)
    
    stroke(0, 0, 40)
    stroke_weight(0.5)
    for i in range(61):
        line(i * cell_size, 0, i * cell_size, 600)
        line(0, i * cell_size, 600, i * cell_size)
    line(600, 0, 600, 600)

def draw_info_panel(current_hour):
    fill(0, 0, 86)
    no_stroke()
    rect(601, 0, 200, 600)
    
    fill(0, 0, 0)
    text_size(11)
    text_align(LEFT)
    
    text("Color = Hours", 610, 30)
    text("Rows = Minutes", 610, 50)
    text("Cols = Seconds", 610, 70)
    text("Each cell = 1 second", 610, 90)
    text("Fills left to right,", 610, 110)
    text("top to bottom", 610, 125)
    
    fill(0, 0, 0)
    text_size(12)
    text("Hour Colors:", 610, 145)
    
    rows = 12
    cols = 2
    square_size = 28
    start_x = 610
    start_y = 155
    col_spacing = 8
    row_spacing = 8
    
    for h in range(24):
        row = h // 2
        col = h % 2
        x = start_x + (col * (square_size + col_spacing))
        y = start_y + (row * (square_size + row_spacing))
        
        hour_hue = (h * 15) % 360
        fill(hour_hue, 100, 100)
        no_stroke()
        rect(x, y, square_size, square_size)
        
        fill(0, 0, 0)
        text_size(12)
        text_align(CENTER)
        text(str(h), x + square_size/2, y + square_size/2 + 4)
    
    stroke(0, 0, 0)
    stroke_weight(3)
    no_fill()
    current_row = current_hour // 2
    current_col = current_hour % 2
    x = start_x + (current_col * (square_size + col_spacing))
    y = start_y + (current_row * (square_size + row_spacing))
    rect(x - 2, y - 2, square_size + 4, square_size + 4)

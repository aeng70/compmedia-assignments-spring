# PY5 IMPORTED MODE CODE
def draw_grid():
  push_style()
  translate(0,0)
  fill(220)
  stroke_weight(0)
  rect(0, 0, 80, 40)
  fill(0)
  stroke_weight(1)
  text(str(mouse_x) + " , " + str(mouse_y), 20, 20)
  stroke_weight(1)
  stroke(0)
  
  for x in range(0, width, 20):
    line(x, 0, x, height)
  
  for y in range(0, height, 20):
    line(0, y, width, y)
  
  no_fill()
  pop_style()

def draw_dot():
  push_style()
  translate(0,0)
  stroke_weight(3)
  if is_mouse_pressed:
    if is_key_pressed:
      if key == chr(65535): #shift key
        stroke(0,0,255)
        ellipse(mouse_x,mouse_y, 5, 5)
    else:
      stroke(255,0,0)
      ellipse(mouse_x,mouse_y,5,5)
  no_stroke()
  pop_style()
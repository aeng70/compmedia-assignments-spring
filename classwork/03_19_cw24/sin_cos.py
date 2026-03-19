#Credit to Ken Chung for the p5 version of this code

a = 70  #Set up the horizontal amplitute
b = 50  #Set up the vertical amplitute
angle = 0

def setup():
  size(400, 400)
  text_size(20)
  
  text_align(CENTER)
  rect_mode(CENTER)

def draw():
  background(255)
  global a, b, angle
  x = a*cos(radians(angle))
  y = b*sin(radians(angle))
  angle += 1
  
  # Heading & Settings
  text("TO DRAW A CIRCLE (or ELLIPSE) . . .", 200, 30)
  text("a = " + str(a) + ",   b = " + str(b), 200,320)
  fill(150)
  text("Try changing a and b in lines 3 and 4 of the code. If a = b, you get a circle.", 200, 350, width-50, 50)
  
  # Draw circle
  stroke(0)
  no_fill()
  ellipse(200, 200, 2*a, 2*b)
  line(200,200,200+a,200)
  no_stroke()
  fill(255,0,0)
  circle(200+x, 200+y, 8)
  circle(200, 200, 4)
  stroke(255,0,0)
  line(200, 200, 200+x, 200+y)
  fill(100, 100)
  arc(200, 200, a/2, a/2, 0, radians(angle))

  
  # Highlight x-movement
  stroke(0,255,0)
  fill(0,255,0)
  circle(200+x, 180-a, 8)
  line(200+x, 180-a, 200+x, 200+y)
  line(200+x, 200, 200, 200)
  push()
  text_size(10)
  fill(0)
  no_stroke()
  text("x = a*cos(radians(angle))", 200+x+45, 180-a+2.5)
  pop()
  
  # Highlight y-movement
  stroke(0,0,255)
  fill(0,0,255)
  circle(180-a, 200+y, 8)
  line(180-a, 200+y, 200+x, 200+y)
  line(200+x, 200, 200+x, 200+y)
  push()
  translate(180-a, 200+y)
  rotate(radians(-90))
  text_size(10)
  fill(0)
  no_stroke()
  text("y = b*sin(radians(angle))", 45, 2.5)
  pop()
  
  # Label x and y movement
  fill(0)
  text("x-movement uses cosine",200,150-a, 120, 50)
  push()
  translate(150-a, 200)
  rotate(radians(-90))
  text("y-movement uses sine",0, 0, 120, 50)
  pop()
  
  # Display angle measurement
  no_stroke()
  fill(255)
  rect(250+a,200,60,30)
  fill(0)
  text(str(angle%360)+"°",250+a,210)
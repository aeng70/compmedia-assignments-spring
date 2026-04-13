timer = 5

def setup():
    size(600,400)

def draw():
    global timer
    background(220)
    #text(str(mouse_x) + ", " + str(mouse_y), 20, 20)
    
    '''
    #this doesn't work because it's all happening at the same time
    while (timer > 0): 
     timer += 1
    '''
    fill(0)
    text_align(CENTER, CENTER)
    text_size(100)
    text(timer, width/2, height/2)
  
    '''
    frame_count --> this keeps track of the number of times the program has gone throught the code, 60 = 1 second
    % ---> this is the Modulo operator, it divides numbers and evaluates to the remainder: 17 % 5 evaluates to 2 remainder
    this can be used to determine if the number on the left is divisible by the number on the right
    '''
    
    # if frame_count % int(get_frame_rate()) ... does not work as well
    if frame_count % 60 == 0 and timer > 0:
      timer -= 1
      
    if (timer == 0):
      text("GAME OVER", width/2, height*0.7);
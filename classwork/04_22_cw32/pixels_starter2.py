pDictionary = {}

def setup():
    size(500,500)
    global img, pDictionary
    img = load_image("PRFlag.jpg")
    
    img.resize(width//2,0)
    image(img,20,20)
    
    load_pixels() #load all pixels of current screen - creates array called pixels
    
    for x in range(width): #loop through every x
        for y in range(height): #loop through every y with every x
            newKey = str(x) + "," + str(y)  #save string "x,y" to create dictionary key name
            pDictionary[newKey] = pixels[x+y*width] #for every newKey, get the color value from pixels and save it to dictionary
    print(pDictionary) #comment out once you've tested this!
    
    print("done") # comment once tested
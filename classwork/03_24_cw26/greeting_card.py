from PIL import Image

def setup():
    size(1920,1080)
    background(0)
    
def draw():
    img = Image.open('rosie_riveter.png')
    resized_img = img.resize((0, img.height // 2))
    resized_img.save('new_rosie.png')
    image(new_rosie,0,0)
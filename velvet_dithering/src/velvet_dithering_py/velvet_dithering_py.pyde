# alexthescott
# translated from https://github.com/danielepiccone/dithering_algorithms/blob/master/ordered/ordered.pde

matrix = [[1,9,3,11],[13,5,15,7],[4,12,2,10],[16,8,14,6]]
mratio = 1.0 / 17
mfactor = 255.0 / 5

file_name = "cat_2.jpg"
src = None

def setup():
    global src
    src = loadImage("cat_2.jpg")
    res = createImage(src.width, src.height, RGB)
    size(768,768)
    noLoop()
    
    
def draw():  
    global src  
    for x in range(src.width):
        for y in range(src.height):
            old_p = src.get(x,y)
            val = color(brightness(old_p) + (mratio*matrix[x%4][y%4] * mfactor))
            new_p = findClosestColor(val)
            src.set(x,y,new_p)
            stroke(new_p)
            point(x,y)
    saveFrame("{}_dither".format(file_name.split(".")[0]))

def findClosestColor(i):
    if brightness(i) < 128:
        return color(0)
    else:
        return color(255)

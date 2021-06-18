# carpet noise -> alexthescott 6/18/21
# three palettes, layered 2D perlin nosie, perfect loop

from random import randint

inc = 2
scl = 20
start = 0.0
n_scale = 0.1
cols = None
rows = None

palettes = [[[7, 59, 76], [255, 209, 102], [236, 136, 5], [6, 214, 160], [17, 229, 236]],
               [[205, 214, 208], [214, 203, 193], [214, 169, 154], [225, 96, 54], [227, 23, 10]],
               [[135, 130, 130], [132, 220, 207], [166, 217, 247], [188, 204, 224], [191, 152, 160]]]

palette_choice = randint(0, len(palettes) - 1) 
palette = palettes[palette_choice]

def setup():
    size(160, 160)
    global rows, cols
    cols = width / scl
    rows = height / scl
    noStroke()
    noiseDetail(2)
    blendMode(DIFFERENCE)
    
def draw():
    global start
    clear()
    background(palette[0][0], palette[0][1], palette[0][2])
    
    yoff_0 = cos(start)
    xoff_0 = sin(start)
    
    yoff_1 = cos(start)
    xoff_1 = sin(start)
    
    for x in range(rows):
        for y in range(cols):
            n1 = noise(xoff_0 / 5.0, yoff_0) * 255
            n2 = noise(xoff_1 / 10.0, yoff_1) * 255
            
            # 'stuttered' blocks
            if n1 <= 96:
                c1 = palette[1]
                c2 = palette[2]
                r = map(x, 0, rows, c1[0], c2[0])
                g = map(x, 0, rows, c1[1], c2[1])
                b = map(x, 0, rows, c1[2], c2[2])
                fill(r, g, b)
                rect(x * scl, y * scl, scl, scl / 2)
            
            # full blocks
            if n2 <= 96:
                c1 = palette[2]
                c2 = palette[3]
                r = map(x, 0, rows, c1[0], c2[0])
                g = map(x, 0, rows, c1[1], c2[1])
                b = map(x, 0, rows, c1[2], c2[2])
                fill(r, g, b)
                rect(y * scl, x * scl, scl, scl)
                
            xoff_0 += inc
            xoff_1 -= inc
            
        yoff_0 += inc
        yoff_1 -= inc
        
    start += radians(inc)
    
    if frameCount <= 180:
        saveFrame()
    else:
        noLoop()

def mouseClicked():
    noiseSeed(frameCount)
    global palette, palette_choice, start
    temp_choice = palette_choice
    palette_choice = randint(0, len(palettes) - 1)
    while palette_choice == temp_choice:
        palette_choice = randint(0, len(palettes) - 1)
    palette = palettes[palette_choice]

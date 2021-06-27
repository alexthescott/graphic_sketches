# alexthescott, 6/24/21
# a grid of triangles is draw, with a new the orientation upon activated by the mouse, or by a perlin noise position
# if activated, the triangles are drawn with full bightness, and these triangles slowly fade away into the black background

from random import randint

tile_size = 50
tiles = []
time = 0
time_vel = 0.02
noise_x = None
noise_y = None
m_x = 0
m_y = 0
mouse_still = 61
mouse_moved = False

def setup():
    size(400, 400)
    for x in range(width // tile_size):
        temp_tiles = []
        for y in range(1, 1 + height // tile_size):
            temp_tiles.append(tile(x, y))
        tiles.append(temp_tiles)
    noiseDetail(2)
    colorMode(HSB, 100)
    strokeJoin(ROUND)
    
def draw():
    global m_x, m_y, tile_size, mouse_moved, mouse_still, time
    clear()
    background(0, 0, 0)
    noStroke()
    noFill()
    
    noise_x = int(map(noise(time), 0, 1, 0, 1 + width / tile_size))
    noise_y = int(map(noise(time+1), 0, 1, 1, 1 + height / tile_size))
    
    old_m_x, m_x, = m_x, mouseX / tile_size
    old_m_y, m_y, = m_y, mouseY / tile_size
    
    if m_x == old_m_x and m_y == old_m_y:
        mouse_still += 1
    else:
        mouse_still = 0
    
    translate(width / 10.0, height / 10.0)
    scale(0.8, 0.8)
    for x in range(len(tiles)):
        for y in range(len(tiles[0])):
            tiles[x][y].update((x == noise_x and y == noise_y) or (mouse_moved == True and x == m_x and y == m_y))
            tiles[x][y].draw()
            
    mouse_moved = mouse_still <= 60
    
    resetMatrix()
    noFill()
    strokeWeight(10)
    stroke(0, 0, map(noise(time / 2), -1, 1, 50, 100))
    strokeWeight(50)
    square(0, 0, width)
    
    time += time_vel
            
class tile():
    def __init__(self, x, y):
        self.x = x * tile_size
        self.y = y * tile_size
        self.ori = randint(0, 3)
        self.new_ori = False
        self.glow = 0.0
        
    def __str__(self):
        return "{:3} {:3} {} {}".format(self.x, self.y, self.ori, self.glow)
        
    def update(self, found):
        if found:
            if self.new_ori == False:
                self.ori = randint(0, 3)
                self.new_ori = True
                self.glow = 100.0
        else:
            self.new_ori = False
            if self.glow > 0:
                self.glow -= self.glow / 100.0
    
    def draw(self):
        fill(self.glow)
        if self.ori == 0: 
            # top left
            triangle(self.x, self.y, self.x, self.y-tile_size, self.x+tile_size, self.y-tile_size)
        elif self.ori == 1:
            # top right
            triangle(self.x+tile_size, self.y, self.x, self.y-tile_size, self.x+tile_size, self.y-tile_size)
        elif self.ori == 2:
            # bottom right
            triangle(self.x, self.y, self.x+tile_size, self.y-tile_size, self.x+tile_size, self.y)
        else:
            #bottom left
            triangle(self.x, self.y, self.x, self.y-tile_size, self.x+tile_size, self.y)

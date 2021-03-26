""" everything becomes nothing.py -> Alex Scott 3/26/21  

After chosing one of five color palettes, circle grows and shrinks
as the background and circle swap between colors. Works best if 
color list is an odd length
"""

from random import randint

colors = [["#EF476F", "#FFD166", "#06D6A0"],
        ["#1DBDE6", "#8787A2", "#F1515E"],
        ["#46B83D", "#2C6B24", "#111E0B"],
        ["#F9A470", "#DB7D70", "#BC556F"],
        ["#ECDEC4", "#A7E9DF", "#62F4F9"]];

choice = randint(0, len(colors)-1)
palette = colors[choice]

def setup():
    size(400, 400)
    global ball_object
    ball_object = grow_shrink_circle(palette)
    noStroke()

def draw():
    global ball_object
    ball_object.draw()
    
def update_index(index, list_size):
    if index >= list_size - 1:
        return 0
    else:
        return index + 1 
    
class grow_shrink_circle():
    def __init__(self, palette):
        self.palette = palette
        self.bg_color_i = 0
        self.color_i = 1
        self.bg_color = self.palette[self.bg_color_i]
        self.color = self.palette[self.color_i]
        self.r = 0
        self.vel = 0
        self.acc = 0 
        self.max_acc = 5
        self.max_vel = 10
        self.x = width / 2
        self.y = height / 2
        self.max_size = sqrt((width * width) + (height * height))
        self.grow = True
    
    def draw(self):
        background(self.bg_color)
        fill(self.color)
        circle(self.x, self.y, self.r)
    
        if self.grow:
            if self.r >= self.max_size:
                self.bg_color_i = update_index(self.bg_color_i, len(self.palette))
                self.bg_color_i = update_index(self.bg_color_i, len(self.palette))
                self.bg_color = self.palette[self.bg_color_i]
                self.r = self.max_size
                self.acc = 0
                self.vel = 0
                self.grow = False
            if self.acc < self.max_acc:
                self.acc += 0.0006
        else:
            if self.r <= 0:
                self.color_i = update_index(self.color_i, len(self.palette))
                self.color_i = update_index(self.color_i, len(self.palette))
                self.color = self.palette[self.color_i]
                self.r = 0
                self.acc = 0
                self.vel = 0
                self.grow = True
                print(frameCount)
            if self.acc < self.max_acc:
                self.acc -= 0.0006
        
        if self.vel < self.max_vel:
            self.vel += self.acc
            
        self.r += self.vel
    

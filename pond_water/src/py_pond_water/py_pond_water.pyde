import random

colors = [["#E63946", "#4CC9F0"],
        ["#023047", "#FFB703"],
        ["#081c15", "#52b788"],
        ["#deaaff", "#c0fdff"],
        ["#fb5607", "#ff006e"],
        ["#355070", "#b56576"]]

palette_choice = random.randint(0, len(colors)-1)
palette = colors[palette_choice]

# decide if ripple color and bg color should be flipped
bg_flip = random.randint(0, 1)
bg = None
ripple_clor = None

if bg_flip == 0:
    bg = palette[0]
    ripple_color = palette[1]
else:
    bg = palette[1]
    ripple_color = palette[0]
    
# 3 ripples, avoid one corner
avoid_pos = random.randint(0, 3)

ripples = []

def setup():
    size(400, 400)
    for i in range(4):
        if i != avoid_pos:
            ripples.append(ripple(i))
    noFill()
    
def draw():
    background(bg)
    stroke(ripple_color)
    # framed rectangle around the canvas
    strokeWeight(12)
    rect(0, 0, width, height)
    # draw all ripples
    strokeWeight(5)
    for ripple in ripples:
        ripple.draw()
    
class ripple():
    def __init__(self, pos):
        self.ripples = []
        self.speed = 0.4
        self.max_size = 2.25 * ((width * width) + (height * height)) ** 0.5
        self.spawn_rate = 5
        
        ripple_gap = self.speed * self.spawn_rate * 60
        num_of_ripples = int(1 + self.max_size / ripple_gap)
        
        # prepopulate the ripples
        for i in range(num_of_ripples, -1, -1):
            self.ripples.insert(0, i * ripple_gap)
        
        # decide corner to draw from
        if pos == 0:
            self.x = -width/10
            self.y = -height/10
        elif pos == 1:
            self.x = width + width/10
            self.y = -height/10
        elif pos == 2:
            self.x = -width/10
            self.y = height + height/10
        else:
            self.x = width + width/10
            self.y = height + height/10
        
    def draw(self):
        # spawn new ripples at a regular frequency
        if frameCount % (self.spawn_rate * 60) == 0:
            self.ripples.insert(0, 0.0)
        
        removed = 0
        for i, ripple in enumerate(self.ripples):
            # pop from list if ripple is too large
            if ripple >= self.max_size:
               del self.ripples[-1]
               removed += 1
            
            # draw and grow ripple
            circle(self.x, self.y, ripple)
            self.ripples[i-removed] += self.speed

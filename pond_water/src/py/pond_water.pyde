import random

colors = [["#E63946", "#4CC9F0"],
        ["#023047", "#FFB703"],
        ["#081c15", "#52b788"],
        ["#deaaff", "#c0fdff"],
        ["#fb5607", "#ff006e"],
        ["#355070", "#b56576"]]

palette_choice = random.randint(0, len(colors)-1)
palette = colors[palette_choice]

ripples = []

def setup():
    size(400, 400)
    for i in range(3):
        ripples.append(ripple(i))
    noFill()
    stroke(palette[1])
    strokeWeight(5)
    
def draw():
    background(palette[0])
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
        
        for i in range(num_of_ripples, -1, -1):
            self.ripples.insert(0, i * ripple_gap)
        
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
        if frameCount % (self.spawn_rate * 60) == 0:
            self.ripples.insert(0, 0.0)
        
        removed = 0
        for i, ripple in enumerate(self.ripples):
            if ripple >= self.max_size:
               del self.ripples[-1]
               removed += 1
       
            circle(self.x, self.y, ripple)
            self.ripples[i-removed] += self.speed

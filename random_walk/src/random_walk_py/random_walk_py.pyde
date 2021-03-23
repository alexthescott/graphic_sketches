from random import randint

def setup():
    size(500, 667)
    background(255)
    frameRate(20)
    strokeCap(SQUARE)
    strokeJoin(BEVEL)
    global walker
    walker = RandomWalk()
    
def draw():
    background(255)
    global walker
    walker.show()
    
class RandomWalk():
    def __init__(self):
        self.steps = 100
        self.max_size = max(width, height)
        self.min_size = min(width, height)
        self.border = self.min_size / 10
        self.front_x = randint(self.border, width - self.border)
        self.front_y = randint(self.border, height - self.border)
        self.points = [[self.front_x, self.front_y]]
        self.stroke_weights = []
        self.orientation = randint(0, 1)
        self.vert_const = 2
        self.hori_const = 2
        
    def show(self):
        self.update()
        for i in range(len(self.points) - 1):
            point_a = self.points[i]
            point_b = self.points[i + 1]
            strokeWeight(self.stroke_weights[i])
            line(point_a[0], point_a[1], point_b[0], point_b[1])
            
    def update(self):
        if self.steps > 0:
            # 0 -> up, 1 -> down, 2 -> right, 3 -> left
            direction = None
            weight = 1
            
            if self.orientation == 0:
                direction = randint(0, 1)
                # 14% chance for vertical to have thicker stroke
                weight = randint(3, 6) if randint(0, 50) < 7 else 1
            else:
                direction = randint(2, 3)
                # 50% chance for horizontal line have thicker stroke
                weight = randint(3, 6) if randint(0, 1) == 1 else 1
            
            new_x = self.front_x
            new_y = self.front_y
            
            if direction == 0:
                distance = ((self.front_y - self.border) // self.vert_const)
                line_len = randint(0, distance)
                new_y -= line_len
            elif direction == 1:
                distance = ((height - self.front_y - self.border) // self.vert_const)
                line_len = randint(0, distance)
                new_y += line_len
            elif direction == 2:
                distance = ((width - self.front_x - self.border) // self.hori_const)
                line_len = randint(0, distance)
                new_x += line_len
            elif direction == 3:
                distance = ((self.front_x - self.border) // self.hori_const)
                line_len = randint(0, distance)
                new_x -= line_len
            
            self.points.append([new_x, new_y])
            self.stroke_weights.append(weight)
            self.front_x = new_x
            self.front_y = new_y
            self.orientation = 1 if self.orientation == 0 else 0
            self.steps -= 1
        elif self.steps > -100:
            self.steps -= 1
        else:
            self.steps = 100
            self.points = [[self.front_x, self.front_y]]
                
                    

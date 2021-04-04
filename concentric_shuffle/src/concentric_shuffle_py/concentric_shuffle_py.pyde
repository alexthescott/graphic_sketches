from random import shuffle, randint

sticks = []
meta_info = []
circle_count = 4
sticks_count = 108 if randint(0, 1) == 0 else 72

palettes = [[(0, 78, 204), (48, 168, 255), (60, 186, 255), (72, 204, 255), (96, 239, 255)],
            [(8, 28, 21), (64, 145, 108), (82, 183, 136), (116, 198, 157), (216, 243, 220)],
            [(143, 0, 64), (252, 85, 82), (250, 120, 62), (249, 138, 52), (248, 155, 41)],
            [(68, 162, 2), (147, 223, 14), (205, 236, 25), (222, 240, 25), (245, 248, 99)],
            [(235, 51, 57), (245, 167, 130), (247, 212, 134), (238, 227, 170), (197, 249, 215)]]

palette = palettes[randint(0, len(palettes)-1)]

def setup():
    r, g, b = palette[0]
    background(r, g, b)
    stroke(255)
    size(400, 400)
    for c in range(1, circle_count+1):
        stick_angle = 0.0
        angle_step = TWO_PI / (sticks_count / circle_count)
        draw_color = palette[c]
        for i in range(sticks_count / circle_count):
            x_pos = map(cos(stick_angle), -1, 1, width/10.0*c, width-width/10.0*c)
            y_pos = map(sin(stick_angle), -1, 1, height/10.0*c, height-height/10.0*c)
            pos = PVector(x_pos, y_pos)
            pos_copy = pos.copy()
            new_stick = Stick(pos, stick_angle, draw_color)
            sticks.append(new_stick)
            meta_info.append([pos_copy, stick_angle, draw_color])
            stick_angle += angle_step
    shuffle(meta_info)
    # meta_info[0], meta_info[1] = meta_info[1], meta_info[0]

def draw():
    r, g, b = palette[0]
    background(r, g, b)
    stroke(255)
    global flip
    for s in sticks:
        s.draw()
    
    if frameCount % 240 == 0:
        for i, s in enumerate(sticks):
            s.goal = meta_info[i][0]
            s.goal_angle = meta_info[i][1]
            s.goal_color = meta_info[i][2]
            s.new_goal = True
        shuffle(meta_info)
        
    if frameCount == 300:
        saveFrame()
    
class Stick():
    def __init__(self, pos, angle, draw_color):
        self.len = 15
        self.pos = pos
        self.pos_start = self.pos
        self.goal = pos
        self.new_goal = False
        self.angle = angle
        self.goal_angle = angle
        self.end_t = 2.0 * frameRate
        self.start_t = self.end_t
        self.draw_color = draw_color
        self.goal_color = draw_color

    def draw(self):
        x_len = (cos(self.angle) * self.len) / 2
        y_len = (sin(self.angle) * self.len) / 2
        start_x = self.pos.x - x_len
        start_y = self.pos.y - y_len
        end_x = self.pos.x + x_len
        end_y = self.pos.y + y_len
        
        # strokeWeight(1) # DEBUG
        # stroke(100)
        # line(self.goal.x, self.goal.y, self.pos.x, self.pos.y)
        
        strokeWeight(6)
        # draw the line!
        r, g, b = self.draw_color
        stroke(r, g, b)
        line(start_x, start_y, end_x, end_y)
        
        self.update()
        
    def update(self):
        if self.new_goal:
            self.start_t = 0.0
            self.pos_start = self.pos
            self.new_goal = False
        
        if self.pos != self.goal:
            percent = self.start_t / self.end_t
            x_dist = map(percent, 0, 1, self.pos_start.x, self.goal.x)
            y_dist = map(percent, 0, 1, self.pos_start.y, self.goal.y)
            angle_dist = map(percent, 0, 2, self.angle, self.goal_angle)
            self.pos.x = x_dist
            self.pos.y = y_dist
            self.angle = angle_dist
            
            cur_r, cur_g, cur_b = self.draw_color
            goal_r, goal_g, goal_b = self.goal_color
            
            new_r = map(percent, 0, 1, cur_r, goal_r)
            new_g = map(percent, 0, 1, cur_g, goal_g)
            new_b = map(percent, 0, 1, cur_b, goal_b)
            
            self.draw_color = (new_r, new_g, new_b)
            
            self.start_t += 0.1
        
def angle_between(o, p):
    # given two PVectors, return the angle from the origin to the point relative to the x-axis
    delta_y = p.y - o.y
    delta_x = p.x - o.x
    angle = atan2(delta_y, delta_x)
    return angle
        
        

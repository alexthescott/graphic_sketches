from random import randint

colors = [["#586F6B", "#7F9183", "#B8B8AA", "#CFC0BD", "#DDD5D0"],
              ["#53599A", "#068D9D", "#6D9DC5", "#80DED9", "#AEECEF"],
              ["#F4AFAB", "#F4CBC6", "#F7EDF0", "#F4F482", "#F4EEA9"],
              ["#401712", "#3B52A5", "#D95D39", "#F18805", "#F0A202"],
              ["#191716", "#D83137", "#804D54", "#B592A0", "#C6B8CC"]]

choice = randint(0, len(colors)-1)
palette = colors[choice]

circles = []

def setup():
    size(200, 200)
    background(palette[0])
    strokeWeight(4)
    for i in range(4):
        ball_size = (i + 1) * 4
        new_ball = ball(ball_size, palette[i+1])
        circles.append(new_ball)

def draw():
    background(palette[0])
    for c in circles:
        c.draw()
        
class ball:
    def __init__(self, d, ball_color):
        self.ball_color = ball_color
        self.r = d / 2
        self.x = random(self.r * 2, width - self.r * 2)
        self.y = random(self.r * 2, height - self.r * 2)
        self.dir = random(10, 350)
        self.x_vel = cos(self.dir) * 3
        self.y_vel = sin(self.dir) * 3
        self.line_p = [[self.x, self.y]]
        self.line_vel = [[self.x_vel, self.y_vel]]
        self.line_delay = 3
        
    def draw(self):
        fill(self.ball_color)
        noStroke()
        circle(self.x, self.y, self.r * 2)
        stroke(self.ball_color)
        
        # before the first bouce, attach the line to the pos
        if len(self.line_p) == 0:
            line(self.line_p[0][0], self.line_p[0][1], self.x, self.y)
        
        else:
            for i in range(len(self.line_p) - 1):
                past_point = self.line_p[i]
                new_point = self.line_p[i + 1]
                line(past_point[0], past_point[1], new_point[0], new_point[1])
            last_point = self.line_p[-1]
            line(last_point[0], last_point[1], self.x, self.y)
        
        # update pos
        if self.x <= self.r or self.x >= width - self.r:
            self.x_vel *= -1
            self.line_p.append([self.x, self.y])
            self.line_vel.append([self.x_vel, self.y_vel])
        
        if self.y <= self.r or self.y >= height - self.r:
            self.y_vel *= -1
            self.line_p.append([self.x, self.y])
            self.line_vel.append([self.x_vel, self.y_vel])
        
        # update the position of the old trail after self.line_delay seconds
        if millis() >= self.line_delay * 1000:
            # remove from the list if the trail 'bounces' off the wall
            if self.line_p[0][0] <= self.r or self.line_p[0][0] >= width - self.r:
                self.line_vel.pop(0)
                self.line_p.pop(0)
            
            if self.line_p[0][1] <= self.r or self.line_p[0][1] >= height - self.r:
                self.line_vel.pop(0)
                self.line_p.pop(0)
            
            self.line_p[0][0] += self.line_vel[0][0]
            self.line_p[0][1] += self.line_vel[0][1]
        
        self.x += self.x_vel
        self.y += self.y_vel
            
        
        
        

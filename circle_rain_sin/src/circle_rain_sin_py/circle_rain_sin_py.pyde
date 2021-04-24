# alexthescott 4/24/21
# Attempt at a faithful recreation of the sketch linked below! 
# https://twitter.com/beesandbombs/status/1385611174704713728

time = 0
vel = TWO_PI / 300
hori_count = 14
vert_count = 7
colors = ["#F94144", "#F65A38", "#F3722C",
              "#F68425", "#F8961E", "#F9AF37",
              "#F9C74F", "#C5C35E", "#90BE6D",
              "#6AB47C", "#43AA8B", "#4D908E",
              "#52838F", "#577590"]
def setup():
    size(400, 400)
    noFill()
    strokeWeight(3)
    blendMode(SCREEN)

def draw():
    global time
    clear()
    background(0, 0, 32)
    for y in range(vert_count):
        for t in range(hori_count):
            y_pos = map(sin(time + t / 6.0 + y / 2.0), -1, 1, width * 0.1875, width - (width * 0.1875))
            x_pos = map(y, 0, vert_count - 1, height * 0.125, height - (height * 0.125))  
            stroke(colors[t])
            circle(x_pos, y_pos, 35)
    time += vel

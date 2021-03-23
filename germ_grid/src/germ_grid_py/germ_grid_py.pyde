from random import randint

colors = [["#F45D52", "#2E86AB"],
        ["#59344F", "#8BBF9F"],
        ["#E8E9F3", "#272635"],
        ["#2D0320", "#6C969D"],
        ["#C36F09", "#F4E409"],
        ["#F2F5DE", "#86E7B8"]];

palette_choice = randint(0, len(colors)-1)
palette = colors[palette_choice]

if randint(0, 1) == 00:
    bg = palette[0]
    ball_color = palette[1]
    shadow_color = color(unhex(palette[1][1:]), 100)
else:
    bg = palette[1]
    ball_color = palette[0]
    shadow_color = color(unhex(palette[0][1:]), 100)

def setup():
    size(400, 400)
    strokeWeight(25)
    background(bg)
    noiseDetail(4)
    
gridHeight = 7
gridWidth = 7
cellSize = 50
a_off = 0
a_speed = 0.25

def draw():
    global a_off
    background(bg)
    noFill()
    stroke(ball_color)
    rect(0, 0, width, height)
    xOffset = (width - gridWidth * cellSize) / 2 + cellSize / 2
    yOffset = (height - gridHeight * cellSize) / 2 + cellSize / 2
    translate(xOffset, yOffset)
    for y in range(gridHeight):
        for x in range(gridWidth):
            x_off = cos(a_off)
            y_off = sin(a_off)
            n = noise(x_off + x / 1.9, y_off + y / 1.9)
            n_map = map(n, 0, 1, -1.75, 1.75)
            shadow_pos = map(n, 0, 1, 2, 4)
            noStroke()
            fill(shadow_color)
            circle(x * cellSize + shadow_pos, y * cellSize + shadow_pos, n_map * cellSize)
            fill(ball_color)
            circle(x * cellSize, y * cellSize, n_map * cellSize)
    a_off += radians(a_speed)

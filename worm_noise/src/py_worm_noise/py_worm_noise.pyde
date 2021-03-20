time = 0
speed = TWO_PI/720
inc = 0.01
strokeAmount = 12

from random import randint

colors = [["#F0F7F4", "#3C493F"],
        ["#3C493F", "#FFFFFF"],
        ["#373F51", "#008DD5"],
        ["#94849B", "#7E9181"],
        ["#D4AA7D", "#EFD09E"],
        ["#525B76", "#869D96"]];

palette_choice = randint(0, len(colors)-1)
palette = colors[palette_choice]

if randint(0, 1) == 0:
    bg = palette[0]
    fill_color = palette[1]
else:
    bg = palette[1]
    fill_color = palette[0]

def setup():
    size(400, 400, FX2D)
    frameRate(60)
    background(bg)
    noiseDetail(2)

def draw():
    global top_start, bottom_start, time, inc
    background(bg)
    beginShape()
    stroke(0)
    strokeWeight(strokeAmount)
    fill(fill_color)
    line_off = 0
    for x in range(-strokeAmount, width+strokeAmount):
        time_x = cos(time)
        time_y = sin(time)
        top_noise = noise(line_off, time_x, time_y)
        pos = map(top_noise, 0, 1, 0, height / 2)
        vertex(x, pos)
        time -= inc
        line_off += inc
    line_off = 0
    for x in range(-strokeAmount, width+strokeAmount):
        time_x = cos(time)
        time_y = sin(time)
        bottom_noise = noise(line_off, time_y, time_x)
        pos = map(bottom_noise, 0, 1, height / 2, height)
        vertex(width-x+strokeAmount, pos)
        time += inc
        line_off += inc
    endShape()
    time += speed

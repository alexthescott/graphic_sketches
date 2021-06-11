# Alex Scott - 5/25/21, recreating, and remixing @mattdesl's boxes -- front  
#   -> https://twitter.com/mattdesl/status/1396876632594554887
# 
# threw my occasional twist on things
#   - 50% chance for an alternate palette
#   - 25% chance for a squircle shape, instead of a sharp line
#   - 20% chance for a alternate blending mode (10% for multiply, 10% for hard_light)

import random

border = 72
obj_count = 16
obj_size = 16
obj_limit = 32
objs = []

og_palette = ["#000000", "#FFFFFF", "#9A9899", "#3C5DE7", "#B0587C",
                "#F6521C", "#FF9204", "#FCC400", "#4C9A1B", "#B68817"]

alt_palette = ["#000000", "#FFFFFF", "#F94144", "#F3722C", "#F8961E",
                  "#F9844A", "#F9C74F", "#90BE6D", "#43AA8B", "#4D908E",
                  "#577590", "#277DA1"]

palette = og_palette if random.random() >= 0.25 else alt_palette
squircle = random.random() <= 0.25
blend_chance = random.random()

def get_size():
    return (random.randint(1, 4), random.randint(1, 4))

def get_pos(size):
    return (random.randint(0, 16 - size[0]), random.randint(0, 16 - size[1]))

def get_color_index(palette):
    return palette[random.randint(0, len(palette) - 1)]

def setup():
    size(4 * 100, 4 * 100)
    
    if blend_chance <= 0.1:
        blendMode(MULTIPLY)
    elif blend_chance <= 0.2:
        blendMode(HARD_LIGHT)
    
    for i in range(obj_limit):
        new_size = get_size()
        new_pos = get_pos(new_size)
        new_color = get_color_index(palette)
        objs.append([new_pos, new_size, new_color])
        
    noStroke()
    
def draw():
    clear()
    background("#EAE2D4")
    
    if frameCount % 4 == 0:
        new_size = get_size()
        new_pos = get_pos(new_size)
        new_color = get_color_index(palette)
        objs.append([new_pos, new_size, new_color])
        if len(objs) > obj_limit:
            del objs[0]
    
    for i in range(len(objs)):
        pos = objs[i][0]
        sze = objs[i][1]
        color = objs[i][2]
        fill("{}".format(color))
        if squircle:
            rect(72 + pos[0] * obj_size, 72 + pos[1] * obj_size, sze[0] * obj_size, sze[1] * obj_size, 5)
        else:
            rect(72 + pos[0] * obj_size,72 + pos[1] * obj_size, sze[0] * obj_size, sze[1] * obj_size)

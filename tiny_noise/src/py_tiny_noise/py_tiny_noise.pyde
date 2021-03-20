# tiny noise
# Alex Scott, 2020
# -> ... cell_size / (width || height) must be an int

from random import randint

cell_size = 8
noise_const = 0.05
time = 0 
time_vel = 1
time_frailty = 20 # how much should time move noise?
slant = map(random(0, 1), 0, 1, -2, 2)

palettes = [['#273043', '#F02D3A', '#EFF6EE'],
            ['#1E2019', '#E2C044', '#587B7F'],
            ['#15A0A2', '#4A8FE7', '#44E5E7'],
            ['#5C95FF', '#B9E6FF', '#F87575'],
            ['#2C302E', '#474A48', '#909590'],
            ['#243010', '#829E2E', '#AFCC66']]

palette_choice = randint(0, len(palettes)-1)
palette = palettes[palette_choice]

def setup():
    size(400, 400)
    noStroke()
    noiseDetail(3)
    
def draw():
    global time, time_vel
    background(palette[0])
    x_grid = width // cell_size
    y_grid = height // cell_size
    
    x_cir = cos(time)
    y_cir = sin(time)
    z_pos = x_cir+y_cir
    for x in range(x_grid):
        for y in range(y_grid):
            x_off = x * noise_const / slant if slant != 0 else x * noise_const
            y_off = y * noise_const * slant if slant != 0 else y * noise_const 
            
            x_pos = float(x) / time_frailty
            y_pos = float(y) / time_frailty

            c = noise(x_pos, y_pos, z_pos)
    
            if c >= 0.55:
                fill(palette[1])
                square(x * cell_size, y * cell_size, cell_size)
            elif c > 0.45:
                fill(palette[2])
                square(x * cell_size, y * cell_size, cell_size)
    time += radians(time_vel)
    

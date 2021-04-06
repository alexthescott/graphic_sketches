// concentric_shuffle.js -> alexthescott 4/5/20

let palettes = [[[0, 78, 204], [48, 168, 255], [60, 186, 255], [72, 204, 255], [96, 239, 255]],
            [[8, 28, 21], [64, 145, 108], [82, 183, 136], [116, 198, 157], [216, 243, 220]],
            [[143, 0, 64], [252, 85, 82], [250, 120, 62], [249, 138, 52], [248, 155, 41]],
            [[68, 162, 2], [147, 223, 14], [205, 236, 25], [222, 240, 25], [245, 248, 99]],
            [[235, 51, 57], [245, 167, 130], [247, 212, 134], [238, 227, 170], [197, 249, 215]]]

var sticks = []
var meta_info = []
var circle_count = 4
var sticks_count = 0
var palette_choice = 0
var palette = []

function setup() {
  sticks_count = (random() <= 0.5) ? 108 : 72 
  
  // pick one of 5 colors
  palette_choice = randint(0, palettes.length - 1)
  palette = palettes[palette_choice]

  var r = palette[0][0]
  var g = palette[0][1]
  var b = palette[0][2]
  
  angleMode(RADIANS)
  createCanvas(400, 400)
  background(r, g, b)  
  strokeWeight(6)
  for(var c = 1; c < circle_count + 1; c++){
    var stick_angle = 0.0
    var angle_step = TWO_PI / (sticks_count / circle_count)
    var draw_color = palette[c]
    for(var i = 0; i < sticks_count / circle_count; i++){
      var x_pos = map(cos(stick_angle), -1, 1, width/10 * c, width-width/10 * c)
      var y_pos = map(sin(stick_angle), -1, 1, height/10 * c, width-height/10 * c)
      var pos = createVector(x_pos, y_pos)
      sticks.push(new stick(pos, stick_angle, draw_color))
      meta_info.push([pos.copy(), stick_angle, draw_color])
      stick_angle += angle_step
    }
  }
  meta_info = shuffle_list(meta_info)
}

function draw() {
  var r = palette[0][0]
  var g = palette[0][1]
  var b = palette[0][2]
  
  background(r, g, b);
  
  for (var i = 0; i < sticks_count; i++){
    sticks[i].draw()
  }
  if (frameCount % 240 == 0){
    for (var i = 0; i < sticks_count; i++){
      sticks[i].new_goal = true
      sticks[i].goal = meta_info[i][0]
      sticks[i].goal_angle = meta_info[i][1]
      sticks[i].goal_color = meta_info[i][2]
    }
    meta_info = shuffle_list(meta_info)
  }
}

class stick {
  constructor(pos, angle, draw_color){
    this.len = 10
    this.pos = pos
    this.pos_start = this.pos
    this.angle = angle 
    this.goal_angle = angle
    this.new_goal = false
    this.end_t = 2 * 60
    this.start_t = this.end_t
    this.draw_color = draw_color
    this.goal_color = draw_color
  }
  
  draw(){
    var x_len = (cos(this.angle) * this.len) / 2
    var y_len = (sin(this.angle) * this.len) / 2
    var s_x = this.pos.x - x_len
    var s_y = this.pos.y - y_len
    var e_x = this.pos.x + x_len
    var e_y = this.pos.y + y_len
    stroke(this.draw_color)
    line(s_x, s_y, e_x, e_y)
    this.update()
  }
  
  update(){
    if (this.new_goal){
      this.start_t = 0
      this.pos_start = this.pos
      this.new_goal = false
    }
    
    if (this.start_t < this.end_t){
      var percent = this.start_t / this.end_t
      var x_dist = map(percent, 0, 1, this.pos_start.x, this.goal.x)
      var y_dist = map(percent, 0, 1, this.pos_start.y, this.goal.y)
      var angle_dist = map(percent, 0, 1, this.angle, this.goal_angle)
      this.pos.x = x_dist
      this.pos.y = y_dist
      this.angle = angle_dist
      
      var cur_r = this.draw_color[0]
      var cur_g = this.draw_color[1]
      var cur_b = this.draw_color[2]
      var goal_r = this.goal_color[0]
      var goal_g = this.goal_color[1]
      var goal_b = this.goal_color[2]
      var new_r = map(percent, 0, 1, cur_r, goal_r)
      var new_g = map(percent, 0, 1, cur_g, goal_g)
      var new_b = map(percent, 0, 1, cur_b, goal_b)
      this.draw_color = [new_r, new_g, new_b]
      
      this.start_t = this.start_t + 0.2
    }
  }
}

function randint(min, max){
  // min and max should are inclusive
  return Math.floor(Math.random() * Math.floor(1+max-min)) + min
}

function shuffle_list(the_array){
  // https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm
  let end = the_array.length
  let new_list = the_array.slice()
  for(var i = 0; i < end; i++){
    let swap_i = randint(i, end-1) 
    let temp_var = new_list[i]
    new_list[i] = new_list[swap_i]
    new_list[swap_i] = temp_var
  }
  return new_list
}
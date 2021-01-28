var colors = [["#000000", "#7D80DA", "#62C370", "#CC3363"],
             ["#000000", "#613F75", "#E5C3D1", "#EF798A"],
             ["#000000", "#FFE66D", "#4ECDC4", "#F7FFF7"],
             ["#FFFFFF", "#5BC0EB", "#DB4E41", "#211A1E"],
             ["#FFFFFF", "#7D80DA", "#62C370", "#CC3363"],
             ["#FFFFFF", "#744FC6", "#4F86C6", "#379392"]
             ];

var choice = Math.floor(Math.random() * colors.length);
var num_fishes = 2 + Math.floor(Math.random() * 2);
var fishes = [];
var palette = colors[choice];

function setup() {
  createCanvas(400, 400);
  var angle = 360 / num_fishes;
  for (var i = 0; i < num_fishes; i++){
    var fish_angle = angle * i;
    var fish_color = palette[i+1];
    fishes[i] = new fish(width/2-20, 0.5, fish_angle, fish_color);
  }
  noFill();
  strokeWeight(6);
}

function draw() {
  background(palette[0]);
  for (var i = 0; i < num_fishes; i++){
    var temp_fish = fishes[i];
    temp_fish.draw();
  }
}

class fish {
  constructor(r_rot, speed, angle, palette) {
    this.ripple_color = color(palette);
    this.x = 0;
    this.y = 0;
    this.r_rot = r_rot;
    this.speed = speed;
    this.angle = angle;
    this.ripple_pos = [];
    this.ripple_size = [];
    this.ripple_speed = 0.5;
    this.ripple_fade = 1+1/(4-num_fishes);
    this.max_size = Math.sqrt((width * width) + (height * height)) / this.ripple_fade;
    setInterval(() => this.new_ripple(), 700);
  }
  
  new_ripple(){
    this.ripple_pos.push([this.x, this.y]);
    this.ripple_size.push(0);
  }

  draw() {
    for(var i = 0; i < this.ripple_pos.length; i++){
      var rip_x = this.ripple_pos[i][0];
      var rip_y = this.ripple_pos[i][1];
      this.ripple_size[i] += this.ripple_speed;
      var temp_color = this.ripple_color;
      var temp_alpha = map(this.ripple_size[i], 0, this.max_size, 255, 0);
      temp_color.setAlpha(temp_alpha);
      stroke(temp_color);
      if (this.ripple_size[i] > this.max_size){
        this.ripple_size.splice(i, 1);
        this.ripple_pos.splice(i, 1);
      }
      circle(rip_x, rip_y, this.ripple_size[i]);
    }
    this.update();
  }
  
  update() {
    this.angle += this.speed;
    this.x = this.r_rot * cos(radians(this.angle)) + width / 2;
    this.y = this.r_rot * sin(radians(this.angle)) + height / 2;
  }
}
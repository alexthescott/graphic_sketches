/* everything becomes nothing -> Alex Scott 1/21/21  

After chosing one of five color palettes, circle grows and shrinks
as the background and circle swap between colors. Works best if 
color list is an odd length
*/

var colors = [["#EF476F", "#FFD166", "#06D6A0"],
              ["#1DBDE6", "#8787A2", "#F1515E"],
              ["#46B83D", "#2C6B24", "#111E0B"],
              ["#F9A470", "#DB7D70", "#BC556F"],
              ["#ECDEC4", "#A7E9DF", "#62F4F9"]];

var choice = Math.floor(Math.random() * (colors.length));
var palette = colors[choice];

function setup() {
  createCanvas(500, 500);
  ball_object = new grow_shrink_circle(palette);
  noStroke();
}

function draw() {
  ball_object.draw();
}

class grow_shrink_circle{
  constructor(new_palette){
    this.palette = new_palette;
    this.bg_color_i = 0;
    this.color_i = 1;
    this.bg_color = this.palette[this.bg_color_i];
    this.color = this.palette[this.color_i];
    this.r = 0;
    this.vel = 0;
    this.acc = 0;
    this.max_acc = 5;
    this.max_vel = 10;
    this.x = width / 2;
    this.y = height / 2;
    this.max_size = Math.sqrt((width * width) + (height * height));
    this.grow = true;
  }
  
  draw(){
    background(this.bg_color);
    fill(this.color);
    circle(this.x, this.y, this.r);
    this.update();
  }
  
  update(){
    // when we grow, acc should be positive, and reset once we've hit the edge
    if (this.grow){
      if (this.r >= this.max_size){
        this.bg_color_i = this.update_index(this.bg_color_i, this.palette.length);
        this.bg_color_i = this.update_index(this.bg_color_i, this.palette.length);
        this.bg_color = this.palette[this.bg_color_i];
        this.r = this.max_size;
        this.acc = 0;
        this.vel = 0;
        this.grow = false;
      }
      if (this.acc < this.max_acc){
        this.acc += 0.0002;
      }
    } 
    // when we shrink, acc should be negative, and reset once the ball has totally shrunk
    else {
      if (this.r <= 0){
        this.color_i = this.update_index(this.color_i, this.palette.length);
        this.color_i = this.update_index(this.color_i, this.palette.length);
        this.color = this.palette[this.color_i];
        this.r = 0;
        this.acc = 0;
        this.vel = 0;
        this.grow = true;
      }
      if (this.acc < this.max_acc){
        this.acc -= 0.0002;
      }
    }
    
    // grow vel if needed
    if (this.vel < this.max_vel){
      this.vel += this.acc;
    }
    
    // grow size from vel
    this.r += this.vel;
  }
  
  update_index(index, size){
    // helper function to rotate through palette
    if (index == size-1){
      return 0;
    } else{
      return index + 1;
    }
  }
}
// alexthescott, 6/24/21
// a grid of triangles is draw, with a new the orientation upon activated by the mouse, or by a perlin nosie position
// if activated, the triangles are drawn with full bightness, and these triangles slowly fade away into the black background

let tile_size = 50;
let tiles = [];
let time = 0;
let time_vel = 0.02;
let noise_x;
let noise_y;
let m_x = 0;
let m_y = 0;
let mouse_still = 61;
let mouse_moved = false;

function setup() {
  createCanvas(400, 400);
  for (let x = 0; x < width / tile_size; x++) {
    let temp_tiles = [];
    for (let y = 1; y < width / tile_size + 1; y++) {
      temp_tiles.push(new tile(x, y));
    }
    tiles.push(temp_tiles);
  }
  noiseDetail(2);
  colorMode(HSB, 100);
  strokeJoin(ROUND);
}

function draw() {
  clear();
  background(0, 0, 0);
  noStroke();
  noFill();

  noise_x = Math.floor(map(noise(time), 0, 1, 0, 1 + width / tile_size));
  noise_y = Math.floor(map(noise(time + 1), 0, 1, 1, 1 + height / tile_size));

  old_m_x = m_x;
  old_m_y = m_y;
  
  m_x = Math.floor(mouseX / tile_size);
  m_y = Math.floor(mouseY / tile_size);

  if (m_x == old_m_x && m_y == old_m_y){
    mouse_still += 1;
  } else{
    mouse_still = 0;
  }

  translate(width / 10, height / 10);
  scale(0.8, 0.8);
  for (let x = 0; x < tiles.length; x++) {
    for (let y = 0; y < tiles[x].length; y++) {
      tiles[x][y].update(
        (x == noise_x && y == noise_y) ||
          (mouse_moved == true && x == m_x && y == m_y)
      );
      tiles[x][y].draw();
    }
  }
  
  mouse_moved = mouse_still <= 60;

  // draw border
  resetMatrix();
  noFill();
  strokeWeight(10);
  stroke(0, 0, map(noise(time / 2), -1, 1, 50, 100));
  strokeWeight(50);
  square(0, 0, width);

  time += time_vel;
}

class tile {
  constructor(x, y) {
    this.x = x * tile_size;
    this.y = y * tile_size;
    this.ori = randint(0, 3);
    this.new_pos = randint(0, 240);
    this.new_ori = false;
    this.glow = 0;
  }

  update(found) {
    // flip current tile, and ensure a new tile pattern with loop
    if (found) {
      if (this.new_ori == false) {
        this.ori = randint(0, 3);
        this.new_ori = true;
        this.glow = 100;
      }
    } else {
      this.new_ori = false;
      if (this.glow > 0) {
        this.glow -= this.glow / 100;
      }
    }
  }

  draw(){
    fill(this.glow)
    switch(this.ori){
      case 0: // top left
        triangle(this.x, this.y, this.x, this.y-tile_size, this.x+tile_size, this.y-tile_size);
        break;
      case 1: // top right 
        triangle(this.x+tile_size, this.y, this.x, this.y-tile_size, this.x+tile_size, this.y-tile_size);
        break;
      case 2: // bottom right
        triangle(this.x, this.y, this.x+tile_size, this.y-tile_size, this.x+tile_size, this.y);
        break;
      case 3: // bottom left
        triangle(this.x, this.y, this.x, this.y-tile_size, this.x+tile_size, this.y);
        break;
    }
  }
}

function randint(min, max) {
  // max and min are inclusive
  return min + Math.floor(Math.random() * Math.floor(1 + max - min));
}

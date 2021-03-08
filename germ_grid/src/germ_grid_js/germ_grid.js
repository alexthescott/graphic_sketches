// variation on https://www.openprocessing.org/sketch/780000

var colors = [["#F45D52", "#2E86AB"],
             ["#59344F", "#8BBF9F"],
             ["#E8E9F3", "#272635"],
             ["#2D0320", "#6C969D"],
             ["#C36F09", "#F4E409"],
             ["#F2F5DE", "#86E7B8"]];

// pick one of 6 colors
var palette_choice = Math.floor(Math.random() * colors.length);
var palette = colors[palette_choice];

// decide if ripple color and bg color should be flipped
var bg_flip = Math.floor(Math.random() * 2);
var bg;
var ball_color;
var shadow_color;

function setup() {
  createCanvas(400, 400);
  if(bg_flip == 0){;
    bg = color(palette[0]);
    ball_color = color(palette[1]);
    shadow_color = color(palette[1]);
    shadow_color.setAlpha(100)
  } else{
    bg = color(palette[1]);
    ball_color = color(palette[0]);
    shadow_color = color(palette[0]);
    shadow_color.setAlpha(100);
  }
  strokeWeight(25);
}

let gridHeight = 7;
let gridWidth = 7;
let cellSize = 50;
let a_off = 0;
let a_speed = 0.25;

function draw() {
  background(bg);
  noFill();
  stroke(ball_color);
  rect(0, 0, width, height);
  let xOffset = (width - gridWidth * (cellSize)) / 2 + cellSize/2;
  let yOffset = (height - gridHeight * (cellSize)) / 2 + cellSize/2;
  translate(xOffset, yOffset);
  for(let y = 0; y < gridHeight; y++){
    for(let x = 0; x < gridWidth; x++){
      let x_off = cos(a_off);
      let y_off = sin(a_off);
      let n = noise(x_off+x, y_off+y);
      let n_map = map(n, 0, 1, -2, 1.3);
      let shadow_pos = map(n, 0, 1, 2, 4);
      fill(shadow_color);
      noStroke();
      circle(x*cellSize+shadow_pos, y*cellSize+shadow_pos, n_map*cellSize);
      fill(ball_color);
      circle(x*cellSize, y*cellSize, n_map*cellSize);
    }
  }
  a_off += radians(a_speed);
}
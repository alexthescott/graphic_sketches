// tiny noise
// Alex Scott, 2020
// -> ... cell_size / (width || height) must be an int

let palettes = [['#273043', '#F02D3A', '#EFF6EE'],
  ['#1E2019', '#E2C044', '#587B7F'],
  ['#15A0A2', '#4A8FE7', '#44E5E7'],
  ['#5C95FF', '#B9E6FF', '#F87575'],
  ['#2C302E', '#474A48', '#909590'],
  ['#243010', '#829E2E', '#AFCC66']];

// pick one of 6 palettes
var palette_choice = Math.floor(Math.random() * palettes.length);
var palette = palettes[palette_choice];

var cell_size = 8;
var noise_const = 0.05;
var time = 0;
var time_vel = 1;
var time_frailty = 3; // how much should time move noise?
var slant;

function setup() {
  createCanvas(400, 400);
  noiseDetail(3);
  noStroke();
  slant = map(random(0, 1), 0, 1, -2, 2);
  slant == 0 ? slant = 1 : slant = slant;
}

function draw() {
  background(palette[0]);
  let x_grid = width / cell_size;
  let y_grid = height / cell_size;

  for (let x = 0; x < x_grid; x++) {
    for (let y = 0; y < y_grid; y++) {
      x_off = x * noise_const / slant;
      y_off = y * noise_const * slant;

      x_cir = cos(time);
      y_cir = sin(time);
      c = noise(x_off, y_off, x_cir + y_cir);

      if (c >= 0.55) {
        fill(palette[1]);
        square(x * cell_size, y * cell_size, cell_size);
      } else if (c > 0.455) {
        fill(palette[2]);
        square(x * cell_size, y * cell_size, cell_size);
      }
    }
  }
  time += radians(time_vel);
}
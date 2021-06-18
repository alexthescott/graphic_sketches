// carpet noise -> alexthescott 6/18/21
// three palettes, layered 2D perlin nosie, perfect loop

let inc = 1;
let scl = 32;
let start = 0;
let n_scale = 0.1;
let cols = NaN;
let rows = NaN;

let palettes = [[[7, 59, 76], [255, 209, 102], [236, 136, 5], [6, 214, 160], [17, 229, 236]],
               [[205, 214, 208], [214, 203, 193], [214, 169, 154], [225, 96, 54], [227, 23, 10]],
               [[135, 130, 130], [132, 220, 207], [166, 217, 247], [188, 204, 224], [191, 152, 160]]];

let palette = [];

function setup() {
  // pick one of 3 colors
  palette_choice = randint(0, palettes.length - 1);
  palette = palettes[palette_choice];

  createCanvas(512, 512);
  cols = width / scl;
  rows = height / scl;
  noStroke();
  noiseDetail(2);
  blendMode(DIFFERENCE);
}

function draw() {
  clear();
  background(palette[0]);
  let yoff_0 = cos(start);
  let xoff_0 = sin(start);

  let yoff_1 = cos(start);
  let xoff_1 = sin(start);

  for (let x = 0; x < rows; x++) {
    for (let y = 0; y < cols; y++) {
      let n1 = noise(xoff_0 / 5, yoff_0) * 255;
      let n2 = noise(xoff_1 / 10, yoff_1) * 255;

      // 'stuttered' blocks
      if (n1 <= 96) {
        c1 = palette[1];
        c2 = palette[2];
        r = map(x, 0, rows, c1[0], c2[0]);
        g = map(x, 0, rows, c1[1], c2[1]);
        b = map(x, 0, rows, c1[2], c2[2]);
        fill(r, g, b);
        rect(x * scl, y * scl, scl, scl / 2);
      }

      // full blocks
      if (n2 <= 96) {
        c1 = palette[3];
        c2 = palette[4];
        r = map(x, 0, rows, c1[0], c2[0]);
        g = map(x, 0, rows, c1[1], c2[1]);
        b = map(x, 0, rows, c1[2], c2[2]);
        fill(r, g, b);
        rect(y * scl, x * scl, scl, scl);
      }

      xoff_0 += inc;
      xoff_1 -= inc;
    }
    yoff_0 += inc;
    yoff_1 -= inc;
  }
  start += radians(inc);
}

function mouseClicked() {
  noiseSeed(frameCount);
  var temp_choice = palette_choice;
  palette_choice = Math.floor(Math.random() * palettes.length);
  while (palette_choice == temp_choice) {
    palette_choice = Math.floor(Math.random() * palettes.length);
  }
  palette = palettes[palette_choice];
}

function randint(min, max) {
  // min and max should are inclusive
  return Math.floor(Math.random() * Math.floor(1 + max - min)) + min;
}

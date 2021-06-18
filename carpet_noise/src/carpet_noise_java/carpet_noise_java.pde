// carpet noise -> alexthescott 6/18/21
// three palettes, layered 2D perlin noise, perfect loop


int inc = 1;
int scl = 32;
float start = 0.0;
int cols;
int rows;
int palette_choice;

int[][][] palettes = {{{7, 59, 76}, {255, 209, 102}, {236, 136, 5}, {6, 214, 160}, {17, 229, 236}},
                {{205, 214, 208}, {214, 203, 193}, {214, 169, 154}, {225, 96, 54}, {227, 23, 10}},
                {{135, 130, 130}, {132, 220, 207}, {166, 217, 247}, {188, 204, 224}, {191, 152, 160}}};
int[][] palette;

void setup(){
   palette_choice = randint(0, palettes.length - 1);
   palette = palettes[palette_choice];
   size(512, 512);
   cols = width / scl;
   rows = height / scl;
   noStroke();
   noiseDetail(2);
   blendMode(DIFFERENCE);
}

void draw(){
    clear();
    background(palette[0][0], palette[0][1], palette[0][2]);
    
    float yoff_0 = cos(start);
    float xoff_0 = sin(start);
    
    float yoff_1 = cos(start);
    float xoff_1 = sin(start);

    for(int x = 0; x < rows; x++){
      for(int y = 0; y < cols; y++){
        float n1 = noise(xoff_0 / 5.0, yoff_0) * 255;
        float n2 = noise(xoff_1 / 10.0, yoff_1) * 255;
        
        if(n1 <= 96){
          int[] c1 = palette[1];
          int[] c2 = palette[2];
          
          float r = map(x, 0, rows, c1[0], c2[0]);
          float g = map(x, 0, rows, c1[1], c2[1]);
          float b = map(x, 0, rows, c1[2], c2[2]);
          fill(r, g, b);
          rect(x * scl, y * scl, scl, scl / 2);
        }
        
        if(n2 <= 96){
          int[] c1 = palette[3];
          int[] c2 = palette[4];
          
          float r = map(x, 0, rows, c1[0], c2[0]);
          float g = map(x, 0, rows, c1[1], c2[1]);
          float b = map(x, 0, rows, c1[2], c2[2]);
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

void mouseClicked(){
  noiseSeed(frameCount);
  int temp_choice = palette_choice;
  palette_choice = randint(0, palettes.length - 1);
  while (palette_choice == temp_choice){
    palette_choice = randint(0, palettes.length - 1);
  }
  palette = palettes[palette_choice];
}

int randint(int min, int max) {
  // max and min are inclusive
  return (int) (min + (Math.random() * (1 + max - min)));
}

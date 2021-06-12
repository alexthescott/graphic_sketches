// alexthescott 6/11/21
// Attempt at a faithful recreation of the sketch linked below! 
// https://twitter.com/beesandbombs/status/1385611174704713728

float time = 0;
float vel;
int hori_count = 14;
int vert_count = 7;
int[] colors = {#F94144, #F65A38, #F3722C, #F68425, #F8961E, #F9AF37,
              #F9C74F, #C5C35E, #90BE6D, #6AB47C, #43AA8B, #4D908E,
              #52838F, #577590};
              
void setup(){
  size(400, 400);
  noFill();
  strokeWeight(3);
  blendMode(SCREEN);
  vel = TWO_PI / 300;
}

void draw(){
  clear();
  background(0, 0, 32);
  for(int y = 0; y < vert_count; y++){
    for(int t = 0; t < hori_count; t++){
      float x_pos = map(y, 0, vert_count - 1, 50, height - 50);
      float y_pos = map(sin(time + (float) t / 6 + (float) y / 2), -1, 1, 75, width - 75);
      stroke(colors[t]);
      circle(x_pos, y_pos, 35);
    }
  }
  time += vel;
}

// Alex Scott - 6/11/21 recreating, and remixing @mattdesl's boxes -- front  
//  -> https://twitter.com/mattdesl/status/1396876632594554887
//    
//  threw my occasional twist on things
//    - 50% chance for an alternate palette
//    - 25% chance for a squircle shape, instead of a sharp line
//    - 20% chance for a alternate blending mode (10% for multiply, 10% for hard_light)

import java.lang.Math;

int[] og_palette = {#000000, #FFFFFF, #9A9899, #3C5DE7, #B0587C, 
  #F6521C, #FF9204, #FCC400, #4C9A1B, #B68817};
int[] alt_palette = {#000000, #FFFFFF, #F94144, #F3722C, #F8961E, 
  #F9844A, #F9C74F, #90BE6D, #43AA8B, #4D908E, 
  #577590, #277DA1};
int[] palette;

boolean squircle;
int blend_chance;
int border = 72;
int obj_count = 16;
int obj_size = 16;
int obj_limit = 32;
int[][][] objs = new int[obj_limit][3][2];

void setup() {
  size(400, 400);
  int palette_choice = randint(0, 1);
  squircle = randint(0, 3) == 0;
  palette = (palette_choice == 0) ? og_palette : alt_palette;
  
  blend_chance = randint(0, 100);
  if(blend_chance <= 10){
    blendMode(MULTIPLY);
  } else if (blend_chance <= 20){
    blendMode(HARD_LIGHT);
  }
  
  for (int i = 0; i < obj_limit; i++) {
    int new_size[] = get_size();
    int new_pos[] = get_pos(new_size);
    int new_color[] = get_color_index(palette.length);
    objs[i][0] = new_pos;
    objs[i][1] = new_size;
    objs[i][2] = new_color;
  }
  noStroke();
}

void draw() {
  background(#EAE2D4);
  if (frameCount % 4 == 0) {
    for (int i = 0; i < obj_limit - 1; i++) {
      objs[i][0] = objs[i+1][0];
      objs[i][1] = objs[i+1][1];
      objs[i][2] = objs[i+1][2];
    }
    int new_size[] = get_size();
    int new_pos[] = get_pos(new_size);
    int new_color[] = get_color_index(palette.length);
    objs[obj_limit-1][0] = new_pos;
    objs[obj_limit-1][1] = new_size;
    objs[obj_limit-1][2] = new_color;
  }

  for (int i = 0; i < obj_limit; i++) {
    int[] pos = objs[i][0];
    int[] size = objs[i][1]; 
    int[] obj_color = objs[i][2]; 
    fill(palette[obj_color[0]]);
    if (squircle){
      rect(border + pos[0] * obj_size, border + pos[1] * obj_size, size[0] * obj_size, size[1] * obj_size, 5);
    }
    else{
      rect(border + pos[0] * obj_size, border + pos[1] * obj_size, size[0] * obj_size, size[1] * obj_size);
    }  
  }
}

int randint(int min, int max) {
  // max and min are inclusive
  return (int) (min + (Math.random() * (1 + max - min)));
}

int[] get_size() {
  int[] size = {randint(1, 4), randint(1, 4)};
  return size;
}

int[] get_pos(int[] size) {
  int[] pos = {randint(0, 16 - size[0]), randint(0, 16 - size[1])};
  return pos;
}

int[] get_color_index(int palette_len) {
  int[] color_index = {randint(0, palette_len - 1)};
  return color_index;
}

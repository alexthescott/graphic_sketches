int[][] colors = {
        {#E63946, #4CC9F0},
        {#023047, #FFB703},
        {#081C15, #52B788},
        {#DEAAFF, #C0FDFF},
        {#FB5607, #FF006E},
        {#355070, #B56576}};
        
int palette_choice = round(random(0, colors.length-1));
int[] palette = colors[palette_choice];
color bg;
color ripple_color;

Ripple ripples[] = new Ripple[3];
int avoid_pos = round(random(0, 3));

void setup(){
  size(400, 400);
  int index = 0;
  for(int i = 0; i < 4; i++){
    if (i != avoid_pos){
      ripples[index] = new Ripple(i);
      index++;
    }
  }
  noFill();
  
  // decide if ripple color and bg color should be flipped
  int bg_flip = round(random(0, 1));
  if (bg_flip == 0){
    bg = color(palette[0]);
    ripple_color = color(palette[1]);
  } else{
    bg = color(palette[1]);
    ripple_color = color(palette[0]);
  }
  
  background(bg);
  stroke(ripple_color);
  strokeWeight(12);
  rect(0, 0, width, height);
  strokeWeight(5);
  for(int i = 0; i < 3; i++){
    ripples[i].draw();
  }
}

void draw(){
  background(bg);
  stroke(ripple_color);
  strokeWeight(12);
  rect(0, 0, width, height);
  strokeWeight(5);
  for(int i = 0; i < 3; i++){
    ripples[i].draw();
  }
}

class Ripple{
  int max_size = floor(2.5 * sqrt(sq(width) + sq(height)));
  int spawn_rate = 5;
  float speed = 0.4;
  float ripple_gap = speed * spawn_rate * 60;
  int num_of_ripples = round(max_size / ripple_gap);
  float ripple_r[] = new float[num_of_ripples];
  int x;
  int y;
  int del_index = num_of_ripples-1;
  
  Ripple(int pos){
    switch(pos){
      case 0: // top left 
        x = -width/10;
        y = -height/10;
        break;
      case 1: // top right
        x = width + width/10;
        y = -height/10;
        break;
      case 2: // bottom left
        x = -width/10;
        y = height + height/10;
        break;
      case 3: // bottom right
        x = width + width/10;
        y = height + height/10;
        break;
    }
    
    for(int i = 0; i < num_of_ripples; i++){
      ripple_r[i] = ripple_gap * i;
    }
    
  }
  
  void draw(){
    if (frameCount % (spawn_rate * 60) == 0){
      ripple_r[del_index] = 0;
      if (del_index == 0){
        del_index = num_of_ripples - 1;
      } else{
        del_index = del_index - 1;
      }
    }
    
    for(int i = 0; i < num_of_ripples; i++){
      circle(x, y, ripple_r[i]);
      ripple_r[i] = ripple_r[i] + speed;
    }
  }
}

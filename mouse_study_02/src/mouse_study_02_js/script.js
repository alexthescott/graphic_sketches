// alexthescott
// mouse study 02
// 23/10/24

let t=0
let at=0
let x=0

function draw_mouse(x, y, size=1, angle=0, og_color=True){
  if (og_color){ 
    fill(255)
    stroke(0)
  } else{
    fill(0)
    stroke(255)
  }
  push()
  beginShape();
  translate(x,y)
  rotate(angle)
  vertex(0,0)
  vertex(0,0+17*size)
  vertex(0+4*size,0+13*size)
  vertex(0+7*size,0+20*size)
  vertex(0+10*size,0+19*size)
  vertex(0+7*size,0+12*size)
  vertex(0+12*size,0+12*size)
  endShape(CLOSE)
  pop()
}

function setup() {
  createCanvas(400, 400);
  strokeWeight(1.2)
  noiseDetail(4,0.2)
  angleMode(RADIANS)
}

function draw() {
  background(0);
  for (let i=0; i<=32; i++){
    draw_mouse(noise(100+at+i/16)*width*1.5,noise(at+i/16)*height*1.5,1,0,i==32)
  }
  t+=0.006
  at=t+sin(t)/3
}
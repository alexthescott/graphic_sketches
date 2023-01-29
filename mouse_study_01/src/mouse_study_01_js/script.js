// alexthescott
// mouse study 01
// 23/01/29

let t=0
let x=0

function draw_mouse(x,y,size=2,angle=0){
  push()
  beginShape();
  strokeWeight(2)
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

function draw_mouse_circle(radius, count){
  x=noise(radius/100+t)
  for(let i=x; i<TWO_PI+x; i+=PI/count){
    let x=cos(i)*radius
    let y=sin(i)*radius
    draw_mouse(width/2+x,height/2+y,2,3.25*PI/2+i)
  }
}


function setup() {
  createCanvas(800, 800);
  fill(0)
  stroke(255)
  strokeWeight(1.2)
  noiseDetail(2,0.2)
  angleMode(RADIANS)
}

function draw() {
  background(0);
  draw_mouse(width/2-10,height/2-20)
  draw_mouse_circle(width/12, 4)
  draw_mouse_circle(width/6, 6)
  draw_mouse_circle(width/4, 8)
  draw_mouse_circle(width/3, 10)
  draw_mouse_circle(width/2.38, 14)
  draw_mouse_circle(width/1.97, 16)
  draw_mouse_circle(width/1.7, 20)
  t+=0.01
}
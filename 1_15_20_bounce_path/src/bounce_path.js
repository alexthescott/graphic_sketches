var colors = [["#586F6B", "#7F9183", "#B8B8AA", "#CFC0BD", "#DDD5D0"],
              ["#53599A", "#068D9D", "#6D9DC5", "#80DED9", "#AEECEF"],
              ["#F4AFAB", "#F4CBC6", "#F7EDF0", "#F4F482", "#F4EEA9"],
              ["#401712", "#3B52A5", "#D95D39", "#F18805", "#F0A202"],
              ["#191716", "#D83137", "#804D54", "#B592A0", "#C6B8CC"]];

var choice = Math.floor(Math.random() * (5));
var pallet = colors[choice];

function setup() {
  var p5Canvas = createCanvas(400, 400);
  background(pallet[0]);
  b1 = new ball(8, pallet[1]);
  b2 = new ball(12, pallet[2]);
  b3 = new ball(16, pallet[3]);
  b4 = new ball(20, pallet[4]);
  // all trailing lines will be
}

function draw() {
  background(pallet[0]);
  b1.draw();
  b2.draw();
  b3.draw();
  b4.draw(); 
}

class ball {
  // Ball moves linearly in a random direction drawing a trail
  constructor(r, color) {
    this.color = color
    this.x = random(r * 2, width - r * 2);
    this.y = random(r * 2, height - r * 2);
    this.dir = random(10, 350);
    this.x_vel = cos(this.dir) * 3;
    this.y_vel = sin(this.dir) * 3;
    this.r = r / 2;
    this.line_p = [[this.x, this.y]];
    this.line_vel = [[this.x_vel, this.y_vel]];
    this.line_delay = 3; // seconds will be converted into ms
  }

  draw() {
    fill(this.color);
    noStroke();
    strokeWeight(4);
    circle(this.x, this.y, this.r * 2);
    stroke(this.color);

    // before the first bounce, attach line to pos
    if (this.line_p.length == 0) {
      var first_point = this.line_p[0];
      line(first_point[0], first_point[1], this.x, this.y);
    }

    // there are bounces to be drawn
    else {
      // draw all prior bounces off walls 
      for (var i = 0; i < this.line_p.length - 1; i++) {
        var past_point = this.line_p[i];
        var new_point = this.line_p[i + 1];
        line(past_point[0], past_point[1], new_point[0], new_point[1]);
      }
      // draw current position to last wall bounce
      var last_point = this.line_p[this.line_p.length - 1];
      line(last_point[0], last_point[1], this.x, this.y);
    }
    // update pos of ball and trailing line
    this.update();
  }

  update() {
    // check if the ball bounces off the wall
    if (this.x <= this.r || this.x >= width - this.r) {
      this.x_vel *= -1;
      this.line_p.push([this.x, this.y]);
      this.line_vel.push([this.x_vel, this.y_vel]);
    }

    if (this.y <= this.r || this.y >= height - this.r) {
      this.y_vel *= -1
      this.line_p.push([this.x, this.y])
      this.line_vel.push([this.x_vel, this.y_vel])
    }

    // update the position of the old trail after this.line_delay seconds of drawing line
    if (millis() >= this.line_delay * 1000) {
      // remove from list if trail 'bounces' off the wall
      if (this.line_p[0][0] <= this.r || this.line_p[0][0] >= width - this.r) {
        this.line_vel.shift();
        this.line_p.shift();
      }

      if (this.line_p[0][1] <= this.r || this.line_p[0][1] >= height - this.r) {
        this.line_vel.shift();
        this.line_p.shift();
      }

      // update position of trailing line
      this.line_p[0][0] += this.line_vel[0][0];
      this.line_p[0][1] += this.line_vel[0][1];
    }

    // update the new position of the ball
    this.x += this.x_vel;
    this.y += this.y_vel;
  }

}
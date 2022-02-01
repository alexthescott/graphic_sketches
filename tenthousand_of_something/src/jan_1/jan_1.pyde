# alexthescott
from random import random, randint

pos = []
count=10000.0
var1=3*randint(2,8)
var2=2**randint(7,9)
var3=2**randint(5,7)

def setup():
    global pos
    size(512,512)
    background('#9042E0')
    noFill()
    stroke(255,255,255,10)
    strokeWeight(0)
    blendMode(SUBTRACT)
    for i in range(int(count)):
        a=(i/count)*TWO_PI
        x=width/2+cos(a)*(width/2)
        y=height/2+sin(a)*(height/2)
        pos.append([x,y])
    
def draw():
    background('#9042E0')
    global pos
    for i,p in enumerate(pos):
        n=512
        m=1.07
        circle(p[0],p[1],n*sin(i/(count/TWO_PI/m)))
        
def keyReleased():
    if key == 'c':
        print("frame captured")
        saveFrame()

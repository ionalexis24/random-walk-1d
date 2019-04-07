a=1000
x=0
y=0
off=a/30.0
def setup():
    size(a,a/2)
    background(0)
    stroke(255)
    strokeWeight(2)
    line(0,(a+0.0)/4,width,(a+0.0)/4)
    translate(width/2,height/2)
    stroke(0,0,255)
    strokeWeight(10)
    point(0,0)
    
def X(x):
    a=random(1.0)
    if a<=0.5:
        print -1
        return x-off
    else:
        print +1
        return x+off
    
def draw():
    background(0)
    stroke(255)
    strokeWeight(2)
    line(0,(a+0.0)/4,width,(a+0.0)/4)
    global x
    translate(width/2,height/2)
    stroke(0,0,255)
    strokeWeight(10)
    point(0,0)
    
    stroke(255,0,0)
    point(x,y)
    x=X(x)
    if x>a/2 or x<-a/2:
        x=0
    delay(350)
    
    

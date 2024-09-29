import turtule
color=['pink','yellow','blue']
sketch=turtle.Pen()
turtle.bgcolor(black)
for i in range(30):
    sketch.pencolor(colors[i%6])
    sketch.width(i/100+1)
    sketch.forward(i)
    sketch.left(59)
    

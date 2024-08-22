import turtle
import colorsys
turtle.speed(0)
turtle.pensize(2)
turtle.bgcolor("white")
h=0.5

    
for i in range(70):
    c=colorsys.hsv_to_rgb(h,1,1)
    turtle.pencolor(c)
    h+=0.005
    turtle.circle(5-i,100)
    turtle.lt(80)
    turtle.circle(5-i,100)
    turtle.rt(100)
turtle.done()

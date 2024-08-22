import turtle

turtle.bgcolor('white')
turtle.pencolor('red')
turtle.title('HAMED')
turtle.speed(0)
turtle.width(2)

def form(x):
    turtle.circle(100,x)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.circle(-100,x)

def leaf():
    for i in range(0,100,10):
        form(i)

leaf()
turtle.setheading(90)
leaf()
turtle.setheading(180)
leaf()
turtle.setheading(270)
leaf()
turtle.setheading(360)
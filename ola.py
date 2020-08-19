import turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.color("white")
t.up()
t.goto(-80,100)
t.down()
t.fillcolor("white")
t.begin_fill()
t.forward(230)
t.setheading(270)
s = 360
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)

    
t.forward(180)
s = 270
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)

t.forward(230)
s = 180
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)

t.forward(180)
s = 90
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)
    
t.end_fill()
t.up()
t.forward(110)
t.setheading(270)
#t.color("red")
t.forward(140)
t.forward(100)
t.setheading(0)
t.down
t.fillcolor("black")
t.begin_fill()
t.circle(100)
t.end_fill()
t.setheading(90)
t.up()
t.forward(100)
t.forward(-50)
t.setheading(0)
t.down()
t.fillcolor("#9ACD32")
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.setheading(270)
t.forward(45)
t.setheading(0)
t.down()
t.pensize(3)
t.color("white")
c = 100
for i in range(2):
    t.circle(c)
    t.penup()
    t.forward(5)
    t.pendown()


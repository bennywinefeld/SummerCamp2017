from turtle import Turtle
amy = Turtle()
amy.speed(0)
amy.goto(0,0)
amy.color("coral")
amy.begin_fill()

count = 0
while count < 4:
    amy.forward(100)
    amy.right(90)
    count += 1
amy.end_fill()

amy.color("black")
amy.forward(100)
amy.left(90)
amy.forward(150)
amy.left(90)
amy.forward(100)
amy.left(90)
amy.forward(150)
amy.left(180)

amy.forward(120)
amy.right(60)
amy.color("white")
amy.begin_fill()
amy.circle(30)
amy.end_fill()
amy.color("black")
amy.circle(30)

amy.right(60)
amy.penup()
amy.forward(30)
amy.pendown()
amy.color("white")
amy.begin_fill()
amy.circle(40)
amy.end_fill()
amy.color("black")
amy.circle(40)

amy.left(30)
amy.penup()
amy.forward(70)
amy.pendown()
amy.color("white")
amy.begin_fill()
amy.circle(30)
amy.end_fill()
amy.color("black")
amy.circle(30)

amy.penup()
amy.goto(30,-30)
amy.pendown()
amy.dot(5)
amy.penup()
amy.goto(60,-30)
amy.pendown()
amy.dot(5)
amy.penup()
amy.goto(-30,-70)
amy.pendown()
amy.left(20)

amy.width(3)
amy.forward(80)
amy.right(40)
amy.forward(80)

amy.penup()
amy.goto(30, -70)
amy.width(2)
amy.pendown()
amy.circle(40, 70)

#amy.hideturtle()
#amy.done()
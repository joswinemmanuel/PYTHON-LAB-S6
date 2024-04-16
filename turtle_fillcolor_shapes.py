from turtle import Turtle

t = Turtle()
t.screen.title("Star")
t.width(4)
t.color('red')
t.fillcolor('yellow')
t.hideturtle()

t.begin_fill()
for i in range(5):
    t.forward(200)
    t.left(144)
t.end_fill()

t.penup() 
t.goto(-300, 0)
t.pendown()

t.color('blue')
t.fillcolor('orange')

t.begin_fill()
for i in range(5):
    t.forward(200)
    t.right(144)
t.end_fill()

t.screen.exitonclick()

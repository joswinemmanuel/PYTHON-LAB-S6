from turtle import Turtle

t = Turtle()
t.screen.title("Star")
t.width(4)
t.color("red")
t.hideturtle()

for i in range(5):
    t.forward(200)
    t.left(144)

t.penup() 
t.goto(-300, 0)
t.pendown()

for i in range(5):
    t.forward(200)
    t.right(144)

t.screen.exitonclick()

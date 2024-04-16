from turtle import Turtle

t = Turtle()
t.screen.title("Hexagon")
t.width(5)
t.color("blue")
t.hideturtle()

for i in range(6):
    t.forward(200)
    t.left(60)

t.screen.exitonclick()

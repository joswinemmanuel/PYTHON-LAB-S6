from turtle import *

t = Turtle()
t.hideturtle()
speed(0)

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break

t.screen.exitonclick()

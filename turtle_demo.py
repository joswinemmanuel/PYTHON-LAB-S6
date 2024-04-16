from turtle import Turtle

t = Turtle()
t.screen.title("First Demo")
t.screen.bgcolor("Red")
t.speed(0)
t.color("yellow")
for i in  range(10**3):
    t.forward(2+i*2)
    t.right(90)
t.screen.exitonclick()

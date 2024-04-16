from turtle import Turtle

t = Turtle()
t.screen.title("Square")
t.width(3)
t.color("blue")
t.hideturtle()
print(dir(t))
for i in range(4):
    t.forward(100)
    t.left(90)
t.screen.exitonclick()

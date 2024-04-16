from turtle import Turtle

t = Turtle()
t.speed(0)

for i in range(25):
    t.circle(2*i)
    t.circle(-2*i)
    t.left(i)
    
t.screen.exitonclick()

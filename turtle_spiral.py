from turtle import Turtle

t = Turtle()
t.speed(0)

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        t.color(c)
        t.forward(steps)
        t.right(30)
        
t.screen.exitonclick()

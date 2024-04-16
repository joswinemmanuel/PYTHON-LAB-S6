from turtle import Turtle
import random

def audi(t, l):
    for i in range(4):
        t.circle(l)
        t.penup()
        t.fd(l*1.25)
        t.pendown()

t = Turtle()
t.hideturtle()
t.speed(0)
t.width(5)

audi(t, 50)
    

t.screen.mainloop()

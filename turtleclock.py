import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
clock = turtle.Turtle()
clock.speed(100)
clock.shape("turtle")
clock.color("blue")
x=90
for i in range(12):
    clock.pu()
    clock.lt(x)
    clock.fd(100)
    clock.pd()
    clock.fd(30)
    clock.pu()
    clock.fd(25)
    clock.stamp()
    clock.rt(180)
    clock.fd(155)
    clock.lt(90)
    x+=30
    if (x>=150):
        x-=30
clock.lt(25)

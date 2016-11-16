#Hanzala Siddiqui
#Computer Programming
#9/15/16
import turtle
wn=turtle.Screen()
hanz=turtle.Turtle()
hanz.speed(.5)
wn.bgcolor("black")
hanz.pensize(10)
hanz.shape("triangle")

bob=turtle.Turtle()
bob.shape("square")
bob.color("silver")
bob.pensize(10)
bob.pu()
bob.goto(-250,-250)
bob.pd()
bob.begin_fill()
for i in range(4):
    bob.fd(500)
    bob.lt(90)
bob.color("white")
bob.end_fill()
bob.hideturtle()

x=0
hanz.begin_fill()
while x<=180:
    hanz.left(x)
    hanz.color("blue")
    hanz.forward(150)
    hanz.left(90)
    hanz.stamp()
    hanz.color("red")
    hanz.forward(150)
    hanz.left(90)
    hanz.stamp()
    hanz.color("orange")
    hanz.forward(150)
    hanz.left(90)
    hanz.stamp()
    hanz.color("grey")
    hanz.forward(150)
    hanz.left(90)
    hanz.stamp()
    x+=.5
    hanz.color("firebrick")
hanz.end_fill()



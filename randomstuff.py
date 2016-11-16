#Hanzala Siddiqui
#Computer Programming
#10/6/16
import turtle
wn=turtle.Screen()
poly=turtle.Turtle()
sides=int(input("How many sides does the polygon have? "))
angle=360/sides
for i in range(sides):
    poly.fd(75)
    poly.lt(angle)
    poly.fd(50)
    poly.lt(angle)
    poly.fd(75)
    poly.bk(75)
    poly.rt(angle)

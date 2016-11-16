#Hanzala Siddiqui
#Computer Programming
#9/20/16
import turtle

while True:
    try:
        numside = int(input("What is the number of sides? "))
        break
    except ValueError:
        print("Oops!  That was not a number.  Try again...")
while True:
    try:
        sidelength = int(input("What is the length of the sides? "))
        break
    except ValueError:
        print("Oops!  That was not a number.  Try again...")
while True:
    scolor = input("What is the color of the sides? ")
    if(scolor=="red" or scolor=="blue" or scolor=="black"or scolor=="white"or scolor=="orange"or scolor=="green"):
        break
    else:
        print("Oops!  That was not a valid option.  Try again...")
while True:
    fcolor = input("What is the color of the sides? ")
    if(fcolor=="red" or fcolor=="blue" or fcolor=="black"or fcolor=="white"or fcolor=="orange"or fcolor=="green"):
        break
    else:
        print("Oops!  That was not a valid option.  Try again...")
wn=turtle.Screen()
bob=turtle.Turtle()
bob.color(scolor, fcolor)
bob.pensize(3)
bob.begin_fill()
angle=360/numside
for i in range(numside):  
    bob.fd(sidelength)
    bob.lt(angle)
bob.end_fill()

#Hanzala Siddiqui
#Computer Programming
#10/6/16
import turtle
import time
wn=turtle.Screen()
poly=turtle.Turtle()
flower=turtle.Turtle()

def drawpoly():
    for i in range(6):
        poly.fd(75)
        poly.lt(120)
        poly.fd(75)
        poly.lt(120)
        poly.fd(75)
        poly.lt(180)
    time.sleep(3)
def drawflower():
    flower.lt(90)
    flower.speed(.5)
    for i in range(4):
        for i in range(180):
            flower.fd(1)
            flower.rt(.6)
        flower.rt(70)#
        for i in range(180):
            flower.fd(1)
            flower.rt(.6)
        flower.lt(15)
        flower.up
        flower.setx(0.0)
        flower.sety(0.0)
        flower.down
    time.sleep(3)
def menu():
    while True:
        try:
            choice=int(input("""What would you like to do:
1-Draw Flower
2-Draw Polygon
3-Quit
"""))
            if(choice==1):
                poly.reset()
                drawflower()
            elif(choice==2):
                flower.reset()
                drawpoly()
            elif(choice==3):
                quit()
            else:
                print("That's not an option! ")
        except ValueError:
            print("Oops!  That was not a number.  Try again...")
        
    
menu()

#Hanzala Siddiqui
#Computer Programming
#10/13/16
import math
def  is_rightangle(a, b, c):
    sa=a**2
    sb=b**2
    sc=c**2
    if(sa+sb==sc):
        return True
    else:
        return False



while True:
    try:
        a=float(input("What is the first base: "))
        break
    except ValueError:
        print("Oops!  That was not a number.  Try again...")
while True:
    try:
        b=float(input("What is the second base: "))
        break
    except ValueError:
        print("Oops!  That was not a number.  Try again...")          
while True:
    try:
        c=float(input("What is the hypotenuse: "))
        break
    except ValueError:
        print("Oops!  That was not a number.  Try again...")  

if(abs(a-b)<=.001):
    a=b
rtriangle=is_rightangle(a, b, c)

if(rtriangle==True):
    print("Those three sides belong to a right triangle.")
else:
    print("Those three sides do not belong to a right triangle.")

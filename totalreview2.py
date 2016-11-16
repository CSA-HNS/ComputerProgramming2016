#Hanzala Siddiqui
#Computer Programming 1
#11/15/16
import random
def rangeprinter():
    while True:
        try:
            s=int(input("Minimum number: "))
            break
        except ValueError:
            print("Oops!  That was not a number.  Try again...")
    while True:
        try:
            m=int(input("Maximum number: "))
            if(m>s):
                break
            else:
                print("The maximum number has to be bigger than the minimum number!")
        except ValueError:
            print("Oops!  That was not a number.  Try again...")
    while True:
        try:
            n=int(input("How many random numbers: "))
            break
        except ValueError:
            print("Oops!  That was not a number.  Try again...")
    
    for i in range(n):
        x=random.randrange(s, m+1)
        print(x)
rangeprinter()

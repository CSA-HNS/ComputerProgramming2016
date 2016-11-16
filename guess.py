#Hanzala Siddiqui
#Computer Programming
#9/28/2016
import random
x=random.randrange(1,11)
while True:
    try:
        guess=int(input("Guess a number from 1 to 10: "))
        if(guess>=1 and guess<=10):
            break
        else:
            print("Oops!  That was not a number between 1 and 10.  Try again...")
    except ValueError:
        print("Oops!  That was not a number.  Try again...")
    
if(guess==x):
    print("Correct!")
else:
    print("Incorrect!")

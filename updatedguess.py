#Hanzala Siddiqui
#Computer Programming
#9/28/2016
import random
x=random.randrange(1,11)
print(x)
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
elif(guess>=x):
    print("Incorrect, you guessed too high!")
elif(guess<=x):
    print("Incorrect, you guessed too low!")
while True:
    try:
        guess2=int(input("Try again and guess a number from 1 to 10: "))
        if(guess2>=1 and guess2<=10):
            break
        else:
            print("Oops!  That was not a number between 1 and 10.  Try again...")
    except ValueError:
        print("Oops!  That was not a number.  Try again...")
if(guess2==x):
    print("Correct!")
else:
    print("Incorrect!")

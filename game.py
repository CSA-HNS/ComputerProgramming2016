#Hanzala Siddiqui
#Computer Programming
#9/28/2016
import random

ponenum=random.randrange(1, 101)
ptwonum=random.randrange(1, 101)
while True:
    try:
        pone=int(input("""You are Player One.
Do you want to roll? 1-Yes , 2-No """))
        if(pone==1):
            break
        elif(pone==2):
            quit()
        else:
            print("Oops!  That was not a valid option.  Try again...")
    except ValueError:
        print("Oops!  That was not a number.  Try again...")
while True:
    try:
        ptwo=int(input("""You are Player Two.
Do you want to roll? 1-Yes , 2-No """))
        if(ptwo==1):
            break
        elif(ptwo==2):
            quit()
        else:
            print("Oops!  That was not a valid option.  Try again...")
    except ValueError:
        print("Oops!  That was not a number.  Try again...")
print("Player 1 got a ", ponenum)
print("Player 2 got a ", ptwonum)
if(ponenum>ptwonum):
    print("Player 1 won the game!")
elif(ponenum<ptwonum):
    print("Player 2 won the game!")

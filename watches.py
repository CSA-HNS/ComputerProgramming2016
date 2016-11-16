#Hanzala Siddiqui
#Computer Programming
#9/28/2016
import random
watches = ["Hublot", "Rolex", "Bvlgari"]
cost=random.randrange(1,11)
print(cost)
name=input("Username: ")
print("Hello, "+name)
while True:
    try:
        watch = input("""Which watch would you like to buy?
Your options are: Hublot, Rolex, Bvlgari""")
        if(watch in watches):
            print("Success")
            break
    except ValueError:
        print("Oops!  That was not a number.  Try again...")


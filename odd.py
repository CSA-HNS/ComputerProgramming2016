#Hanzala Siddiqui
#Computer Programming
#10/12/16
def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False
while True:
    try:
        n=int(input("What is the number: "))
        break
    except ValueError:
        print("Oops!  That was not a number.  Try again...")
iodd=is_odd(n)
if(iodd==True):
    print("That number is an odd number.")
else:
    print("That number is not an odd number.")

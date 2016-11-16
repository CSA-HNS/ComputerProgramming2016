#Hanzala Siddiqui
#Computer Programming
#10/5/16
def total(x, y, z):
    return x+y+z
while True:
    try:
        num=int(input("How Many Runners? "))
        if(num>=1):
            break
        else:
            print("Oops!  That was not a valid option.  Try again...")
    except ValueError:
        print("Oops!  That was not a number.  Try again...")

totaltime=0
run=1
for i in range(num):
    print("Runner ", run)
    while True:
        try:
            x=int(input("How long did it take to run lap 1: "))
            if(num>=1):
                break
            else:
                print("Oops!  That was not a valid option.  Try again...")
        except ValueError:
            print("Oops!  That was not a number.  Try again...")
    while True:
        try:
            y=int(input("How long did it take to run lap 2: "))
            if(num>=1):
                break
            else:
                print("Oops!  That was not a valid option.  Try again...")
        except ValueError:
            print("Oops!  That was not a number.  Try again...")
    while True:
        try:
            z=int(input("How long did it take to run lap 3: "))
            if(num>=1):
                break
            else:
                print("Oops!  That was not a valid option.  Try again...")
        except ValueError:
            print("Oops!  That was not a number.  Try again...")

    time=total(x, y, z)
    totaltime+=time
    run+=1
print("Total time: ",totaltime, " minutes")

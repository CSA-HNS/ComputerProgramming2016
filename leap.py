#Hanzala Siddiqui
#Computer Programming
#10/12/16
def leapyear(year):
    if(year%400==0):
        return False
    elif(year%4==0):
        return True
    else:
        return False
while True:
    try:
        year=int(input("What year is it: "))
        break
    except ValueError:
        print("Oops!  That was not a number.  Try again...")
lyear=leapyear(year)
if(lyear==True):
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")


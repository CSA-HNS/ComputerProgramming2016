#Hanzala Siddiqui
#Computer Programming 1
#11/15/16
def divisible():
    while True:
        try:
            num=int(input("What is the number? "))
            break
        except ValueError:
            print("Oops!  That was not a number.  Try again...")
    if(num%2==0):
        print(num/2)
    else:
        print("Not divisible by 2! ")
    if(num%5==0):
        print(num/5)
    else:
        print("Not divisible by 5! ")
    if(num%6==0):
        print(num/6)
    else:
        print("Not divisible by 6! ")
divisible()

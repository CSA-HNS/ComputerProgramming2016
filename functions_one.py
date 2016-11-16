#Hanzala Siddiqui
#Computer Programming
#10/6/16
def pname(name):
    print("Hi, "+name)
    menu()
    
def name():
    name=input("What is your  name? ")
    pname(name)
def addmath():
    while True:
        try:
            x=int(input("What is the first number: "))
            break
        except ValueError:
            print("Oops!  That was not a number.  Try again...")
    while True:
        try:
            y=int(input("What is the second number: "))
            break
        except ValueError:
            print("Oops!  That was not a number.  Try again...")
    print("The answer is "+str(x+y)".")
    menu()
def menu():
    while True:
        try:
            choice=int(input("""What would you like to do:
1-Print Hello Message
2-Add two numbers
3-Quit
"""))
            if(choice==1):
                name()
            elif(choice==2):
               addmath()
            elif(choice==3):
                quit()
            else:
                print("That's not an option! ")
        except ValueError:
            print("Oops!  That was not a number.  Try again...")
        
    
menu()

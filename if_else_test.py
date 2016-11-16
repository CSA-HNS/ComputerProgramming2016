#Hanzala Siddiqui
#Computer Programming
#9/9/16
def numbersix():
    while True:
        try:
            num1 = int(input("What is the first number: "))
            break
        except ValueError:
            print("Oops!  That was not a number.  Try again...")
    while True:
            try:
                num2 = int(input("What is the second number: "))
                break
            except ValueError:
                print("Oops!  That was not a number.  Try again...")
    if(abs(num1)==6 or abs(num2)==6):
        resultsix=True
    elif(abs(num1-num2)==6 or abs(num1+num2)==6):
        resultsix=True
    else:
        resultsix=False
    return (resultsix)
    
def alarmtime():
    while True:
        try:
            wday = int(input("What day is it? 0=Sun, 1=Mon, 2=Tue, 3=Wed, 4= Thurs, 5=Fri 6=Sat: "))
            if(0<=wday<=6):
                break    
            else:
                print("Oops!  Day must be between 0 and 6.  Try again...")
        except ValueError:
            print("Oops!  That was not a number.  Try again...")
    while True:
        try:
            vday = int(input("Is it a vacation day? 1=Yes, 2=No: "))
            if(vday==1):
                bday=True
                break
            elif(vday==2):
                bday=False
                break
            else:
                    print("Oops!  Must enter 1 for Yes or 2 for No.  Try again...")
           
        except ValueError:
            print("Oops!  That was not a number.  Try again...")
    if(vday==True):
        alarm=("10:00")
    elif(vday==False and wday==0 or wday==6):
        alarm=("10:00")
    else:
        alarm=("7:00")
    return(alarm)
def speedingticket():
    while True:
        try:
            speed = int(input("What speed were you driving at? "))
            if(speed>=0):
                break    
            else:
                print("Oops!  Speed must be above 0.  Try again...")
        except ValueError:
            print("Oops!  That was not a number.  Try again...")
    while True:
        try:
            bday = int(input("Is it your birthday? 1=Yes, 2=No: "))
            if(bday==1):
                bday=True
                break
            elif(bday==2):
                bday=False
                break
            else:
                    print("Oops!  Must enter 1 for Yes or 2 for No.  Try again...")
           
        except ValueError:
            print("Oops!  That was not a number.  Try again...")
    if(bday==True):
        if(speed<=65):
            ticket=0
        elif(65<speed<=85):
            ticket=1
        else:
            ticket=2
    elif(bday==False):
        if(speed<=60):
            ticket=0
        elif(60<speed<=80):
            ticket=1
        else:
            ticket=2
    if(ticket==0):
        print("You were driving within the speed limit.")
    elif(ticket==1):
        print("You were let off with a warning!")
    else:
        print("You got a huge ticket which comes with a huge fine!")
        print(" ")
    menu()
def datenight():
    while True:
        try:
            you = int(input("What would you rank your clothes? "))
            if(you<=10 and you>=0):
                date = int(input("What would you rank your date's clothes? "))
                if(date<=10 and date>=0):
                    break
                else:
                    print("Oops!  Rating must be between 0 and a 10.  Try again...")
            else:
                    print("Oops!  Rating must be between 0 and a 10.  Try again...")
           
        except ValueError:
            print("Oops!  That was not a number.  Try again...")

    if(date<=2 or you<=2):
        entry=0
    elif(date>=8 or you>=8):
        entry=2
    else:
        entry=1
    if(entry==0):
        print("Sorry Sir, but we CAN NOT book you a table!")
    elif(entry==2):
        print("Welcome Sir, we have a VIP table just for you!")
    else:
        print("Hello Sir, I'll see if I can get you a table.")
    print(" ")

    menu()
def menu():
    while True:
        try:
            choice=int(input("""Welcome
Please select an option from the menu provided below.
1-Date Night
2-Speeding Ticket
3-Alarm
4-Number 6
5-Quit
"""))
            if(1<=choice<=5):
                break
            else:
                print("Oops!  Choice must be between 1 and a 5.  Try again...")
        except ValueError:
            print("Oops!  That was not a number.  Try again...")
    if(choice==1):
        datenight()
    elif(choice==2):
        speedingticket()
    elif(choice==3):
        print(alarmtime())
        print(" ")
        menu()
    elif(choice==4):
        print(numbersix())
        print(" ")
        menu()
    elif(choice==5):
        quit
    
menu()

#Hanzala Siddiqui
#Computer Programming 1
#10/07/2016
incorrect=0
def login_correct(name):
    print("Welcome to the Secret Service, "+ name)
def login_incorrect(incorrect):
    incorrect+=1
    if(incorrect>=3):
        print("The police has been alerted. Time for you to run. You have 5 seconds")
        quit(1)
    return incorrect
def login(incorrect):
    
    name=input("Name? ")
    pw="bob"
    entry=input("Password: ")
    if(pw==entry):
        login_correct(name)
    else:
        incorrect=login_incorrect(incorrect)
        print(incorrect)
        login(incorrect)
        
login(incorrect)

#Hanzala Siddiqui
#Computer Programming
#9/8/16
name=input("Name? ")
while True:
    try:
        grade = int(input("What is the grade? "))
        if(grade<=100 and grade>=0):
            break
        else:
            print("Oops!  Grade must be between 0 and a 100.  Try again...")
           
    except ValueError:
        print("Oops!  That was not a number.  Try again...")
        
if(grade>=90):
    print(name+" got an A")
elif(grade>=80):
    print(name+" got a B")
elif(grade>=70):
    print(name+" got a C")
elif(grade>=60):
    print(name+" got a D")
else:
    print(name+" got an F")

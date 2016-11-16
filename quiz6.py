cs=int(input("What is your current score? "))
pm=int(input("How many points did you make? "))
def addpoints(cs, pm):
    tp=cs+pm
    return tp
print("You have "+str(addpoints(cs, pm))+" points!")

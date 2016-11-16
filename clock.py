#Hanzala Siddiqui
#Computer Programming
#9/2/16
name=(input("Name? "))
ctime=(input("Current time? "))
ctime=(int(ctime))
wtime=(input("How many hours until alarm? "))
wtime=(int(wtime))
atime=(wtime%24)
atime=(atime+ctime)
atime=(str(atime))
print("The time will be "+atime+" when the alarm rings.")

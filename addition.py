#Hanzala Siddiqui
#Computer Programming(NOT COMPUTER SCIENCE 1)
#9/1/16
x = input("First Number: ")
try:
   num1 = int(x)
except ValueError:
   print("That's not an int!")
   exit()
   
y = input("Second Number: ")
try:
   num2 = int(y)
except ValueError:
   print("That's not an int!")
   exit()
print(num1+num2)


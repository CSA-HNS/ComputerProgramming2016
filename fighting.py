#Hanzala Siddiqui
#Computer Programming
#9/28/2016
import random
weapons = ["Sniper", "Shotgun", "Pistol"]
defense=random.randrange(1,11)
print(defense)
name=input("Username: ")
print("Hello, "+name)
while True:
  
    weapon = input("""Which weapon would you like to hoose?
Your options are: Sniper, Shotgun, Pistol: """)
    weapon=weapon.lower()
    weapon=weapon.title()
    if(weapon in weapons):
        break
    else:
        print("That is not an option!")
if(weapon=="Sniper"):
    attack=random.randrange(6,10)
elif(weapon=="Shotgun"):
    attack=random.randrange(1,11)
elif(weapon=="Pistol"):
    attack=random.randrange(2,7)
print (attack)
if(attack>=defense):
    print("You Win!")
else:
    print("You Lose!")

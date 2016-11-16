#Hanzala Siddiqui
#Computer Programming
#10/14/2016
import os
def escape_planet(planet, ev, speed, ep, points):
    nev=ev*.1
    
    if(speed>=ev-nev and speed<=ev+nev):
        print("Success!")
        print("The planet code is "+planet.upper())
        points+=ep
        print ("You have "+str(points)+" points.")
        game(planet, points)
        os.system("cls")
    else:
        if(speed>ev):
            print("The velocity was to high!")
            print("You had "+str(points)+" points when you died!")
        elif(speed<ev):
            print("The velocity was to low!")
            print("You had "+str(points)+" points when you died!")
        start()
            
    
def game(planet, points):
    planets=["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Sun"]
    escapevelocities=[4.3, 10.3, 11.2, 5.0, 59.6, 35.6, 21.3, 23.8, 1.2, 617.5]
    escapepoints=[2, 4, 5, 3, 9, 8, 6, 7, 1, 10]
    print("You are on planet", planet)
    while True:
        p=input("""What planet do you want to go to?
Options:
Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto
""")
        p=p.lower()
        p=p.title()
        if(p in planets):
            pn=planets.index(planet)
            ev=escapevelocities[pn]
            ep=escapepoints[pn]
            break
        else:
            print("That is not an option. Please try again! ")
    while True:
        try:
            s=float(input("How many km/s do you want to go to escape planet "+planet+"?"))
            break
        except ValueError:
            print("Oops!  That was not a number.  Try again...")
    escape_planet(p, ev, s, ep, points)
def start():
    print("""Welcome!
This is a spaceship simulator.
The objective is to make it from one planet to the next.
""")
    global name
    name=input("What is your name? ")
    global points
    points=0
    
def menu():
    start="Earth"
    while True:
        try:
            c=int(input("""Options:
    1-Start Game
    2-Enter Planet Code
    3-Quit
    Enter the number corresponding to your choice.
    """))
            if(c==1 or c==2 or c==3):
                os.system("cls")
                if(c==1):
                    while True:
                        try:
                            w=int(input("What is the ship weight?"))
                            break
                        except ValueError:
                            print("Oops!  That was not a number.  Try again...")
                    game(start, points)
                elif(c==2):
                    planetcodes=["MERCURY", "VENUS", "EARTH", "MARS", "JUPITER", "SATURN", "URANUS", "NEPTUNE", "PLUTO", "SUN"]
                    code=input("Please enter Planet Code: ")
                    if(code in planetcodes):
                        print("Success")
                        code=code.lower()
                        code=code.title()
                        game(code, points)
                    else:
                        print("Invalid Code!")
                        menu()
                elif(c==3):
                    quit()
            else:
                print("Oops!  That was not an option.  Try again...")
        except ValueError:
            print("Oops!  That was not a number.  Try again...")
            

start()
menu()
    
    

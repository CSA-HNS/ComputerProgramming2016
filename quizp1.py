x=input("What is your name? ")
x=x.lower()
x=x.title()
def know(x):
   names=["Jenny","Bob","Fran","Billy"]
   if(x in names):
      print("Hello, "+x)
   else:
      print("I don’t know you, "+x)

    
know(x)

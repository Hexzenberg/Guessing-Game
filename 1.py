print("Welcome to my computer quiz!")
playing=input("Do you want to play? Yes or No\n")
if playing.lower()!="yes":
    quit()
s=0
print("Let's begin the game!")
a=input("What does CPU stand for?\n")
if a.lower()=="central processing unit":
    print("Correct!")
    s+=1
else:
    print("Wrong Answer!")
    s-=1
a=input("What does RAM stand for?\n")
if a.lower()=="random access memory":
    print("Correct!")
    s+=1
else:
    print("Wrong Answer!")
    s-=1
a=input("What does GPU stand for?\n")
if a.lower()=="graphics processing unit":
    print("Correct!")
    s+=1
else:
    print("Wrong Answer!")
    s-=1
a=input("What does PSU stand for?\n")
if a.lower()=="power supply unit":
    print("Correct!")
    s+=1
else:
    print("Wrong Answer!")
    s-=1
print("You scored "+str(s)+" out of 4!\n"+"Which is "+str(s*100/4)+"% of the total")


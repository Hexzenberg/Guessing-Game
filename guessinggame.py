w="Python"
g=""
c=0
l=3
o=False
print("You have three chances to win\n"+"Hint for the word "+w[0]+" and "+w[5])
while g!=w and not(o):
    if c<l:
        g=input("Enter your guess:\n")
        c+=1
    else:
        o=True
if o:
    print("Out of chances!\nYou Lose!")
else:
    print("You Win!")

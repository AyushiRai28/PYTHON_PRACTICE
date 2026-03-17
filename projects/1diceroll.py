from random import randint 

def diceroll(m):
    a=1
    while(a<=m):
        i = input("roll the dice(y/n) : ")
        if i.lower() == "y":
            x = randint(0,6)
            print(f"your number is {x}") 

        elif i.lower() == "n":
            print("sorry for the uncovenience!")
            print("thank you")
            continue
        else:
            print("invalid input")
            continue
        a += 1

        


diceroll(2)       
          

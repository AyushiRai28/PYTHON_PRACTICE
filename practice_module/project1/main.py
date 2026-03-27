import random

'''
let 1 for snake 
-1 for water 
0 for gun'''

# write a program for the snake water gun program.

computer = random.choice([1,0,-1])
youstr =  input("enter your choice :")
youdict = { "s": 1, "w" : -1, "g":0}
reverse = { 1:"snake" , -1: "water" , 0:"gun"}
you= youdict[youstr]
print("you chose ", reverse[you])
print("computer chose",reverse[computer])

if(computer ==-1 and you==1):
    print("You won!!")

elif(computer==-1 and you==0):
    print("You lost!!")

elif(computer==1 and you==0):  
    print("you won!!")    

elif(computer==1 and you==-1):  
    print("you lose!!")    

elif(computer==0 and you==1):  
    print("you lost!!")    

elif(computer==0 and you==-1):  
    print("you won!!")    

else:
    print("It's a tie!!")      
    print("Try again")      
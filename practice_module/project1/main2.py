# another way for same question

# if(computer ==-1 and you==1):
#     print("You won!!")

# elif(computer==-1 and you==0):
#     print("You lost!!")

# elif(computer==1 and you==0):  
#     print("you won!!")    

# elif(computer==1 and you==-1):  
#     print("you lose!!")    

# elif(computer==0 and you==1):  
#     print("you lost!!")    

# elif(computer==0 and you==-1):  
#     print("you won!!")    

# else:
#     print("It's a tie!!")      
#     print("Try again")   
import random   
computer = random.choice([1,0,-1])
youstr =  input("enter your choice :")
youdict = { "s": 1, "w" : -1, "g":0}
you= youdict[youstr]

if(computer-you==-1 or computer-you==2):
    print("you lose")

else:
    print("you win")    

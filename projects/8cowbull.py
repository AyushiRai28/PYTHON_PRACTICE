import random


digit = random.randint(1000,9999)


def game():

    while True :

        guess = int(input("Guess the 4 digit number : "))


       

        for i in range (0,4) :
            bull = 0
            cow = 0



            if digit[i] == guess[i]:
                bull += 1

        for digit in guess:
            if digit in guess:
               cow += 1

        cow -= bull  # remove bulls from cows count    

        print(f" {cow} Cows , {bull} Bulls ") 
        
        if guess == digit :
            print("Yayyy ! you won ")
            return 
        
game()        
        



    

    
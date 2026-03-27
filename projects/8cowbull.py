import random

def game():
    secret = str(random.randint(1000,9999))
    attempt = 0
    while True :
        bull = 0
        cow = 0

        user = int(input("Guess the 4 digit number : "))
        guess = str(user)

        for i in range (4) :
           
            if secret[i] == guess[i]:
                bull += 1

        for g in guess:
            if g in secret:
               cow += 1

        cow -= bull  # remove bulls from cows count   
        attempt += 1 

        print(f" {cow} Cows , {bull} Bulls ") 
        
        if guess == secret :
            print(f"Yayyy ! you won in {attempt} attempts ")
            return 
        
game()        

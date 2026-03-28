import random

def spin_wheel():
    symbols = ["🍒", "🍋", "🔔", "⭐", "7️⃣"]

    return[random.choice(symbols) for _ in range(3)]
 
def cashback(reels , bet):
    # All three match
    if reels[0] == reels[1] == reels[2]:
        return bet * 10
    
    # Two match
    elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
        return bet * 2
    
    # No match
    else:
        return 0
    
def game():

    print("===-- WELCOME TO THE GAME --===")
    balance = int(input("Enter your starting balance : $"))

    while True: 
        choice= input("You wanna play again? (y/n)  ")

        if choice != 'y':
            print(f"Your balance current blance is {balance}")
            break
        

        bet = int(input("Enter amount to bet: $"))
        reels = spin_wheel()
        print("|".join(reels))
        award = cashback(reels , bet)
        if award == 0:
            print("you lost !")
            balance = balance - bet
            continue

        else :
            print(f"You won an amount of {award}")   
            balance = balance - bet + award 
            continue

game()
  

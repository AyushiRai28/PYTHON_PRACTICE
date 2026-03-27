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
    while True: 
        balance = int(input("Enter your starting balance: $"))
        bet = int(input("Enter amount to bet: $"))
        reels = spin_wheel()
        cashback(reels , bet)
        balance = balance - bet
        print(f"You won : ${cashback}")

        choice= input("You wanna play again? (y/n)  ")

        if choice != 'y':
            break

game()


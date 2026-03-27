import random

def spin_reels():
    symbols = ["🍒", "🍋", "🔔", "⭐", "7️⃣"]
    return [random.choice(symbols) for _ in range(3)]

def check_payout(reels, bet):
    # All three match
    if reels[0] == reels[1] == reels[2]:
        return bet * 10
    
    # Two match
    elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
        return bet * 2
    
    # No match
    else:
        return 0

def slot_machine():
    print("🎰 Welcome to the Slot Machine Game!")
    
    balance = 100  # Starting balance
    
    while balance > 0:
        print(f"\n💰 Current Balance: {balance}")
        
        choice = input("Do you want to play? (yes/no): ").lower()
        if choice != "yes":
            print(f"🏆 You walk away with {balance} coins!")
            break
        
        try:
            bet = int(input("Enter your bet: "))
            
            if bet > balance or bet <= 0:
                print("❌ Invalid bet amount.")
                continue
        
        except ValueError:
            print("❌ Please enter a valid number.")
            continue
        
        # Spin
        reels = spin_reels()
        print("\n🎲 Spinning...")
        print(" | ".join(reels))
        
        # Check result
        winnings = check_payout(reels, bet)
        
        if winnings > 0:
            print(f"🎉 You won {winnings} coins!")
            balance += winnings - bet
        else:
            print("😢 You lost your bet.")
            balance -= bet
    
    if balance == 0:
        print("💀 You're out of money! Game Over.")

# Run the game
slot_machine()


import random

def roll_dice():
    return random.randint(1, 6)

def player_turn(player_name):
    turn_score = 0
    
    while True:
        roll = roll_dice()
        print(f"{player_name} rolled a {roll}")
        
        if roll == 1:
            print("Oops! You rolled a 1. No points this turn.\n")
            return 0
        
        turn_score += roll
        choice = input("Roll again? (y/n): ").lower()
        
        if choice != 'y':
            print(f"{player_name} scored {turn_score} points this turn.\n")
            return turn_score

def pig_dice_game():
    scores = [0, 0]
    current_player = 0
    
    while scores[0] < 100 and scores[1] < 100:
        print(f"Player {current_player + 1}'s turn")
        
        turn_points = player_turn(f"Player {current_player + 1}")
        scores[current_player] += turn_points
        
        print(f"Current scores: Player 1: {scores[0]}, Player 2: {scores[1]}\n")
        
        # Switch player
        current_player = 1 - current_player
    
    # Winner
    if scores[0] >= 100:
        print("🎉 Player 1 wins!")
    else:
        print("🎉 Player 2 wins!")

# Run the game
pig_dice_game()

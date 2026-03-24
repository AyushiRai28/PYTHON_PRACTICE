import random 


def roll():
    return random.randint(1,6)

def player_turn(player) :

    while True :
        print(f" {player} rolled {roll}")
        turn_points += roll

        if roll==1 :
            print("Oopss! You got a 1 and lost all your point")
            return 0
        
    
        turn_points = 0

        choice = input("Do you wanna roll again (y/n)?? ").lower()

        if choice!= "y" :
            print(f"{player} scored {turn_points } in this turn")
            return turn_points


def game():
    scores = [0,0]
    current_player = 0

    while scores[0]<100 and scores[1]<100 :
        print(f"Player {current_player + 1}'s turn")   
        turn_score = player_turn(f"Player {current_player + 1}")
        scores[current_player] += turn_score

        print(f"Current score Player 1 : {scores[0]} ,  Player 2 : {scores[1]}")

        current_player = 1 - current_player


    if scores[0] >= 100:
        print("🎉 Player 1 wins!")
    else:
        print("🎉 Player 2 wins!")

# Run the game
game()   







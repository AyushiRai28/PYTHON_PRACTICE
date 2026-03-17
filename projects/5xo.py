#tic tac toe game

# Tic Tac Toe Game

board = [[" " for i in range(3)] for j in range(3)]

def print_board():
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

player = "X"

for turn in range(9):
    print_board()
    print(f"Player {player}'s turn")
    
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    
    if board[row][col] == " ":
        board[row][col] = player
    else:
        print("Cell already taken. Try again.")
        continue
    
    if check_winner(player):
        print_board()
        print(f"Player {player} wins!")
        break
    
    player = "O" if player == "X" else "X"
else:
    print_board()
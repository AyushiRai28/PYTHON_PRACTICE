import random

def generate_number():
    # Generate a 4-digit number (digits can repeat)
    return str(random.randint(1000, 9999))

def calculate_cows_bulls(secret, guess):
    bulls = 0
    cows = 0

    # Count bulls (correct digit & position)
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1

    # Count cows (correct digit, wrong position)
    for digit in guess:
        if digit in secret:
            cows += 1

    cows -= bulls  # remove bulls from cows count

    return cows, bulls

def play_game():
    secret = generate_number()
    attempts = 0

    print("Welcome to Cows and Bulls Game!")
    print("Guess the 4-digit number.\n")

    while True:
        guess = input("Enter your guess: ")

        # Validation
        if len(guess) != 4 or not guess.isdigit():
            print("❌ Enter a valid 4-digit number.\n")
            continue

        attempts += 1
        cows, bulls = calculate_cows_bulls(secret, guess)

        print(f"Cows: {cows}, Bulls: {bulls}\n")

        if bulls == 4:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break

# Run the game
play_game()

import random

def game():
    list1 = ('rat', 'cat', 'dog', 'mat', 'hat', 'sat', 'mad', 'how', 'cow', 'wow', 'who', 'log')

    word = random.choice(list1)
    final = ["_"] * len(word)   # use list instead of string
    n = 0

    while True:
        print(" ".join(final))
        guess = input("Guess a letter: ").lower()

        if guess in word:
            for i in range(len(word)):   # FIXED
                if guess == word[i]:
                    final[i] = guess     # FIXED

        n += 1

        if "".join(final) == word:  # convert list to string
            break

    print(f"🎉 Yayy!! The word was {word}")
    print(f"You got the word in {n} attempts")

game()

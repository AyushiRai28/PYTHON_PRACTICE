'''The Word Guessing Game is a fun and interactive project where players try to
guess a secret word, one letter at a time. The word is selected randomly from a list
of words stored in a text file. The player has six attempts to guess the word, with
each incorrect guess reducing the remaining attempts. Correctly guessed letters
are revealed in their respective positions, while incorrect guesses prompt the
player to try again.'''

import random


def game():
    list1 = ('rat' , 'cat' , 'dog' , 'mat'  , 'hat' , 'sat' , 'mad' , 'how' , 'cow' , 'wow' , 'who' , 'log')

    word = random.choice(list1)
    final = ["_"] * len(word)
    n = 0
    while True:
        
        print(" ".join(final))
        guess = input("Guess a letter : ").lower()

        if guess in word:
            for i in range(len(word)):
                if guess == word[i]:
                    final[i] = guess

        
        n += 1
        
        if "".join(final) == word:
            break


    print(f" YAyyy!! The word was {word}")
    print(f"you got the word in {n} attempts")  

game()    





  



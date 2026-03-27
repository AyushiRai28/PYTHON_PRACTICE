#  to make a game that reads your score and storres your high score and changes the high score when you beat it.

import random
def game():
    print("you are playing the game")
    score = random.randint(1,62)
    #fetch hiscore
    with open("hiscore.txt") as f :
        hiscore = f.read()
        if hiscore != "" :
            hiscore = int(hiscore)
        else :
            hiscore =  0

    print(f"Your score: {score}")
    if(score>hiscore ):
        #writw this high score to the file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

        return score
game()
       
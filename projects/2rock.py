import  random

a  = random.randint(-1,1)
print("welcomr to the game ")
print(''' enter
      r for rock
      p for paper
      s for scissor
      ''')
g = input(" enter your choice : ")

d1 = { "r": 1, "p" : 0, "s":-1}
d2 = { 1:"rock" , 0:"paper" , -1:"scissor"}

b=d1[g]
n = d2[b]
c=d2[a]
print(f"you chose {n}")

print(f"the computer chose {c}")

if a== 1 and b == 0 :
    print("You win")

elif a==1 and b==-1:
    print("You loose")
elif a==0 and b==-1:
    print("You win")
elif a==0 and b==1:
    print("You loose")
elif a==-1 and b==1:
    print("You win")
elif a==-1 and b==0:
    print("You loose")
else:
    print("Its a tie")



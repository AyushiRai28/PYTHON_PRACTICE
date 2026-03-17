print('''WELCOME TO KNOW THE WORLDS CUTTEST FREIND QUIZ GAME ''')
score = []
while True:
    

    type = int(input('''ENTER THE TYPE OF QUIZ  
                1. HER FAVORITES
                2. HER BEHAVIOUR
                ANSWER IN 1 OR 2 : '''))
    

    if type==1:
        point1 = 0
        
        
        a = input('''a. Her favrorite color
                a. purple
                b. blue
                c. black
                d. all of the above
                your answer= ''')
        b = input('''b. Her favrorite actor
                a. akshay kumar
                b. kartik aryan
                c. srk
                d. all of the above
                your answer= ''')
        c = input('''c. Her favrorite desert
                a. ice cream
                b. choolate
                c. cake
                d. both a and b
                your answer= ''')
        d = input('''d. Her favrorite hoobie
                a. singing
                b. movies
                c. sleeping
                d. all of the above
                your answer= ''')
        e = input('''e. Her favrorite moviee 
                a. yeh jawani hai deewani
                b. jab we met
                c. kal ho na ho
                d. all of the above
                your answer= ''')
        if  a == 'd':
            point1 += 1
            print("correct")
        else:
            print("incorrect")    
        if  b == 'd':
            point1 += 1
            print("correct")
        else:
            print("incorrect")
        if  c == 'd':
            point1 += 1
            print("correct")
        else:
            print("incorrect")
        if  d == 'd':
            point1 += 1
            print("correct")
        else:
            print("incorrect")
        if  e == 'd':
            point1 += 1
            print("correct")
        else:
            print("incorrect")
        score.append(point1)     
        print("your score is : ", point1) 

    elif type==2:
        
        point = 0
        a = input('''a. Biggesst fear
                a. disappointments
                b. expectations
                c. dependency
                d. all of the above
                your answer= ''')
        b = input('''b. What annoys her the most
                a. imperfection
                b. repeatation of mistake
                c. ignorance
                d. all of the above
                your answer= ''')
        c = input('''c. What lifts her mood up when alone
                a. food
                b. music
                c. movie
                d. all of the above
                your answer= ''')
        d = input('''d.What lifts her mood up when with you
                a. food
                b. hug
                c. deep talks
                d. all of the above
                your answer= ''')
        e = input('''e. Her favrorite move with you 
                a. hug
                b. kiss
                c. holding hands
                d. all of the above
                your answer= ''')
        if  a == 'd':
            point += 1
            print("correct")
        else:
            print("incorrect")    
        if  b == 'd':
            point += 1
            print("correct")
        else:
            print("incorrect")
        if  c == 'd':
            point += 1
            print("correct")
        else:
            print("incorrect")
        if  d == 'd':
            point += 1
            print("correct")
        else:
            print("incorrect")
        if  e == 'a':
            point += 1
            print("correct")
        else:
            print("incorrect")
        score.append(point)        
        print("your score is : ", point) 
    else:
        print("invalid input")
        print("try again")        
        continue
    
    choice = input("Do you want to convert again? (yes/no): ").lower()
    if choice != "yes":

        break

print("your score is : ", score)    








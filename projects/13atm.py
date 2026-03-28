def atm():

    balance = 1000

    while True :
        print("WELCOME TO THE ATM ")
        print('''
        1. Check Balance
        2. Deposit 
        3. Withdraw
        4. Exit      

        ''')

        try:
            choice = int(input("Enter your option (index no. ) : "))

        except ValueError:
            print("please enter valid option ")
            continue

        if choice == 1 :
            print(f"Your current balance is {balance}")
        elif choice == 2 :

            try:
                dep = int(input("Enter amount to deposit: "))    

            except ValueError:
                print("please enter valid amount .")    
            print("Deposit successful ")
            balance += dep
        elif choice == 3 :

            try: 
                withdraw = int(input("Enter the amount you wanna withdraw : "))   
            except ValueError:
                print("Enter valid amount! ")

            if balance<withdraw :
                print("Balance unsufficient . Try again")
                continue

            print("Withdrawl successful")
            balance -= withdraw 

        elif choice ==4:
            print("thank you")
            break

        else :
            print("Invalid input")
            continue        


atm()        

            






    
        
        

    
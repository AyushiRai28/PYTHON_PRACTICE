print('''"Your to do list:" 
"1.view tasks" 
"2.add task" 
"3.remove task" 
"4.exit "
"5. mark complete''' )
task = []
completed = []
while True:
    choice = int(input("enter your choice: "))
    if choice == 2:
        inp = input("enter the task: ")
        task.append(inp)
        print("task added")

    elif choice == 1:
        if task:
            for i, t in enumerate(task):
                print(f"{i}. {t}")
        else:
            print("No tasks yet.")

    elif choice== 3:
        print(task)
        rem = int(input("enter index of the task to be removed: ") )
        if 0 <= rem < len(task):
            task.pop(rem)
            print(f"Removed task: {rem}")
    
        else:
            print("task not found")
            print ("try again!!") 
            continue

    elif choice == 4:
        break    

    elif choice == 5:
        complete = int(input("Enter index for the task completed"))
        if 0<= complete < len(task) :
            task.pop(complete)
            completed.append(complete)

            print("task left: " , task)
            print("completed task: ", complete)
        else:
            print("task not found")
            print ("try again!!") 
            continue

    else :
        print("invalid input!!")
        continue
        

    option = input("do you want further changes ?(y/n): ").lower()
    if option != "y" :
        break

print("THANK YOU !!")    


        





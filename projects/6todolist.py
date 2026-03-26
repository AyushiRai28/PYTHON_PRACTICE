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
                print(f"{i+1}. {t}")
        else:
            print("No tasks yet.")

    elif choice== 3:
        if task:
            for i,t in enumerate(task):
                print(f"{i+1}. {t}")
        rem1 = int(input("enter index of the task to be removed: ") )
        rem = rem1 - 1
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
            completed.append(task[complete])
            task.pop(complete)

            print("task left: " , task)
            print("completed task: ", completed)
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


savefile = input("Do you want  to save your tasks (y/n)??  ")
if savefile == 'y':

    filename = input("Enter file name to open/create: ")
    
    try:
        with open(filename, 'r') as file:
            print("\n--- Existing Content ---")
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("\n A new file will be created.")
        
        with open(filename , 'w') as file:
            file.write(f"Tasks : {task}")
            file.write(f"Tasks completed ✅ : {completed}")

        print("File saved successfully")    

    

print("THANK YOU !!")    


        





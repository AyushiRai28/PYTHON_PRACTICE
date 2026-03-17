print("Your to do list:\n"
      "1. View tasks\n"
      "2. Add task\n"
      "3. Remove task\n"
      "4. Exit")

task = []

while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nTasks:")
        if task:
            for i, t in enumerate(task):
                print(f"{i}. {t}")
        else:
            print("No tasks yet.")

    elif choice == 2:
        new_task = input("Enter the task: ")
        task.append(new_task)
        print("Task added!")

    elif choice == 3:
        if not task:
            print("No tasks to remove.")
            continue
        print("\nTasks:")
        for i, t in enumerate(task):
            print(f"{i}. {t}")
        rem = int(input("Enter index of the task to remove: "))
        if 0 <= rem < len(task):
            removed = task.pop(rem)
            print(f"Removed task: {removed}")
        else:
            print("Invalid index. Try again.")

    elif choice == 4:
        break

    else:
        print("Invalid input! Try again.")

    option = input("Do you want further changes? (y/n): ").lower()
    if option != "y":
        break

print("THANK YOU!!")
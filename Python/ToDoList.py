print("========= TO-DO-LIST MENU =========")


tasks = []
completed_tasks = set()

def Addlist():
    try:
        addtask = int(input("Enter the number of tasks to add: "))
        if addtask <= 0:
            print(" Please enter a number greater than 0.")
            return

        for i in range(addtask):
            while True:
                task = input(f"Enter task {i + 1}: ").strip()
                if task:
                    tasks.append(task)
                    break
                else:
                    print("Task cannot be empty. Please enter again.")
                    
        print("\n Tasks added successfully!")

    except ValueError:
        print(" Invalid input. Please enter a valid number.")
    except Exception as e:
        print(" Error:", e)
    finally:
        print(" Task Adding Completed\n")

def Showtask():
    try:
        if not tasks:
            print("No tasks found.")
        else:
            print(" List of Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "Done" if (i - 1) in completed_tasks else " Pending"
                print(f"{i}. {task} [{status}]")
    except Exception as e:
        print(" Error:", e)
    finally:
        print(" Show Task Completed\n")

def MarkedTask():
    try:
        if not tasks:
            print(" No tasks to mark as done.")
            return

        Showtask()
        value = int(input("Enter the Task Number to mark as done: "))

        if 1 <= value <= len(tasks):
            index = value - 1
            if index in completed_tasks:
                print(" Task already marked as done.")
            else:
                completed_tasks.add(index)
                print("Task marked as done.")
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")
    except Exception as e:
        print(" Error:", e)
    finally:
        print(" Mark Task Completed\n")

def Deletetask():
    try:
        if not tasks:
            print(" No tasks to delete.")
            return

        Showtask()
        delete = int(input("Enter the task number to delete: "))

        if 1 <= delete <= len(tasks):
            removed = tasks.pop(delete - 1)
            completed_tasks.discard(delete - 1)

            # Re-index completed_tasks
            new_completed = set()
            for idx in completed_tasks:
                if idx < delete - 1:
                    new_completed.add(idx)
                elif idx > delete - 1:
                    new_completed.add(idx - 1)
            completed_tasks.clear()
            completed_tasks.update(new_completed)

            print(f" Task '{removed}' deleted successfully.")
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")
    except Exception as e:
        print(" Error:", e)
    finally:
        print(" Delete Task Completed\n")

# Main menu loop
while True:
    print("========= TO-DO-LIST MENU =========")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1–5): ").strip()

    if choice == "1":
        Addlist()
    elif choice == "2":
        Showtask()
    elif choice == "3":
        MarkedTask()
    elif choice == "4":
        Deletetask()
    elif choice == "5":
        print(" Exiting the program. Goodbye!")
        break
    else:
        print(" Invalid choice. Please select a number between 1 and 5.\n")

# New project


def add_task(tasks):
    get_task = input("Enter the task you want to add: ")
    tasks.append({"task":get_task.upper(),
                  "completed":False})
    print(f"{get_task} added to list")
    print()

def check_task(tasks):
    if tasks == []:
        print("No task added")
        print()
    else:
        print("=" * 20)
        print("Available Tasks".upper())
        print("=" * 20)
        for task in tasks:
            print(task["task"])
        print("---------------------------")
        print()

def delete_task(tasks):
    if tasks == []:
        print("NO TASK TO BE DELETED")
        print()
    else:
        available = []
        for task in tasks:
            available.append(task["task"])
            print(task["task"])


        get_choice = input("Enter what you want to delete: ")
        if not get_choice.upper() in available:
            print("task not in record")
        else:
            many = len(tasks)
            for postion in range(many):
                if tasks[postion]["task"] == get_choice.upper():  #here i forgot .upper() and waste like 50mins debugging😭
                    tasks.pop(postion)
                    break
            print(f"{get_choice} has been removed")


def complete_task(tasks):
    if tasks == []:
        print("No Record task")
        print()
    else:
        get_choice = input("Enter task to be completed: ")

        for task in tasks:
            if task["task"] == get_choice.upper() and task["completed"] == False:
                print(f"{get_choice} completed")
                task["completed"] = True

            elif task["task"] == get_choice.upper() and task["completed"] == True:
                print("Task is already completed")

            else:
                print("No available task")

def completed_tasks(tasks):
    for task in tasks:
        if task["completed"] == True:
            print(f"{task["task"]} is completed")

        elif task["completed"] == False:
            pass# print(f"{task["task"]} not completed tasks")

        else:
            print("No task yet")
    
            

def main():
    print("== TO DO LIST APP ==".center(100))
    tasks = []
    while True:
        print("1. Add Task")
        print("2. Check Tasks")
        print("3. Delete Task")
        print("4. Complete Tasks")
        print("5. Check completed tasks")
        print("6. Exits")

        choice = input("Please enter option between 1-6: ")

        match choice:
            case "1":
                add_task(tasks)
            case "2":
                check_task(tasks)
            case "3":
                delete_task(tasks)
            case "4":
                complete_task(tasks)
            case "5":
                completed_tasks(tasks)
            case "6":
                print("Bye, Return back soon to complete your unfinished tasks!")
                quit()
            case _:
                print("Please choose between 1-6")

if __name__ == "__main__":
    main()



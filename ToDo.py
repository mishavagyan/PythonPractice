# To-Do List
to_do = []
def add_task():
    task = input("Add task: ")
    to_do.append(task)
def remove_task():
    task = input("Enter number of task you want to remove: ")
    try:
        i = int(task) - 1
        if 0 <= i < len(to_do):
            to_do.pop(i)
        else:
            print("Invalid input. Please enter a valid number.")
            remove_task()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        remove_task()
def view_task():
    print(f"\nYou have {len(to_do)} tasks")
    for i in range(len(to_do)):
        print((i + 1), ": ", to_do[i], sep="")
    print()

run = True

while run:
    print("Enter number to do.")
    print("1: To add new task")
    print("2: To remove task")
    print("3: View tasks")
    print("4: Close program")
    process = input("Enter number: ")
    if process == "1":
        add_task()
    elif process == "2":
        remove_task()
    elif process == "3":
        view_task()
    elif process == "4":
        run = False


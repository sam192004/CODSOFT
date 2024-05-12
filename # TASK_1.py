tasks = []
def add_task(task):
    tasks.append(task)

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
    else:
        print("Task not found!")
def show_tasks():
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks!")
while True:
    print("\nTo-Do List:")
    print("1. Enter your task")
    print("2. Remove your Task")
    print("3. Display your Tasks")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        print("Your task list:")
        show_tasks()
    elif choice == '4':
        print("Closing!")
        break
    else:
        print("Enter valid choice")

# My To-Do List App - By Pranavi
# KITS CSD - Level 3 Project | github.com/rachamallapranavi/todo-list-app

todo_list = []

def show_menu():
    print("\n--- My To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task():
    task = input("Enter new task: ").strip()
    if task:
        todo_list.append(task)
        print(f"✅ Added: {task}")
    else:
        print("⚠️ Task cannot be empty!")

def view_tasks():
    print("\nYour Tasks:")
    if len(todo_list) == 0:
        print("No tasks yet! Add one.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def remove_task():
    if len(todo_list) == 0:
        print("No tasks to remove!")
        return
    view_tasks()
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(todo_list):
            removed = todo_list.pop(num - 1)
            print(f"❌ Removed: {removed}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")

# Main Loop
while True:
    show_menu()
    choice = input("Choose option (1-4): ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Bye! Good job today! 👋")
        break
    else:
        print("Please choose 1-4 only")
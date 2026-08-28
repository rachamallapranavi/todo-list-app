# My To-Do List App - By Pranavi
# KITS CSD - Level 3 Project

todo_list = []

def show_menu():
    print("\n--- My To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose option (1-4): ")

    if choice == "1":
        task = input("Enter new task: ")
        todo_list.append(task)
        print(f"✅ Added: {task}")

    elif choice == "2":
        print("\nYour Tasks:")
        if len(todo_list) == 0:
            print("No tasks yet!")
        else:
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(todo_list) == 0:
            print("No tasks to remove!")
        else:
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(todo_list):
                removed = todo_list.pop(num - 1)
                print(f"❌ Removed: {removed}")
            else:
                print("Invalid number!")

    elif choice == "4":
        print("Bye! Good job today! 👋")
        break

    else:
        print("Please choose 1-4 only")
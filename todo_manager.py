tasks = []


def add_task():
    task = input("Enter task: ")

    if task.strip():
        tasks.append({
            "task": task,
            "completed": False
        })

        print("Task added.")
    else:
        print("Task cannot be empty.")


def view_tasks():

    if not tasks:
        print("No tasks available.")
        return

    print("\n--- Tasks ---")

    for index, item in enumerate(tasks, start=1):

        status = "✓" if item["completed"] else " "

        print(
            f"{index}. [{status}] "
            f"{item['task']}"
        )


def complete_task():

    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task completed.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Enter a valid number.")


def delete_task():

    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Enter a valid number.")


while True:

    print("\n--- To-Do Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        break

    else:
        print("Invalid choice.")
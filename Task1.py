class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter the task: ")
        self.tasks.append({"task": task, "completed": False})
        print(f'Added task: "{task}"')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\nTo-Do List:")
        for idx, task in enumerate(self.tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f'{idx}. [{status}] {task["task"]}')
        print()  # For a new line after the list

    def update_task(self):
        self.view_tasks()
        try:
            index = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            self.tasks[index - 1]["task"] = new_task
            print(f'Updated task {index} to: "{new_task}"')
        except (ValueError, IndexError):
            print(f'Error: Invalid task number.')

    def delete_task(self):
        self.view_tasks()
        try:
            index = int(input("Enter the task number to delete: "))
            task = self.tasks.pop(index - 1)
            print(f'Deleted task: "{task["task"]}"')
        except (ValueError, IndexError):
            print(f'Error: Invalid task number.')

    def mark_task_completed(self):
        self.view_tasks()
        try:
            index = int(input("Enter the task number to mark as completed: "))
            self.tasks[index - 1]["completed"] = True
            print(f'Marked task {index} as completed.')
        except (ValueError, IndexError):
            print(f'Error: Invalid task number.')

    def print_menu(self):
        print("""
        To-Do List Application Menu:
        1. Add a new task
        2. View all tasks
        3. Update a task
        4. Delete a task
        5. Mark a task as completed
        6. Show this menu
        7. Exit
        """)

def main():
    todo_list = TodoList()
    todo_list.print_menu()

    while True:
        try:
            choice = int(input("\nEnter your choice (1-7): "))
            if choice == 1:
                todo_list.add_task()
            elif choice == 2:
                todo_list.view_tasks()
            elif choice == 3:
                todo_list.update_task()
            elif choice == 4:
                todo_list.delete_task()
            elif choice == 5:
                todo_list.mark_task_completed()
            elif choice == 6:
                todo_list.print_menu()
            elif choice == 7:
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()

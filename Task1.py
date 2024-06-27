import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        # Create UI elements
        self.tasks = []
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.mark_complete_button = tk.Button(self.root, text="Mark as Complete", command=self.mark_complete)
        self.mark_complete_button.pack(pady=5)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            new_task = simpledialog.askstring("Update Task", "Update the task:", initialvalue=self.tasks[selected_task_index]["task"])
            if new_task:
                self.tasks[selected_task_index]["task"] = new_task
                self.update_task_listbox()
        else:
            messagebox.showwarning("Update Task", "Please select a task to update.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Delete Task", "Please select a task to delete.")

    def mark_complete(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            self.tasks[selected_task_index]["completed"] = not self.tasks[selected_task_index]["completed"]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Mark as Complete", "Please select a task to mark as complete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = task["task"] + (" [Completed]" if task["completed"] else "")
            self.task_listbox.insert(tk.END, display_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

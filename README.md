To-Do List Application


Overview

This is a simple To-Do List Application built using Python's tkinter library. It allows users to add, update, delete, and mark tasks as complete.

Features

Add Task: Add a new task to the list.
Update Task: Modify an existing task.
Delete Task: Remove a selected task from the list.
Mark as Complete: Mark a task as completed or incomplete.

Usage

Add Task: Click the "Add Task" button and enter the task description.
Update Task: Select a task from the list, click the "Update Task" button, and modify the task description.
Delete Task: Select a task from the list and click the "Delete Task" button.
Mark as Complete: Select a task from the list and click the "Mark as Complete" button. Completed tasks are indicated with "[Completed]".

Code Structure

TodoApp Class: Main class containing all the functionality and UI elements.
__init__(self, root): Initializes the UI elements and the task list.
add_task(self): Adds a new task to the list.
update_task(self): Updates the selected task.
delete_task(self): Deletes the selected task.
mark_complete(self): Marks the selected task as complete/incomplete.
update_task_listbox(self): Refreshes the task list display.

Author
Anshika Pandey

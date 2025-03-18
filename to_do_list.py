import tkinter as tk
from tkinter import messagebox, simpledialog

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        return f"{'[✓] ' if self.completed else '[✗] '} {self.description}"

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List Application")
        self.tasks = []

        self.listbox = tk.Listbox(self.master, width=50, height=15)
        self.listbox.pack(pady=10)

        self.add_button = tk.Button(self.master, text="Add Task", fg="white", bg='blue', command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(self.master, text="Mark as Completed", fg="white", bg='green', command=self.mark_completed)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(self.master, text="Delete Task", fg="white", bg='red', command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.filter_button = tk.Button(self.master, text="Filter Tasks",fg="white", bg='black', command=self.filter_tasks)
        self.filter_button.pack(pady=5) 
        self.exit_button = tk.Button(self.master, text="Exit", fg="white", bg='red', command=self.exit_app)
        self.exit_button.pack(pady=5)

        

    def add_task(self):
        description = simpledialog.askstring("Input", "Enter task description:")
        if description:
            task = Task(description)
            self.tasks.append(task)
            self.update_listbox()

    def mark_completed(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.tasks[selected_index].completed = True
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def delete_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def filter_tasks(self):
        filter_status = simpledialog.askstring("Input", "Filter by (c)ompleted or (p)ending?").lower()
        filtered_tasks = []
        if filter_status == 'c':
            filtered_tasks = [task for task in self.tasks if task.completed]
        elif filter_status == 'p':
            filtered_tasks = [task for task in self.tasks if not task.completed]
        else:
            messagebox.showwarning("Warning", "Invalid choice.")
            return

        self.listbox.delete(0, tk.END)
        for task in filtered_tasks:
            self.listbox.insert(tk.END, str(task))

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, str(task))

    def exit_app(self):
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
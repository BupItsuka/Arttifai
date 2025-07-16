import tkinter as tk
from tkinter import messagebox

class ToDo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []
        self.task_entry = tk.Entry(root, width=45)
        self.task_entry.pack(pady=10)
        self.task_listbox = tk.Listbox(root, width=50, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=2)
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=2)
        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.complete_task)
        self.complete_button.pack(pady=2)
        self.task_entry.bind("<Return>", lambda event: self.add_task())
        self.update_listbox()

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"task": task_text, "completed": False})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty.")
        self.task_entry.focus()


    def complete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_listbox()

    def remove_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            del self.tasks[selected[0]]
            self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display = f"[{'✓' if task['completed'] else ' '}] {task['task']}"
            self.task_listbox.insert(tk.END, display)
            if task["completed"]:
                self.task_listbox.itemconfig(tk.END, fg="blue")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDo(root)
    root.mainloop()

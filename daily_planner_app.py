import tkinter as tk
from tkinter import messagebox

class DailyPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Planner App")

        # Create frames
        self.top_frame = tk.Frame(self.root)
        self.middle_frame = tk.Frame(self.root)
        self.bottom_frame = tk.Frame(self.root)

        # Create labels and entry fields
        self.task_label = tk.Label(self.top_frame, text="Task:")
        self.task_entry = tk.Entry(self.top_frame, width=40)
        self.date_label = tk.Label(self.top_frame, text="Date:")
        self.date_entry = tk.Entry(self.top_frame, width=40)

        # Create buttons
        self.add_button = tk.Button(self.middle_frame, text="Add Task", command=self.add_task)
        self.view_button = tk.Button(self.middle_frame, text="View Tasks", command=self.view_tasks)
        self.exit_button = tk.Button(self.bottom_frame, text="Exit", command=self.root.quit)

        # Layout
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        self.task_label.pack(side=tk.LEFT)
        self.task_entry.pack(side=tk.LEFT)
        self.date_label.pack(side=tk.LEFT)
        self.date_entry.pack(side=tk.LEFT)
        self.add_button.pack(side=tk.LEFT)
        self.view_button.pack(side=tk.LEFT)
        self.exit_button.pack(side=tk.BOTTOM)

    def add_task(self):
        # Add task logic here
        pass

    def view_tasks(self):
        # View tasks logic here
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = DailyPlannerApp(root)
    root.mainloop()
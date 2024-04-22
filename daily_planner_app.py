import sys
from PyQt5 import QtWidgets, QtCore
from daily_planner_logic import UserProfile

class DailyPlannerApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.user = UserProfile()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Daily Planner App")

        # Create labels and entry fields
        self.task_label = QtWidgets.QLabel("Task:")
        self.task_entry = QtWidgets.QLineEdit()
        self.date_label = QtWidgets.QLabel("Due Date:")
        self.date_entry = QtWidgets.QLineEdit()

        # Connect the returnPressed signal to the add_task method
        self.task_entry.returnPressed.connect(self.add_task)

        # Create buttons
        self.add_button = QtWidgets.QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        self.view_button = QtWidgets.QPushButton("View Tasks")
        self.view_button.clicked.connect(self.view_tasks)
        self.exit_button = QtWidgets.QPushButton("Exit")
        self.exit_button.clicked.connect(self.close)
        self.completed_button = QtWidgets.QPushButton("Mark as Completed")
        self.completed_button.clicked.connect(self.mark_completed)

        # Create a QListWidget to display tasks
        self.task_list = QtWidgets.QListWidget()

        # Create a QListWidget to display completed tasks
        self.completed_list = QtWidgets.QListWidget()

        # Layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.task_label)
        layout.addWidget(self.task_entry)
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_entry)
        layout.addWidget(self.add_button)
        layout.addWidget(self.view_button)
        layout.addWidget(self.exit_button)
        layout.addWidget(self.completed_button)
        layout.addWidget(self.task_list)
        layout.addWidget(self.completed_list)

        self.setLayout(layout)

    def add_task(self):
        task_name = self.task_entry.text()
        due_date = self.date_entry.text()
        self.user.tasks.append({"name": task_name, "due_date": due_date})
        self.task_entry.clear()
        self.date_entry.clear()
        self.task_list.addItem(f"{task_name} (Due: {due_date})")

    def view_tasks(self):
        self.task_list.clear()
        for task in self.user.tasks:
            self.task_list.addItem(f"{task['name']} (Due: {task['due_date']})")

    def mark_completed(self):
        selected_index = self.task_list.currentRow()
        if selected_index >= 0:
            task = self.user.tasks.pop(selected_index)
            #print("Task:", task)  # Add this print statement
            self.completed_list.addItem(f"{task['name']} (Due: {task['due_date']})")
            self.task_list.clear()
            for task in self.user.tasks:
                self.task_list.addItem(f"{task['name']} (Due: {task['due_date']})")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DailyPlannerApp()
    window.show()
    sys.exit(app.exec_())
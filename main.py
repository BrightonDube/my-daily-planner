class UserProfile:
    def __init__(self):
        self.name = ""
        self.goals = []
        self.preferences = {
		    "theme": "default",
		    "font_size": 12,
		    "color_scheme": "light"
		}
		

def main():
    user = UserProfile()
    user.name = "John Doe"
    user.tasks = []

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(user)
        elif choice == "2":
            view_tasks(user)
        elif choice == "3":
            break
        else:
             print("Invalid choice. Please try again.")

def show_menu():
	# Menu logic here
    print("Daily Planner Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

def add_task(user):
    task_name = input("Enter task name: ")
    user.tasks.append(task_name)
    print("Task added successfully!")

def view_tasks(user):
    if not user.tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for i, task in enumerate(user.tasks, 1):
            print(f"{i}. {task}")

if __name__ == "__main__":
	main()
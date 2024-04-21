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


if __name__ == "__main__":
	main()
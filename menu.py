class Menu:
    def __init__(self, service):
        self.service = service

    def print_menu(self):
        print("1. List notes")
        print("2. Add note")
        print("3. Edit note")
        print("4. Delete note")
        print("5. Exit")

    def run(self):
        while True:
            self.print_menu()
            choice = input("Enter your choice (1-5): ")
            if choice == "1":
                self.service.list_notes()
            elif choice == "2":
                self.service.add_note()
            elif choice == "3":
                self.service.edit_note()
            elif choice == "4":
                self.service.delete_note()
            elif choice == "5":
                print("Exiting the application...")
                break
            else:
                print("Invalid choice. Please try again.")

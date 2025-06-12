from auth import AuthManager

def main():
    auth = AuthManager()
    print("Welcome to the Task Manager!")
    
    while True:
        print("\nMenu:")
        print("1. Register User")
        print("2. Login User")
        print("3. Update Password")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            try:
                auth.register(username, password)
            except ValueError as e:
                print(f"❌ {e}")
        
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            try:
               auth.register(username, password)
            except ValueError as e:
                print(f"❌ {e}")
        
        elif choice == '3':
            username = input("Enter username: ")
            old_password = input("Enter old password: ")
            new_password = input("Enter new password: ")
            try:
                auth.update_password(username, old_password, new_password)
            except ValueError as e:
                print(f"❌ {e}")
        
        elif choice == '4':
            print("Exiting Task Manager. Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

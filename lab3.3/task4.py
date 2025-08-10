# INSERT_YOUR_CODE
users_db = {}

def register_user():
    print("=== Register User ===")
    username = input("Enter a username: ").strip()
    if username in users_db:
        print("Username already exists. Please choose a different username.")
        return
    password = input("Enter a password: ").strip()
    users_db[username] = password
    print(f"User '{username}' registered successfully.")

def login_user():
    print("=== Login User ===")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    if users_db.get(username) == password:
        print(f"Login successful. Welcome, {username}!")
    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select an option: ").strip()
        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

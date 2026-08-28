while True:
    users = {}

    print("Welcome to the login system!")
    print("Please choose an option:")
    print("1. Register")
    print("2. Login")
    print("3. Exit") 
    choice = input("Enter your choice (1, 2, or 3): ")
    while choice not in ['1', '2', '3']:
        print("invalid choice. Please try again.")
        choice = input("Enter your choice (1, 2, or 3): ")
    if choice == '1':
        username = input("Enter a username: ")
        while username in users:
            print("Username already exists. Please try again.")
            username = input("Enter a username: ")
        password = input("Enter a password: ")
        users[username] = password
    if choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in users and users[username] == password:
            print("Login successful!")
        else:
            print("Invalid username or password.")
    if choice == '3':
        print("Thank you for using the login system!")
        break  
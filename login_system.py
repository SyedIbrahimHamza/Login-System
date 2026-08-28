users = {}

print("Welcome to the login system!")
print("Please choose an option:")
print("1. Register")
print("2. Login")
choice = input("Enter your choice (1 or 2): ")
while choice not in ['1', '2']:
    print("invalid choice. Please try again.")
    choice = input("Enter your choice (1 or 2): ")
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
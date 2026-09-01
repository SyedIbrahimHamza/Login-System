Login System

A simple terminal-based Login System built with Python. The program allows users to register with a username and password, log in using their registered credentials, and exit the program.

User information is stored in a Python dictionary while the program is running.

Features
Register a new user
Prevent empty usernames
Prevent duplicate usernames
Enter and confirm passwords
Prevent empty passwords
Validate menu choices
Login with registered credentials
Verify username and password
Display login success or failure messages
Continuously display the menu
Exit the program
Menu
Welcome to the login system!

Please choose an option:
1. Register
2. Login
3. Exit


The program continues displaying the menu until the user selects option 3.

Register

Select 1 to register a new user.

The program asks for:

Username
Password
Password confirmation

The username cannot be empty and cannot already exist in the users dictionary.

The password and confirmation must match, and the password cannot be empty.

Example:

Enter your choice (1, 2, or 3): 1
Enter a username: Ali
Enter a password: 12345
Confirm your password: 12345
Registration successful!


User information is stored using:

users[username] = password

Login

Select 2 to log in with a registered username and password.

Example:

Enter your choice (1, 2, or 3): 2
Enter your username: Ali
Enter your password: 12345
Login successful!


If the username or password is incorrect:

Invalid username or password.


The login check is performed using:

if username in users and users[username] == password:
    print("Login successful!")
else:
    print("Invalid username or password.")

Menu Validation

The program only accepts 1, 2, or 3 as menu choices.

If an invalid choice is entered, the program asks again:

Enter your choice (1, 2, or 3): 7
Invalid choice. Please try again.
Enter your choice (1, 2, or 3): 2

User Data

Registered users are stored in a Python dictionary:

users = {}


For example:

users = {
    "Ali": "12345",
    "Ahmed": "67890"
}


The username is used as the dictionary key and the password is stored as its value.

Note: User data is stored only while the program is running. It is not saved permanently to a file or database.

Exit

Select 3 to exit the program.

The program displays:

Thank you for using the login system!


The break statement stops the main while True loop:

elif choice == '3':
    print("Thank you for using the login system!")
    break

Python Concepts Used

This project practices several Python fundamentals:

Dictionaries
Lists
while loops
while True
Conditional statements
if, elif, and else
User input with input()
String comparison
Dictionary lookup and assignment
Logical operators
Comparison operators
break
Input validation
How to Run

Make sure Python is installed on your computer.

Run the program from the terminal:

python login_system.py


The program will then display the login system menu.

Project Status

Complete — Basic Version

The current version includes:

Registration
Username validation
Duplicate username prevention
Password confirmation
Empty password validation
Login verification
Menu validation
Continuous menu
Exit functionality

The project is designed as a Python practice project for learning basic programming concepts and building a simple login and registration system.

Author

Built as a Python practice project to learn dictionaries, loops, user input, input validation, conditional logic, and basic login and registration functionality.
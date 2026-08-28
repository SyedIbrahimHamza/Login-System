Login System

A simple terminal-based Login System built with Python. The program provides a menu-driven interface that allows users to register with a username and password, log in using their registered credentials, and exit the program.

The system validates menu choices, prevents duplicate usernames, stores user information in a Python dictionary, verifies login credentials, and continuously displays the menu until the user chooses to exit.

What It Does

The program currently allows you to:

Display a welcome message
Display registration, login, and exit options
Validate the menu choice
Store user information using a Python dictionary
Take username and password input
Register new users
Prevent duplicate usernames
Login using registered credentials
Verify usernames and passwords
Display login success or failure messages
Continue displaying the menu using a while True loop
Exit the program when the user chooses option 3
Current Features
Option	Feature	Status
1	Register	✅ Complete
2	Login	✅ Complete
3	Exit	✅ Complete
4	Menu Choice Validation	✅ Complete
5	User Dictionary	✅ Complete
6	Duplicate Username Check	✅ Complete
7	Login Verification	✅ Complete
8	Continuous Menu	✅ Complete
How to Run

Make sure Python is installed on your computer.

Run the program from the terminal:

python login_system.py


The program will display the menu and ask the user to select an option.

Menu
Welcome to the login system!
Please choose an option:
1. Register
2. Login
3. Exit
Enter your choice (1, 2, or 3):


The menu continues to appear until the user chooses option 3.

Register

Select 1 to register a new user.

The program asks for:

Username
Password

The username is checked to make sure it does not already exist in the users dictionary.

Example
Enter your choice (1, 2, or 3): 1
Enter a username: Ali
Enter a password: 12345


The information is stored using:

users[username] = password

Duplicate Username Check

If the username already exists, the program asks the user to enter another username.

Example:

Enter a username: Ali
Username already exists. Please try again.
Enter a username: Ahmed


This prevents multiple users from being registered with the same username.

The check is performed using:

while username in users:
    print("Username already exists. Please try again.")
    username = input("Enter a username: ")

Login

Select 2 to log in with a registered username and password.

The program asks for:

Username
Password

It then checks whether the username exists and whether the entered password matches the stored password.

Successful Login
Enter your choice (1, 2, or 3): 2
Enter your username: Ali
Enter your password: 12345
Login successful!

Failed Login

If the username does not exist or the password is incorrect, the program displays:

Invalid username or password.


The login verification uses:

if username in users and users[username] == password:
    print("Login successful!")
else:
    print("Invalid username or password.")

Exit

Select 3 to exit the program.

The program displays a goodbye message:

Enter your choice (1, 2, or 3): 3
Thank you for using the login system!


The break statement stops the while True loop:

if choice == '3':
    print("Thank you for using the login system!")
    break

Menu Choice Validation

The program makes sure that the user enters 1, 2, or 3.

This is done using:

while choice not in ['1', '2', '3']:
    print("invalid choice. Please try again.")
    choice = input("Enter your choice (1, 2, or 3): ")


If an invalid option is entered, the program continues asking for a valid choice.

Example
Enter your choice (1, 2, or 3): 7
invalid choice. Please try again.
Enter your choice (1, 2, or 3): 2

Continuous Menu

The program uses:

while True:


to continuously display the menu.

This allows the user to:

Register a user
Return to the menu
Log in
Return to the menu
Exit when finished

The program stops only when the user selects option 3.

User Data

The program uses a Python dictionary to store registered users:

users = {}


When a user registers, the username becomes the dictionary key and the password becomes the value.

For example:

users = {
    'Ali': '12345',
    'Ahmed': '67890'
}


Here:

Ali is a username
12345 is Ali's password
Ahmed is another username
67890 is Ahmed's password
Python Concepts Used

This project practices the following Python concepts:

Dictionaries — storing usernames and passwords
Lists — storing valid menu choices
While loops — creating a continuous menu and validating input
Conditional statements — handling registration, login, and exit
User input — using input() to receive information
Strings — handling usernames, passwords, and messages
Dictionary lookup — checking whether a username exists
Dictionary assignment — storing new username and password data
Logical operators — using and to verify login conditions
Comparison operators — comparing passwords
break statement — stopping the main program loop
Functions

The current version does not use custom functions such as:

def register():


or:

def login():


The registration and login logic is currently written directly inside the main program loop.

Functions can be introduced in a future version to make the program more organized, reusable, and easier to maintain.

What I Learned

While building this project, I practiced:

Creating and using dictionaries
Creating lists
Taking user input with input()
Validating user input
Using while loops
Creating an infinite loop with while True
Using break to exit a loop
Checking whether a value exists inside a list
Checking whether a key exists in a dictionary
Storing username and password data
Using conditional logic
Using the and logical operator
Comparing values
Preventing duplicate usernames
Verifying login credentials
Handling successful and failed login attempts
Creating an exit option
Building a continuous terminal-based menu
Project Status

This project is currently in progress.

Implemented Features
✅ Welcome message
✅ Register and Login menu
✅ Exit option
✅ User dictionary
✅ Menu choice validation
✅ Invalid choice handling
✅ Continuous menu using while True
✅ Repeated input using while loops
✅ Username input
✅ Password input
✅ Store username and password
✅ Prevent duplicate usernames
✅ Login functionality
✅ Username verification
✅ Password verification
✅ Login success message
✅ Login failure message
✅ Exit message
✅ Exit using break
Not Yet Implemented
❌ Functions for registration and login
❌ Empty username validation
❌ Empty password validation
❌ Password confirmation
❌ Maximum login attempts
❌ Login retry limit
❌ Logout functionality
❌ Persistent user storage
❌ Password encryption/hashing
Future Improvements

Planned improvements include:

Add a register() function
Add a login() function
Validate empty usernames
Validate empty passwords
Add password confirmation during registration
Add a maximum number of login attempts
Add login retry functionality
Add logout functionality
Improve error messages
Improve the overall terminal interface
Store users permanently using a file or database
Hash passwords instead of storing them as plain text
Add different user roles
Improve the menu structure
Technologies Used
Python
Dictionaries
Lists
while loops
Conditional statements
input()
Strings
Dictionary operations
Logical operators
break
Author

Built as a Python practice project to learn the fundamentals of dictionaries, lists, loops, user input, input validation, conditional logic, and the basic structure of a login and registration system.
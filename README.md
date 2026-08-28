Login System

A simple terminal-based Login System built with Python. The program provides a basic menu-driven interface that allows users to register with a username and password and log in using their registered credentials.

The program validates the user's menu choice, prevents duplicate usernames, stores user information in a Python dictionary, and verifies login credentials.

What It Does

The program currently allows you to:

Display a welcome message
Display registration and login options
Validate the menu choice
Store user information using a Python dictionary
Take username and password input
Register new users
Prevent duplicate usernames
Login using registered credentials
Verify usernames and passwords
Display login success or failure messages
Current Features
Option	Feature	Status
1	Register	✅ Complete
2	Login	✅ Complete
3	Menu Choice Validation	✅ Complete
4	User Dictionary	✅ Complete
5	Duplicate Username Check	✅ Complete
6	Login Verification	✅ Complete
How to Run

Make sure Python is installed on your computer.

Run the program from the terminal:

python login_system.py


The program will display a welcome message and ask the user to select an option.

Menu
Welcome to the login system!
Please choose an option:
1. Register
2. Login
Enter your choice (1 or 2):


The menu choice is validated using a while loop. If an invalid option is entered, the program continues asking the user to enter either 1 or 2.

Example
Enter your choice (1 or 2): 5
invalid choice. Please try again.
Enter your choice (1 or 2): 1

User Data

The program uses a Python dictionary to store registered users:

users = {}


When a user registers, their username is used as the dictionary key and their password is stored as the value.

For example:

users = {
    'Ali': '12345',
    'Ahmed': '67890'
}


Here:

Ali is the username
12345 is Ali's password
Ahmed is another username
67890 is Ahmed's password
Register

Select 1 to register a new user.

The program asks the user for:

Username
Password

The username is checked to make sure it does not already exist in the users dictionary.

Example
Enter your choice (1 or 2): 1
Enter a username: Ali
Enter a password: 12345


The information is stored using:

users[username] = password

Duplicate Username Check

If the username already exists, the program asks the user to enter another username:

Enter a username: Ali
Username already exists. Please try again.
Enter a username: Ahmed


This prevents multiple users from being registered with the same username.

The check is performed using:

while username in users:
    print("Username already exists. Please try again.")
    username = input("Enter a username: ")

Login

Select 2 to log in with an existing username and password.

The program asks for:

Username
Password

It then checks whether the username exists and whether the entered password matches the stored password.

Successful Login
Enter your choice (1 or 2): 2
Enter your username: Ali
Enter your password: 12345
Login successful!


The login is verified using:

if username in users and users[username] == password:
    print("Login successful!")

Failed Login

If the username does not exist or the password is incorrect, the program displays:

Invalid username or password.


The program uses:

else:
    print("Invalid username or password.")


This prevents the user from logging in with incorrect credentials.

Menu Choice Validation

The program makes sure that the user enters either 1 or 2.

This is done using:

while choice not in ['1', '2']:
    print("invalid choice. Please try again.")
    choice = input("Enter your choice (1 or 2): ")


The list:

['1', '2']


contains the valid menu choices.

If the user's input is not found in the list, the while loop continues and asks for another choice.

Duplicate Username Validation

The registration system checks whether the username is already stored in the dictionary:

while username in users:
    print("Username already exists. Please try again.")
    username = input("Enter a username: ")


This means a username cannot be registered more than once.

Login Verification

The login system checks two conditions:

The username exists in the users dictionary.
The password matches the password stored for that username.

This is done with:

if username in users and users[username] == password:
    print("Login successful!")
else:
    print("Invalid username or password.")


For example, if the dictionary contains:

users = {
    'Ali': '12345'
}


Entering:

Username: Ali
Password: 12345


will result in:

Login successful!


But entering the wrong password:

Username: Ali
Password: 99999


will result in:

Invalid username or password.

Python Concepts Used

This project practices the following Python concepts:

Dictionaries — storing usernames and passwords
Lists — storing valid menu choices
While loops — repeatedly asking for valid input
Conditional statements — handling registration and login
User input — using input() to receive information
Strings — handling usernames, passwords, and messages
Dictionary lookup — checking whether a username exists
Dictionary assignment — storing a new username and password
Logical operators — checking multiple login conditions using and
Comparison operators — comparing the entered password with the stored password
Functions

The current version does not use custom functions such as:

def register():


or:

def login():


The registration and login logic is currently written directly in the main program.

Functions can be introduced in a future version to make the program more organized, reusable, and easier to maintain.

What I Learned

While building this project, I practiced:

Creating and using dictionaries
Creating lists
Taking user input with input()
Validating user input
Using while loops
Checking whether a value exists inside a list
Checking whether a key exists in a dictionary
Storing username and password data
Using conditional logic
Using the and logical operator
Preventing duplicate usernames
Verifying login credentials
Handling successful and failed login attempts
Building a basic terminal-based authentication system
Project Status

This project is currently in progress.

Implemented Features
✅ Welcome message
✅ Register and Login menu
✅ User dictionary
✅ Menu choice validation
✅ Invalid choice handling
✅ Repeated input using a while loop
✅ Username input
✅ Password input
✅ Store username and password
✅ Prevent duplicate usernames
✅ Login functionality
✅ Username verification
✅ Password verification
✅ Login success message
✅ Login failure message
Not Yet Implemented
❌ Exit option
❌ Logout option
❌ Functions for registration and login
❌ Empty username validation
❌ Empty password validation
❌ Password confirmation
❌ Maximum login attempts
❌ Login retry system
❌ Persistent user storage
❌ Password encryption/hashing
Future Improvements

Planned improvements include:

Add a register() function
Add a login() function
Add an exit option
Add a logout option
Validate empty usernames
Validate empty passwords
Add password confirmation during registration
Allow users to retry incorrect login credentials
Add a maximum number of login attempts
Improve error messages
Improve the overall terminal interface
Store users permanently using a file or database
Hash passwords instead of storing them as plain text
Add a main program loop so users can register and log in multiple times
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
Author

Built as a Python practice project to learn the fundamentals of dictionaries, lists, loops, user input, input validation, conditional logic, and the basic structure of a login and registration system.
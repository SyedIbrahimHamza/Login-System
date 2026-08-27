Login System

A simple terminal-based Login System built with Python. The program provides a basic menu-driven interface that allows users to register with a username and password. It also validates the user's menu choice and prevents duplicate usernames.

What It Does

The program currently allows you to:

Display a welcome message
Display registration and login options
Validate the menu choice
Store user information using a Python dictionary
Take username and password input
Register new users
Prevent duplicate usernames
Current Features
Option	Feature	Status
1	Register	✅ Complete
2	Login	🚧 In Progress
3	Menu Choice Validation	✅ Complete
4	User Dictionary	✅ Complete
5	Duplicate Username Check	✅ Complete
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

The username is then checked to make sure it does not already exist in the users dictionary.

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

Login

The login option is displayed in the menu, but the login functionality has not yet been implemented.

The planned login feature will ask for:

Username
Password

It will then check whether the username exists and whether the password matches the stored password.

Planned successful login:

Enter your choice (1 or 2): 2
Enter username: Ali
Enter password: 12345
Login successful.


Planned failed login:

Invalid username or password.

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

Python Concepts Used

This project practices the following Python concepts:

Dictionaries — storing usernames and passwords
Lists — storing valid menu choices
While loops — repeatedly asking for valid input
Conditional statements — handling different menu choices
User input — using input() to receive information
Strings — handling usernames, passwords, and messages
Dictionary lookup — checking whether a username already exists
Dictionary assignment — storing a new username and password
Functions

Custom functions such as:

def register():


and:

def login():


have not yet been added.

They can be introduced in a future version to make the program more organized and easier to maintain.

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
Preventing duplicate usernames
Planning a login and registration system
Project Status

This project is currently in progress.

Implemented Features
 Welcome message
 Register and Login menu
 User dictionary created
 Menu choice validation
 Invalid choice handling
 Repeated input using a while loop
 Username input
 Password input
 Store username and password
 Prevent duplicate usernames
Not Yet Implemented
 Login user
 Verify username
 Verify password
 Login success message
 Login failure message
 Exit option
 Logout option
 Functions for registration and login
 Empty username validation
 Empty password validation
 Password confirmation
 Maximum login attempts
Future Improvements

Planned improvements include:

Add a register() function
Add a login() function
Implement login verification
Validate empty usernames
Validate empty passwords
Add password confirmation during registration
Add an exit option
Add a logout option
Improve error messages
Allow users to retry incorrect login credentials
Add a maximum number of login attempts
Improve the overall terminal interface
Technologies Used
Python
Dictionaries
Lists
while loops
Conditional statements
input()
Strings
Dictionary operations
Author

Built as a Python practice project to learn the fundamentals of dictionaries, lists, loops, user input, input validation, and the basic structure of a login and registration system.
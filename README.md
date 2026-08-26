Login System

A simple terminal-based Login System built with Python. The program provides a basic menu-driven interface that allows users to register and log in using a username and password. It also validates the user's menu choice before continuing.

What It Does

The program currently allows you to:

Display a welcome message
Display registration and login options
Validate the menu choice
Store user information using a Python dictionary
Take username and password input
Register new users
Login registered users
Check username and password
Handle invalid menu choices
Use a loop to repeatedly ask for a valid choice
Current Features
Option	Feature	Status
1	Register	🚧 In Progress
2	Login	🚧 In Progress
-	Menu Choice Validation	✅ Complete
-	User Dictionary	✅ Complete
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


The menu choice is validated using a while loop. If an invalid option is entered, the program asks the user to enter either 1 or 2.

Example:

Enter your choice (1 or 2): 5
invalid choice. Please try again.
Enter your choice (1 or 2): 1

User Data

The program uses a Python dictionary to store users:

users = {}


The dictionary is currently empty when the program starts.

The planned structure for storing a registered user is:

{
    'username': 'Ali',
    'password': '12345'
}


The dictionary can be used to associate a username with its password.

Register

Select 1 to register a new user.

The registration feature is planned to ask the user for:

Username
Password

The entered information can then be stored in the users dictionary.

Example:

Enter your choice (1 or 2): 1

Enter Username: Ali
Enter Password: 12345

Registration successful.


This feature is currently part of the project structure but the registration logic has not yet been implemented in the provided code.

Login

Select 2 to log in.

The login feature is planned to ask the user for:

Username
Password

The program can then check whether the username exists and whether the entered password matches the stored password.

Example:

Enter your choice (1 or 2): 2

Enter Username: Ali
Enter Password: 12345

Login successful.


If the credentials are incorrect:

Invalid username or password.


The login logic has not yet been implemented in the provided code.

Menu Choice Validation

The program makes sure that the user enters either 1 or 2.

This is done using:

while choice not in ['1', '2']:
    print("invalid choice. Please try again.")
    choice = input("Enter your choice (1 or 2): ")


The list:

['1', '2']


contains the valid menu choices.

If the user's input is not found in this list, the while loop continues and asks for another choice.

Data Structure

The project currently uses a dictionary to store user information.

The main dictionary is:

users = {}


A dictionary is useful for storing information using keys and values.

For example:

users = {
    'Ali': '12345',
    'Ahmed': '67890'
}


Here:

Ali is the username
12345 is the password
Ahmed is another username
67890 is the password
Python Concepts Used

While building this project, the following Python concepts are being practiced:

Dictionaries — storing user information
Lists — storing valid menu choices
While loops — repeatedly asking for valid input
Conditional logic — checking whether the choice is valid
User input — using input() to receive information
Strings — handling menu choices and messages
Dictionary lookup — planned for checking registered users
Functions

Custom functions such as:

def register():


and:

def login():


are not yet present in the provided code.

They can be added as a future improvement to make the program more organized.

What I Learned

While building this project, I practiced:

Creating and using dictionaries
Creating lists
Taking user input with input()
Validating user input
Using while loops
Checking whether a value exists inside a list
Working with strings
Planning a user registration system
Planning a login verification system
Organizing data using key-value pairs
Project Status

This project is currently in progress.

Implemented Features
✅ Welcome message
✅ Register and Login menu
✅ User dictionary created
✅ Menu choice validation
✅ Invalid choice handling
✅ Repeated input using a while loop
Not Yet Implemented
⬜ Register user
⬜ Store username and password
⬜ Login user
⬜ Verify username
⬜ Verify password
⬜ Login success message
⬜ Login failure message
⬜ Exit option
⬜ Functions for registration and login
Future Improvements

Planned improvements include:

Add a register() function
Add a login() function
Store registered users in the dictionary
Prevent duplicate usernames
Validate empty usernames
Validate empty passwords
Add password confirmation during registration
Add a logout option
Add an exit option
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
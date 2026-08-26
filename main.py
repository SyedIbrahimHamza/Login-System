#login system
users = {}

print("Welcome to the login system!")
print("Please choose an option:")
print("1. Register")
print("2. Login")
choice = input("Enter your choice (1 or 2): ")
while choice not in ['1', '2']:
    print("invalid choice. Please try again.")
    choice = input("Enter your choice (1 or 2): ")

username = input("Enter your username: ")
username = username.lower()
password = input("Enter your password: ")

if len(username) <= 3 or len(username) > 15:
    print("Please enter a username between 4 and 15 characters long.")
elif len(password) < 8:
    print("Please enter a password that is at least 8 characters long.")

else:
    print("Good job! You have a username.")
    print(f"Username: {username}")
    print(f"Password: {password}")

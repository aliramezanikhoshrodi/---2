username = input("Enter username: ")
if username == "admin":
    password = input("Enter your password")
    if password == "1234":
        print("Welcome, Admin")
    else:
        print("incorrect password")
else:
    print("incorrect username")
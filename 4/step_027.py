ticket = input("Do you have a ticket?(yes/no)")

if ticket == "yes":
    age = input("How old are you?")
    age = int(age)
    if age > 12:
        print("Welcome")
    else:
        print("You are not allowed to enter")
else:
    print("You are not allowed to enter without a ticket.")
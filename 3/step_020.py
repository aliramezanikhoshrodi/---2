age = input("Enter your age: ")
age = int(age)
if age > 18:
    age = True
else:
    age = False

has_gold_card = input("do you have a gold card?(yes/no)")

if has_gold_card == "yes":
    has_gold_card = True
else:
    has_gold_card = False

is_with_special_guest  = input("Are you with a special guest?(yes/no)")

if is_with_special_guest == "yes":
    is_with_special_guest = True
else:
    is_with_special_guest = False

if is_with_special_guest and has_gold_card and age:
    print("You can enter")
else:
    print("You can't enter")
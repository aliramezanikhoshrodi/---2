day = input("Is today Saturday? ")

amount = input("Enter your purchase amount: ")
amount = float(amount)
if day == "yes" or amount >= 100:
    print("True")
else:
    print("False")
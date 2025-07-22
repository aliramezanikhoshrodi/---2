number1 = input("enter number one: ")
number1 = int(number1)
number2 = input("enter number tow: ")
number2 = int(number2)
operator = input("choose(+, -, *, /)")

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
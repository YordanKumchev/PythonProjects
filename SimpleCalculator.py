print("""The idea behind this simple calculator is to get an user input for the
operator, then ask for a first and second number and do the maths""")


operator = input("Enter an operator ( + - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result,3))
elif operator == "-":
    result = num1 - num2
    print(round(result,3))
elif operator == "*":
    result = num1 * num2
    print(round(result,3))
elif operator == "/":
    result = num1 / num2
    print(round(result,3))
else:
    print(f"The {operator} is not a valid operator. Please choose another one.")
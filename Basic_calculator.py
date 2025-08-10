#Basic math calculator 
import math 
import math

# Print the welcome title
print("Welcome to Your Calculator")

# Input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Def function to perform the operation
def calculate(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation!"

# Perform calculation
result = calculate(num1, operation, num2)

# Display the result
print(f"The result of {num1} {operation} {num2} = {result}")
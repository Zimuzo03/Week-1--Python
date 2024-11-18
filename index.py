# Ask the user for two numbers and a mathematical operation

print("Let's perform a mathematical operation!")
num1 = float(input("Enter the **first number**: "))
num2 = float(input("Enter the **second number**: "))
operation = input("Enter the operation to perform (+, -, *, /): ")

# Perform the operation based on the user's input

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"

# Display the result

if isinstance(result, str):  # Handles error messages
    print(result)
else:
    print(f"{num1} {operation} {num2} = {result}")




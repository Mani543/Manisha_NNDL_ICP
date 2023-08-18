# Enter the input
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Perform arithmetic operations
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2

# Check if num2 is not zero to avoid division by zero
if number2 != 0:
    division = number1 / number2
else:
    division = "Cannot divide by zero"

# Print the results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

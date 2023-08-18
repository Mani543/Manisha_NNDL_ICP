# Entering the input
input_string = list(input("Enter the string: "))

# Delete 2 characters from input
chars_to_delete = min(2, len(input_string))
formatted_string = input_string[chars_to_delete:]

# Print the string after deletion
print("String after deleting 2 characters:", formatted_string)

# Reverse the resultant string
reversed_string = ''.join(reversed(formatted_string))

# Print the reversed string
print("Reversed string:", reversed_string)
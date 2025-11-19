"""
Question:4
The user enters a string containing a number (e.g., "45" ). Convert it to:
• an integer
• a float
• a string again
Print all three values with their types.
"""

input_number=input("Enter a number: ")
print(int(input_number),type(int(input_number)))
print(float(input_number),type(float(input_number)))
print(str(int(input_number)),type(str(int(input_number))))
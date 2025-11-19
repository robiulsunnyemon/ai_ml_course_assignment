"""
Question: 10
Take a decimal number as input(like 45.78) and output its:
    •integer part-45
    •fractional part-.78
"""


number=float(input("Enter a decimal number: "))
int_number=int(number/1)
decimal_values=number%int_number

print("integer value: ",int_number)
print("decimal values: ",decimal_values)
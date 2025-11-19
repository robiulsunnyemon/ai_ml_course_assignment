"""
Question: 6
Write a program to swap values of two numbers entered by the user.
"""

### with temp
number1=int(input("Enter 1st Number: "))
number2=int(input("Enter 2nd Number: "))
print(number1,number2)
temp=number1
number1=number2
number2=temp
print(number1,number2)

### without temp

number1=int(input("Enter 1st Number: "))
number2=int(input("Enter 2nd Number: "))
print(number1,number2)
number1=number1+number2
number2=number1-number2
number1=number1-number2
print(number1,number2)
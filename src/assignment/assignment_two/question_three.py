"""
Question: 3
Write a function that prints the digits of a number, n .
For eg: n = 312 , there are 3 digits in it 3, 1 and 2 & we need to print them.

"""

number=input("Enter the number: ")

def digit_print_int(n):
    digit_list = []
    while n!=0:
        digit=n%10
        n=int(n/10)
        digit_list.append(digit)

    digit_list.reverse()
    for i in digit_list:
        print(i)

digit_print_int(int(number))
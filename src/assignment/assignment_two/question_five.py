"""
Question: 5
Write a function to return the sum of digits of a number, n.
"""

def sum_of_digit(n):
    sum_=0
    while n!=0:
        digit=n%10
        sum_+=digit
        n=int(n/10)
    return sum_


print(sum_of_digit(99))

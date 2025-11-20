"""
Question: 4
Write a function to return the count the number of digits in a number, n
"""


number=int(input("Enter the number: "))

def digit_count(n):
    count=0
    while n!=0:
        digit=n%10
        n=int(n/10)
        count +=1
    return  count


print(digit_count(number))
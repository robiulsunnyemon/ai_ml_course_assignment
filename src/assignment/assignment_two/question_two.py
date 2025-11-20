"""
Question:2
Write a function that takes two integers a and b and prints all even
numbers between them (inclusive).

"""

def print_even_num(a,b):
    for i in range(a,b+1):
        if i%2==0:
            print(i)

print_even_num(3,9)

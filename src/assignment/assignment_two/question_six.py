"""
Question: 6
Write a program to print all numbers from 1 to 100 that are divisible by both 3
and 5.

"""

def print_one_hundred():
    for i in range(1,100):
        if (i%3==0) and (i%5==0):
            print(i)


print_one_hundred()

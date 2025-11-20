"""
Question: 7
Design a program to continuously input a number n from user & print if it is
positive or negative until the user enters “Quit”.

"""


def print_num():
    while True:
        n = input("Enter number: ")

        if n == "Quit":
            break

        # Check if input is a valid integer
        if n.lstrip("-").isdigit():
            n = int(n)
            if n < 0:
                print("It is negative")
            else:
                print("It is positive")
        else:
            print("Invalid input! Please enter a number.")


print_num()

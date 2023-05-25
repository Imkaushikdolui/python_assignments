# 14. Write a Python program to print the following floating numbers upto 2 decimal places.
# 3.1415926


def num(number):
    return "{:.2f}".format(number)

print(num(3.1415926))
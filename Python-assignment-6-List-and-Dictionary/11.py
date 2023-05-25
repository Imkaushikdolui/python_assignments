# 11. Write a Python program to sort a dictionary by key.

my_dict = {'c': 30, 'a': 10, 'b': 20}

sorted_dict = dict(sorted(my_dict.items()))

print(sorted_dict)
# 16. Write a Python program to find the highest 3 values in a dictionary.

from heapq import nlargest

my_dict = {'a': 10, 'b': 50, 'c': 30, 'd': 40, 'e': 20}

highest_values = nlargest(3, my_dict.values())

print(highest_values)



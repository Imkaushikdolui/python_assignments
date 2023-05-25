# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {'a': 20, 'b': 10, 'c': 5}

ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))

descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Ascending order:", ascending)
print("Descending order:", descending)
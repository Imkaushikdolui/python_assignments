# 7. Write a Python script to merge two Python dictionaries.

dict1 = {'a': 10, 'b': 20}
dict2 = {'c': 30, 'd': 40}

merged_dict = {}
merged_dict.update(dict1)
merged_dict.update(dict2)

print(merged_dict)
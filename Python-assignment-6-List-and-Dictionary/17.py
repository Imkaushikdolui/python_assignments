# 17. Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
dict2 = {'key1': 1, 'key2': 2}

# Match key values in the dictionaries
for key in dict1:
    if key in dict2 and dict1[key] == dict2[key]:
        print(key + ": " + str(dict1[key]) + " is present in both dict1 and dict2")
# 10. Write a Python program to remove a key from a dictionary. 

my_dict = {'a': 10, 'b': 20, 'c': 30}

print(my_dict)
key = input("Enter the key you want to delete ")
del my_dict[key]

print(my_dict)
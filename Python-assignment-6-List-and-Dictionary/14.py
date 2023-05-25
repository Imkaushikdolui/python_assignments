# 14. Write a Python program to check a dictionary is empty or not. 
my_dict = {'a':1,'b':2,'c':3}
empty_dict = {}

if not bool(empty_dict):
    print("Empty dictionary")
else:
    print("Non-empty dictionary")

if not bool(my_dict):
    print("Empty dictionary")
else:
    print("Non-empty dictionary")
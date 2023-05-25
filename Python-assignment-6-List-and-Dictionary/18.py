# 18. Write a Python program to check if all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

list1 = [{}, {}, {}]
list2 = [{1, 2}, {}, {}]

result1 = all(not bool(dict) for dict in list1)
result2 = all(not bool(dict) for dict in list2)

print(result1)  
print(result2)  
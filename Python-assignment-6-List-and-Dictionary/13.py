# 13. Write a Python program to remove duplicates from Dictionary.

test_dict = {'a': 10, 'b': 25, 'c': 20, 'd': 10, 'e': 20}

print("The original dictionary is : " + str(test_dict))

temp = []
res = dict()

for key, val in test_dict.items():
	if val not in temp:
		temp.append(val)
		res[key] = val

print("The dictionary after values removal : " + str(res))

# 4. Write a Python script to check if a given key already exists in a dictionary. 

mydict = {'a': 1, 'b': 2, 'c': 3}
given_key = input('Enter key for dict ')
for key in mydict:
    if given_key in mydict:
        print("key already present in mydict")
        break
    else:
        print("key doesnt exist in mydict")
        break
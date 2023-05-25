# 11. Write a Python function to reverses a string if it's length is a multiple of 4. 

def reverse_string(string):
    if len(string) % 4 == 0:
        return string[::-1]
    else:
        return string

print(reverse_string("ball"))
print(reverse_string("cat"))
print(reverse_string("dog"))
print(reverse_string("cube"))

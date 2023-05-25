# 14. Print multiplication table of 24, 50 and 29 using loop.

tables = [24, 50, 29]

for num in tables:
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
    print()

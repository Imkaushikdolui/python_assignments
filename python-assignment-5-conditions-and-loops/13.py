# 13. Take 10 integers from keyboard using loop and print their average value on the screen.

total = 0
for i in range(10):
    num = int(input("Enter an integer: "))
    total += num

average = total / 10
print("Average:", average)

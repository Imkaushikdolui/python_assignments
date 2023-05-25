# 19. From a list containing ints, strings and floats, make three lists to store them separately

list = [120, 920.5, "apple", 3.0, "", 475]
integers = []
strings = []
floats = []

for item in list:
    if isinstance(item, int):
        integers.append(item)
    elif isinstance(item, str):
        strings.append(item)
    elif isinstance(item, float):
        floats.append(item)

print("Integers:", integers)
print("Strings:", strings)
print("Floats:", floats)

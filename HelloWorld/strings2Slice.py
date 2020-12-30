#         012345678901234
#         432109876543210   Negative indexing
parrot = "Norwegian Blue"
# We can slice an integer by using [startPos:endPos]
print(parrot[0:6])  # 'Norweg' It print's from 0 up to, but no including, index 6.
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])  # If we don't specify the startPos it will take 0 as startPos.
print(parrot[10:14])
print(parrot[10:])  # If we don't specify the endPos it'll rub to the end of the string.

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])
print(parrot[:])  # If we don't specify startPos nor endPos it prints from the beginning to the end of the string

# Slicing can also be negative
print("\nNegative slicing")
print(parrot[-4:-2])    # Bl
print(parrot[-4:12])    # Bl

print(parrot[-14:-8])   # Norweg


# Step in a Slice
print("\nStep in a slice")
# If we add a 3rd parameter to the slicing we can indicate the space between the steps.
print(parrot[0:6:2])    # Nre by stepping 2
print(parrot[0:6:3])    # Nw by stepping 3
number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)
values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

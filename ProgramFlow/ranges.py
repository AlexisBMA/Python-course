age = int(input("How old are you? "))

# The for goes from 1 up to but not including 21
for i in range(10, 16):
    print("i is now {}".format(i))
print("-" * 80)

# If we don't provide a startPos in the range it will be 0 by default
for i in range (10):
    print("i is now {}".format(i))
print("-" * 80)

# We can also provide the steps by adding a third element, in this case its '2'
for i in range(0, 10, 2):
    print("is is now {}".format(i))
print("-" * 80)

# We can also use a negative step
for i in range(10, 0, -2):
    print("is is now {}".format(i))
print("-" * 80)

# Another use of range i to determine if a value is inside that range.
# if 16 <= age <= 65:     # Simplified and condition
#     print("Have a good day at work.")
# else:
#     print("Enjoy your free time")

if age in range(16, 66):
    print("Have a good day at work.")
else:
    print("Enjoy your free time")

#         012345678901234
#         432109876543210   Negative indexing
parrot = "Norwegian Blue"
print(parrot)
# In Python we can print the letter we want in a string by using [] and passing as parameter the index of the letter
# we want.
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

# We can also use negative indexing in strings.
print()
print(parrot[-1])  # This will print the last 'e' from "Norwegian Blue"
print(parrot[-14])

print("\nSame exercise but using negative indexing.")

print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print("\nSame exercise but using subtraction.")

print(parrot[3-14])
print(parrot[4-14])
print(parrot[9-14])
print(parrot[3-14])
print(parrot[6-14])
print(parrot[8-14])
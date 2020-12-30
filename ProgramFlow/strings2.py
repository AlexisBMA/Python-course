# Lint to the built-in functions https://docs.python.org/3/library/functions.html
# Link to the string methods https://docs.python.org/3/library/stdtypes.html#string-methods
number = input("Please enter a series of numbers, using any separators you like: ")
separators = ""
for char in number:
    if not char.isnumeric():  # isnumeric() return True if the char is a number otherwise return false
        separators = separators + char

# print("The separators are: ", separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))

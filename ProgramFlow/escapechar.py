# Backslash changes the meaning of a letter
# \n = start a new line
split_string = "This string has been\nsplit over\nseveral\nlines"
print(split_string)

# \t = add a tabbed space
tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)

print('The pet shop owner said "No, no, \'e\'s uh,... he\'s resting".')
print("The pet shop owner said \"No, no, 'e's uh,... he's resting\".")

# When we are using the triple quotes python knows that the string
# doesn't end, until it finds those matching triple
# quotes
print("""The pet shop owner said "No, no, \
'e's uh,... he's resting". """)

another_split_string = """This string has been \
split over \
several \
lines \
with triple quotes"""

print(another_split_string)
# To include a backslash in a string we have two options
# We can include an r before the opening double quotes
print(r"C:\Users\time\notes.txt")
# We can use double backslash
print("C:\\Users\\time\\notes.txt")
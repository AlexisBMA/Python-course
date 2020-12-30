# Backslash changes the meaning of a letter
# \n = start a new line
splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

# \t = add a tabbed space
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh,... he\'s resting".')
print("The pet shop owner said \"No, no, 'e's uh,... he's resting\".")

# When we are using the triple quotes python knows that the string doesn't end, until it finds those matching triple
# quotes
print("""The pet shop owner said "No, no, \
'e's uh,... he's resting". """)

anotherSplitString = """This string has been \
split over \
several \
lines \
with triple quotes"""

print(anotherSplitString)
# To include a backslash in a string we have two options
# We can include an r before the opening double quotes
print(r"C:\Users\time\notes.txt")
# We can use double backslash
print("C:\\Users\\time\\notes.txt")
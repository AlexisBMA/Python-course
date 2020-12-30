# In here we are unpacking the string inside enumerate
# for index, character in enumerate("abcdefgh"):
#     print(index, character)

# This is the way enumerate works
index, character = (0, 'a')
print(index)
print(character)

# This is assigning a tuple to each element t
for t in enumerate("abcdefgh"):
    # We are unpacking the tuple t in the variables.
    index, character = t
    print(index, character)





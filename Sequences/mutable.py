shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

# Concatenate a new element to a list.
shopping_list += ["cookies"]
print(shopping_list)
# In this case the list is a mutable object so it remains with the same
# id.

print(id(shopping_list))
print(another_list)

# This is called chain assignment. All the new variables refer to the
# same list.
a = b = c = d = e = f = another_list
print(a)
print("Adding cream")
# append() method Help us adding elements to a list
b.append("cream")
print(c)
print(d)

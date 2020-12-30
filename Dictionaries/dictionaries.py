fruit = {"orange": "a sweet, orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         # Every key takes the last value assigned to it.
         }

# Print a specific element from a dictionary by its key
# print(fruit)
# print(fruit["lemon"])

# Add an item to a dictionary
# fruit["pear"] = "an odd shaped apple"
# print(fruit["pear"])

# If we assign a value to a existing key we replace its content
# fruit["Lime"] = "great with tequila"
# print(fruit["Lime"])

# Remove an item from the dictionary. If we doesn't specify the key,
# it delete all the dictionary.
# del fruit["lemon"]
# print(fruit)

# To delete everything inside a dictionary without deleting it
# fruit.clear()

print(fruit)
# while True:
#     dic_key = input("Please enter a fruit: ")
#     if dic_key == "quit":
#         break
#     # The second argument is the default value.
#     # description = fruit.get(dic_key, "We don't have a " + dic_key)
#     # print(description)
#     if dic_key in fruit:
#         # Get an element from a dictionary using .get
#         description = fruit.get(dic_key)
#         print(description)
#     else:
#         print("we don't have a " + dic_key)

# Order a dictionary by creating a copy in a list
# order_keys = list(fruit.keys())
# order_keys.sort()
#
# order_keys = sorted(fruit.keys())

# print("Ordered by key")
# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])
#
# print("\nOrdered by values")
# for f in sorted(fruit.values()):
#     print(f)
# print('-' * 40)

# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)

print(fruit.items())
# Create a tuple from the elements of a dictionary
f_tuple = tuple(fruit.items())
print(f_tuple)
for snack in f_tuple:
    # Unpacking the tuple into two variables
    items, description = snack
    print(items + ' is ' + description)

# Create a dictionary from a tuple
print(dict(f_tuple))

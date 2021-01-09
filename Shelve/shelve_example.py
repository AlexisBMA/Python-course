# It acts as a dictionary but it is stored in a file instead of memory
# In shelves the keys must be strings, values can be any Python type
# All the methods of the dictionaries can be also used with shelves.

import shelve

# With this line the shelve will close automatically
# with shelve.open('ShelfTest') as fruit:
fruit = shelve.open('ShelveTest')
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making soda"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in brunches"
fruit['lime'] = "a sour, green citrus fruit"

# print(fruit["lemon"])
# print(fruit["grape"])
#
# # Assigning a new value to an existing key
# fruit["lime"] = "great with tequila"
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])

# We can avoid errors when trying to retrieve a non-existing key
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#
#     if dict_key in fruit:
#         # We can assign a default value as in dictionaries
#         # description = fruit.get(dict_key, "We don't have a " + dict_key)
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("We don´t have a " + dict_key)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

for v in fruit.values():
    print(v)
print(fruit.values())

for f in fruit.items():
    print(f)
print(fruit.items())

fruit.close()



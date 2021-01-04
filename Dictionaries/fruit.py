fruit = {"orange": "a sweet, orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         # Every key takes the last value assigned to it.
         }

print(fruit)

veg = {"cabbage": "every child's favorite",
       "sprouts": "mmmm, lovely",
       "spinach": "can I have some more fruit, please"}
print(veg)

# Update adds the fruit dictionary to the veg dictionary. It doesn't
# return a new dictionary.

veg.update(fruit)
print(veg)

# If we want a new dictionary to be created we need to use copy()
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print("\nCreating a new dictionary from fruit and updating it with veg")
print(nice_and_nasty)


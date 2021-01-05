# First way to declare a set
farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)
for animal in farm_animals:
    print(animal)

print('-' * 40)

# Second way to declare a set
wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

# Adding element to a set
# Set are unordered.
farm_animals.add("horse")
wild_animals.add("horse")

print(farm_animals)
print(wild_animals)

# To declare a empty set we must use the second declaration form
empty_set = set()
empty_set_2 = {}  # Python understands these line as an empty dict
empty_set.add("a")

even = set(range(0, 40, 2))
print(even)
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)

# Union
print("-" * 40)
print(len(even))
print(squares)
print(len(squares))
print(even.union(squares))
print(len(even.union(squares)))
print(squares.union(even))

# Intersection
print("-" * 40)
print(even.intersection(squares))
print(even & squares)
print(squares.intersection(even))
print(squares & even)

# Subtraction or difference
print("-" * 40)
print("Even: ", sorted(even))
print("Squares: ", sorted(squares))
print("even - squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))
print("squares - even")
print(squares.difference(even))
print(squares - even)

# Subtraction in place (re-assign the variable value)
print("-" * 40)
print("Even before subtraction: ", sorted(even))
print("Squares before subtraction: ", sorted(squares))
even.difference_update(squares)
print("Even after subtraction: ", sorted(even))

# Symmetric difference
even = set(range(0, 40, 2))
print("-"* 40)
print("Symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))
print("Symmetric squares minus even")
print(sorted(squares.symmetric_difference(even)))

# Removing items from a set
print("-" * 40)
squares.discard(4)
squares.remove(16)
squares.discard(8)  # no error, does nothing
print(squares)

try:  # error because it is not in the set so we check
    squares.remove(8)
except KeyError:
    print("The item 8 is not a member of the set")

# Subset and superset
# Subset: if all the members are contained in another set
# Superset: if it contains all the other sets and members of the sets.
print("-" * 40)
even = set(range(0, 40, 2))
squares_tuple = (4, 6, 16)
squares = set(squares_tuple)

if squares.issubset(even):
    print("Squares is a subset of even")

if even.issuperset(squares):
    print("Even is a superset of squares")

# Frozen set (immutable set)
even_frozen = frozenset(range(0, 100, 2))
print(even_frozen)
# even_frozen.add(3)  # Error because is immutable

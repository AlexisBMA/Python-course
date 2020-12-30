# Declaring lists
empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# Creating a list by the concatenation of other two lists
numbers = even + odd
print(numbers)

# Creating a list by sorting another list.
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

# When we create a list with sorted, the list type will be the same type
# as the items in that object.
digits = sorted("432985617")
print(digits)

# We can also create a list by a taking each element of any iterable.
digit_elements = list("432985617")
print(digit_elements)

# This can be helpful in the case we need to copy a list
more_numbers = list(numbers)
print(more_numbers)

# We can use is to check if its the same list
# In this case they have the same elements but the variables are not
# referring to the same space of memory
print(numbers is more_numbers)
# They both contain the same objects
print(numbers == more_numbers)

# There is another way of copying a list, by using slice
more_more_numbers = numbers[:]
print(more_more_numbers)

# There's 12 different ways of copying lists.
# But the more efficient way of copying a list is using the copy method.
the_numbers = numbers.copy()
print(the_numbers)
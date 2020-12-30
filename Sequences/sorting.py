pangram = "The quick brown fox jumps over the lazy dog"

# Sorted return a new list sorted, you can still have the original list
letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5 , 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

# sort() changes the list that we call, sorted() returns a new list.
numbers.sort()
print(numbers)
# If we want to sort case-sensitive strings
missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "marco"
         ]

names.sort()
print(names)
# If we want to sort case-sensitive list
names.sort(key=str.casefold)
print(names)
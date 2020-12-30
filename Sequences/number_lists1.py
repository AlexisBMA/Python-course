empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# A list containing two lists
numbers = [even, odd]
print(numbers)

for number_list in numbers:
    # Print each element of the main list
    print(number_list)
    # Print each value inside the lists contained in the main list
    for value in number_list:
        print(value)

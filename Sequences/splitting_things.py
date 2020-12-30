panagram = """The quick brown
 fox jumps\tover
the lazy dog"""
# We can use split to separate each word in a phrase.
words = panagram.split()
print(words)

# We can determine which character will be the separator
numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
values = "".join(generated_list)
print(values)

values_list = values.split()
print(values_list)

# Solutions

# My solution to the mini-challenge. Create a new list to store int.
int_values_list = []
for element in values_list:
    int_values_list.append(int(element))
print(int_values_list)

# Replace the elements to ints in the same list.
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])
print(values_list)


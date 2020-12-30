data = [104, 101, 4, 105, 208, 103, 5,
        107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

# To avoid problems when deleting elements from a list its better to
# remove the items backwards.
# for index in range(len(data) - 1, - 1, - 1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)
#         del data[index]

# This method its more efficient than the other two

top_index = len(data) - 1  # len(data) = 13
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]

print(data)

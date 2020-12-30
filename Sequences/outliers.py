# Test case 1
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]
# Test case 2
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]
# Test case 3
# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]
# Test case 4
# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]
# Test case 5
# data = [1041, 1051, 1101, 1201, 1301, 1301, 1501,
#         1601, 1701, 1831, 1851, 1871, 1881, 1911]
# Test case 6
data = []
# We can delete an element from a range in a list using del
# del data[0:2]
# print(data)

# This doesn't work because the this have no longer 16 elements
# del data[16:]
# print(data)
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200

# This wouldn't work because each time we are deleting an element of
# a list, the index will remain the same skipping the elements we want
# to delete
# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
# print(data)

# Process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)  # for debugging
del data[:stop]
print(data)

# process the high values in the list
start = 0
for index in range(len(data) - 1, - 1, - 1):
    if data[index] <= max_valid:
        start = index + 1
        break
print(start)
del data[start:]
print(data)

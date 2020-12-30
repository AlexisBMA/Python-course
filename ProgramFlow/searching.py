shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None

# len() help us know how many items are in a sequence
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         # We can add a break statement so when the code found the item it stops searching
#         break

# We can also search an item in a list with 'in' 
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))

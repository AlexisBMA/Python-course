# We can declare a list by using []
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# This block of code produces the same output as if we were using continue
# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

# Continue
# for item in shopping_list:
#     if item == "spam":
#         # Continue means go to the next iteration of the for loop and skip all the remaining code of the block
#         continue
#     print("Buy " + item)

# Break
for item in shopping_list:
    if item == "spam":
        # Break stops the for loop in the iteration that the condition is satisfied
        break
    print("Buy " + item)

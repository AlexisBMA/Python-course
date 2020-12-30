menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# for meal in menu:
#     if "spam" not in meal:
#         print(meal)
#     else:
#         top_index = len(meal) - 1
#         for index, element in enumerate(reversed(meal)):
#             if element == "spam":
#                 del meal[top_index - index]
#         print(meal)

# Professor solution

#                       Solution 1
# for meal in menu:
#     for index in range(len(meal) - 1, - 1, - 1):
#         if meal[index] == "spam":
#             del meal[index]
#     print(meal)

#                       Solution 2
for meal in menu:
    # we can use join with any iterable
    items = ", ".join((item for item in meal if item != "spam"))
    print(items)

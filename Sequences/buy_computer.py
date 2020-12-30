available_parts = ["Computer",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "Mouse mat",
                   "HDMI",
                   "DVD"
                   ]
# More efficient way to get the indexes
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))

print(valid_choices)

current_choice = '-'
computer_parts = []  # Create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # it's already in so remove it
            print("Removing {}".format(current_choice))
            # We can remove a list from a list by using remove()
            # Remove will throw an error if the element to remove
            # doesn't exist on the list
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add options form the list below")
        # enumerate() function returns each item with its index pos.
        # We can use enumerate() with any iterable type
        for number, part in enumerate(available_parts):
            # The index() method returns the index of an object in a
            # list. But there is a more efficient way.
            # print("{0}: {1}".format(available_parts.index(part) + 1, part))
            print("{0}: {1}".format(number + 1, part))
        print("0: Exit")
    current_choice = input()
else:
    print("Bought all the parts!")
    print(computer_parts)

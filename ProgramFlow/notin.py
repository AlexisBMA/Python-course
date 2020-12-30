activity = input("What would you like to do today? ")

# casefold() converts a string into lower case
if "cinema" not in activity.casefold():
    print("But i want to go to the cinema!")
else:
    print("That sounds awesome!!")
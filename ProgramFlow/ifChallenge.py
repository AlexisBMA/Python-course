name = input("What's your name? ")
age = int(input("How old are you, {}? ".format(name)))

if name and age:
    if 18 <= age <= 30:
        print("{}, feel free to enjoy your holiday".format(name))
    else:
        print("{} you aren't allowed to enter...".format(name))
else:
    print("Enter valid inputs")

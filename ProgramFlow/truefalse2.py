
if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name: ")
if name:
    print("Helo, {}".format(name))
else:
    print("Are you a man with no name?")

# By other way
if name != "":
    print("Helo, {}".format(name))
else:
    print("Are you a man with no name?")


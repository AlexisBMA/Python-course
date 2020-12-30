choice = '-'
while choice != "0":
    if choice in "123456789":
        print("You chose {}".format(choice))
    else:
        print("1. Python")
        print("2. Java")
        print("3. C")
        print("4. C++")
        print("5. C#")
        print("6. JavaScript")
        print("7. PHP")
        print("8. R")
        print("0. Exit")
    choice = input()
else:
    print("Bye!")

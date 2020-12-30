print("1. Python")
print("2. Java")
print("3. C")
print("4. C++")
print("5. C#")
print("6. JavaScript")
print("7. PHP")
print("8. R")
print("0. Exit")
option = None

while option != 0:
    option = int(input("Please select an option: "))
    if option == 1:
        print("You selected 1, Python!")
    elif option == 2:
        print("You selected 2, Java!")
    elif option == 3:
        print("You selected 3, C!")
    elif option == 4:
        print("You selected 4, C++!")
    elif option == 5:
        print("You selected 5, C#!")
    elif option == 6:
        print("You selected 1, JavaScript!")
    elif option == 7:
        print("You selected 7, PHP!")
    elif option == 8:
        print("You selected 8, R!")
    elif option == 0:
        continue
    else:
        print("Invalid option")
        continue
else:
    print("Bye!")
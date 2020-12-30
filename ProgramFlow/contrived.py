numbers = [1, 45, 31, 15, 60]

for number in numbers:
    if number % 8 == 0:
        # Reject the list
        print("The numbers are unacceptable")
        break
else:
    # We can use an else statement in a loop. This will be executed if
    # the loop is executed till the end without any interruption.
    print("All those numbers are fine")

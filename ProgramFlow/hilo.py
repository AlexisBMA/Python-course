low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press enter to start")

guesses = 1
while low != high:
    print("\tGuessing in the rage of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guees is {}. Should i guess higher or lower? "
                     "Enter h or l, or c if my guess was correct "
                     .format(guess)).casefold()
    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater that the guess
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the rage becomes one less than the guess
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")

    # guesses = guesses + 1
    # Augmented assignment
    guesses += 1
else:
    print("You thought of the number {}.".format(low))
    print("I got it in {} guesses!".format(guesses))

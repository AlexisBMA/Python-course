# When we want to use objects from the Python Standard Library, we need to import them.
import random


def get_integer(prompt):
    # To write a docstring use triple double quotes (' """ ')
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The String that the user will see, when
        they're prompted to enter the value.
    :return: The Integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print("Enter a valid integer value!")


help(get_integer)

highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing
print("Please guees a number between 1 and {}: ".format(highest))
guess = ""
while guess != answer:
    guess = get_integer(": ")
    if guess == 0:
        print("Game over")
        break
    if guess == answer:
        print("Well done, you guessed it!")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:   # Guess must be greater than answer
            print("Please guess lower")


# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time!")



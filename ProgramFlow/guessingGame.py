# When we want to use objects from the Python Standard Library, we need to import them.
import random
highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing

print("Please guees a number between 1 and {}: ".format(highest))
guess = ""
while guess != answer:
    guess = int(input())
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
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it!")
        # else:
        #     print("Sorry, you have not guessed correctly")


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



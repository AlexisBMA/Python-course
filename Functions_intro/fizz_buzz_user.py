def fizz_buzz(number: int) -> str:
    """
    Prints fuzz if number is divisible by 3, buzz if is divisible by 5
    and fizz buzz if its divisible by both.
    :param number: The number to check
    :return: String fizz, buzz or fizz buzz
    """
    if number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"
    elif number % 3 == 0 and number % 5 != 0:
        return "fizz"
    elif number % 5 == 0 and number % 3 != 0:
        return "buzz"
    else:
        return str(number)


# for i in range(1, 101):
#     correct_answer = fizz_buzz(i)
#     if i % 2 == 0:
#         # print("Please type your answer\n")
#         user_answer = input()
#         if user_answer == correct_answer:
#             print("Congratulations")
#         else:
#             print("Incorrect answer")
#             break
#     else:
#         print("Computer answer: {}".format(correct_answer))

# Professor solution
input("Play Fizz Buzz. Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print("You lose, the correct answer was: {}".format(correct_answer))
        break
else:
    print("Well done, you reached {}".format(next_number))

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


for i in range(1, 101):
    print(fizz_buzz(i))

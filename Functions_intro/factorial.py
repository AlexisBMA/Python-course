def factorial(number: int) -> int:
    """
    Returns the factorial of a number
    :param number: The number from the function will
    get the factorial.
    :return: The factorial of the number.
    """
    answer = 1
    for j in range(number, 0, -1):
        answer = answer * j
    return answer


for i in range(36):
    print(i, factorial(i))

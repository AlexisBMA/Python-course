def sum_numbers (*nums: float) -> float:
    """
    Return the sum of n numbers
    :param nums: The tuple of numbers to sum
    :return: The sum of all the numbers inside the tuple
    """
    answer = 0
    for num in nums:
        answer += num
    return answer


test_numbers = ((1, 2, 3), (8, 20, 2), (12.5, 3.147, 98.1), (1.1, 2.2, 5.5))
for e in range(len(test_numbers)):
    a, b, c = test_numbers[e]
    print(sum_numbers(a, b, c))


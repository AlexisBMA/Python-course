# To create a function we need to use 'def name():'.
# X and Y are parameters of the function multiply
def multiply(x: float, y: float) -> float:
    """
    Multiply 2 numbers.

    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence.  If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.

    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """
    result = x * y
    return result


# # The values inside the parenthesis are called arguments
# answer = multiply(10.5, 4)
# print(answer)
#
# forty_two = multiply(7, 6)
# print(forty_two)
# print()
#
# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)

# Palindromes (we can have more than 1 function in the same file)


def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.

    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1] == string


def palindrome_sentence(sentence: str) -> bool:
    char_string = ""
    for char in sentence:
        if char.isalnum():
            char_string = char_string + char.casefold()
        else:
            continue
    print(char_string)
    return char_string[::-1] == char_string


def palindrome_sentence_prof(sentence):
    """
    Check if a sentence is a palindrome.

    The function ignores whitespace, capitalisation and
    punctuation in the sentence.

    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    return is_palindrome(string)


# word = input("Please enter a word to check: ").casefold()
# if palindrome_sentence_prof(word):
#     print("'{}' is a palindrome!".format(word))
# else:
#     print("'{}' is not a palindrome...".format(word))

# Test cases
# Was it a car, or a cat, I saw?
# Do geese see god?
# Desnes not far, Rafton sensed
# Not a palindrome sentence

answer = multiply(18,3)
print(answer)

p = palindrome_sentence()
# Create a program that takes some text and return a set of all the
# characters in the text that are not vowels sorted in alphabetical
# order.

# You can either enter the text from the keyboard or initialize a string
# variable with the string.

text = input("Type the text:\n").casefold()
print(text)
vowels = frozenset("aeiou")
consonants = set(text).difference(vowels)
if " " in consonants:
    consonants.remove(" ")

print(sorted(consonants))

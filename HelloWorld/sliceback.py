letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1]    # We can use this notation '::-1' to slice backwards.
print(backwards)
qpo = letters[16:13:-1]
print(qpo)

edcba = letters[4::-1]
print(edcba)

lastCharacters = letters[:-9:-1]
print(lastCharacters)

print(letters[-4:])     # When we use a negative startPos and we don't specify the endPos we get the end characters
print(letters[-1:])
print(letters[:1])
print(letters[0])

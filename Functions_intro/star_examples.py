numbers = (0, 1, 2, 3, 4, 5)

# print(numbers, sep=';')
# * before a variable unpack the values from that variable
# We can unpack any sequence
# print(*numbers, sep=';')
# print(0, 1, 2, 3, 4, 5, sep=';')


# using * in the args means that we can pass 0 or more arguments
def test_star(*args):
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)
print()
test_star()

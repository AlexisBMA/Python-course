# Right aligned elements
for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))  # ** is the exponent operator.
    # We also can add a space format, by adding {n:spaceFormat} inside the string
print()

# Left aligned elements '<'
for i in range(1,13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

# Center aligned elements '^'
print()
for i in range(1,13):
    print("No. {0:2} squared is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

# Specifying the number of digits after de decimal point.
print("Pi is approximately {0:12}".format(22/7))    # Specifying the space with 15 decimals
print("Pi is approximately {0:12f}".format(22/7))   # Specifying the space with 6 decimals
print("Pi is approximately {0:12.50f}".format(22/7))    # Specifying the space and the precision
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:<62.50f}".format(22/7))
print("Pi is approximately {0:<72.50f}".format(22/7))
print("Pi is approximately {0:<72.54f}".format(22/7))
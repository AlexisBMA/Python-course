age = 24
# We can concatenate a int with a string by converting it to a string with str(var)
print("My age is: " + str(age) + " years")

# We also can use {n} inside a string and then use .format(variables) where the variables will substitute {n} in
# the respective order of the tuple inside .format
print("My age is: {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dic"))

print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dic".format(31))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28,30,31))
print()

print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28,30,31))
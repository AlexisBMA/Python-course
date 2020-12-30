# The tuples are declared using () or not. They are immutable.
# They are memory cheaper than lists.
# They protect things that shouldn't change.

t = ("a", "b", "c")
print(t)

# Parentheses must be used when you pass a tuple literal as an argument
# to a function. An example could be the print function.
name = "Alex"
age = 21

print((name, age, "Python", 2020))
print(name, age, "Python", 2020)

# Immutable
# metallica[0] = "Master of Puppets"

welcome = ("Welcome to my Nightmare", "Alice Cooper", 1975)
bad = ("Bad Company", "Bad Company", 1974)
budgie = ("Nightflight", "Budgie", 1981)
imelda = ("More Mayhem", "Emilda May", 2011)
metallica = ("Ride the Lightning", "Metallica", 1984)

print(metallica)
# We can use indexing to access individual items in the tuple
print(metallica[0])
print(metallica[1])
print(metallica[2])

metallica2 = list(metallica)
print(metallica2)

metallica2[0] = "Master of Puppets"
print(metallica2)

# welcome = ("Welcome to my Nightmare", "Alice Cooper", 1975)
# bad = ("Bad Company", "Bad Company", 1974)
# budgie = ("Nightflight", "Budgie", 1981)
# imelda = ("More Mayhem", "Emilda May", 2011)
# metallica = ("Ride the Lightning", "Metallica", 1984)
#
# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)
#
# table = ("Coffee table", 200, 100, 75, 34.50)
# print(table[1] * table[2])
#
# name, length, width, height, price = table
# print(length * width)

albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the Lightning", "Metallica", 1984),
]

# We can unpack tuples inside a for loop 
for name, artist, year in albums:
    print("Album: {}, Artist: {}, year: {}"
          .format(name, artist, year))

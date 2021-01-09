import pickle
# When an object is pickled and it's written to a file that contains the
# objects data together with sufficient information to allow that object
# to be recreated, when its loaded back in.

# imelda = ("More Mayhem",
#           "Imelda May",
#           "2011",
#           ((1, "Pulling the Rug"),
#            (2, "Pycho"),
#            (3, "Mayhem"),
#            (4, "Kentish Town Waltz")))
#
# with open("imelda.pickle", "wb") as pickle_file:
#     pickle.dump(imelda, pickle_file)

# with open("imelda.pickle", "rb") as imelda_pickle:
#     imelda2 = pickle.load(imelda_pickle)
# print(imelda2)
# album, artist, year, track_list = imelda2
# print(album)
# print(artist)
# print(year)
#
# for track in track_list:
#     track_number, track_title = track
#     print(track_number, track_title)

# imelda = ("More Mayhem",
#           "Imelda May",
#           "2011",
#           ((1, "Pulling the Rug"),
#            (2, "Pycho"),
#            (3, "Mayhem"),
#            (4, "Kentish Town Waltz")))
#
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
#
#
# with open("imelda.pickle", "wb") as pickle_file:
#     # If we don't specify the protocol python uses the protocol 3 by
#     # default
#     pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
#     pickle.dump(even, pickle_file, protocol=0)
#     pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
#     pickle.dump(2998302, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
#
# with open("imelda.pickle", "rb") as imelda_pickle:
#     imelda2 = pickle.load(imelda_pickle)
#     even_list = pickle.load(imelda_pickle)
#     odd_list = pickle.load(imelda_pickle)
#     x = pickle.load(imelda_pickle)
#
# print(imelda2)
# album, artist, year, track_list = imelda2
# print(album)
# print(artist)
# print(year)
#
# for track in track_list:
#     track_number, track_title = track
#     print(track_number, track_title)
#
# print("=" * 40)
#
# for i in even_list:
#     print(i)
#
#
# print("=" * 40)
#
# for i in odd_list:
#     print(i)
#
# print("=" * 40)
#
# print(x)


# Code to remove a file.
print("=" * 40)
pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")

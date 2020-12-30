# Importing a list from another file. When we import something from
# another file, Python executes all the code in that file.
from nested_data import albums

# To declare a constant we need to name it in uppercase
SONGS_LISTS_INDEX = 3
SONG_TITLE_INDEX = 1
while True:
    print("Please choose yor album (invalid choice exits).")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_lists = albums[choice - 1][SONGS_LISTS_INDEX]
    else:
        break
    print("Please chose your song: ")
    for index, (track_number, song) in enumerate(songs_lists):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_lists):
        title = songs_lists[song_choice - 1][SONG_TITLE_INDEX]
    else:
        continue
    print("Playing: {}".format(title))
    print("=" * 50)

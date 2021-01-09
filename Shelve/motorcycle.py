import shelve
with shelve.open("bike2") as bike:
    # bike["make"] = "Honda"
    # bike["model"] = "250 dream"
    # bike["color"] = "red"
    # bike["engine_size"] = 250

    # Deleting an entry
    # del bike["engin_size"]

    # Like in dictionaries we can iterate through the keys
    for key in bike:
        print(key)

    print("=" * 40)
    print(bike["engine_size"])
    # print(bike["engin_size"])
    print(bike["color"])







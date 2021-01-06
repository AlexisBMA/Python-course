#
# with open("challenge.txt", "w") as challenge_file:
#     for i in range(1, 13):
#         number = 12 * i
#         print(str(i) + " times 2 is " + str(number), file=challenge_file)

with open("sample.txt", "a") as tables:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2}".format(i, j, i * j), file=tables)
        print("-" * 20, file=tables)

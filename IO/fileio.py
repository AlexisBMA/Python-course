# Reading a file using open and close.
# jabber = open("./sample.txt", 'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         # end prevents print from printing a new line.
#         print(line, end='')
#
# jabber.close()

# Reading a file using with (it closes the file automatically)
# with open("./sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("./sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         # readLine() reads the file line by line
#         line = jabber.readline()

# with open("./sample.txt", 'r') as jabber:
#     # readLines() reads the entire file in one go
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')

with open("./sample.txt", 'r') as jabber:
    # readLines() reads the entire file in one go
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')

with open("./sample.txt", 'r') as jabber:
    # readLines() reads the entire file in one go
    lines = jabber.read()
print(lines)

for line in lines[::-1]:
    print(line, end='')

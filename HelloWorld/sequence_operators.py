string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords."
print(string1 + string2 + string3 + string4 + string5)
print("he's " "probably " "pining " "for the " "fjords.")
print("Hello " * 5)  # The star multiplication symbol repeats a sequence the times we want.

print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

# We can check if a string is a substring of another by using 'in'
today = "friday"
print("day" in today)   # True
print("fri" in today)   # True
print("thu" in today)   # False
print("parrot" in "fjord")  # False

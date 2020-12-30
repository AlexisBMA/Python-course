flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sun flower",
    "Tiger Lily",
    # 42  if one element in the list has a different type than string
    # it crashes.
]

# Join all items in a tuple into a string, using a any character
# as separator. But all the items in the tuple must be strings
# separator = " | "
separator = ", "
output = separator.join(flowers)
print(output)
print(" | ".join(flowers))

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# We bind two lists by using the extend method
even.extend(odd)
print(even)
another_even = even
print(another_even)

# We can sort a list by using sort() method
print("Sorted list")
even.sort()
print(even)

# We can sort in reverse order
print("Reverse sorted list")
even.sort(reverse=True)
print(even)
print(another_even)

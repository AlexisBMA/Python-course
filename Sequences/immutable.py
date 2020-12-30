result = True
another_result = result
# The id() function returns the identity of an object.
print(id(result))
print(id(another_result))
# When we change the value attached to result the id changes.
# This means that a the variable is immutable.
result = False
print(id(result))

results = "Correct"
another_results = results
print(id(results))
print(id(another_results))

results += '!'
print(id(results))
print(id(another_results))
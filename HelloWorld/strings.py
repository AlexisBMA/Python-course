print("Today is a good day to learn Python")
print('Pythons is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
# If you start a string with single quotes you must finish it with the same type, this leave you to use double quotes
# inside single quote string or vice versa.
print("Hello" + " world")  # This is called concatenation
greeting = "Hello"

# We can assign a value to a variable with the input function
name = input("Please enter your name: ")
print(greeting + name)

# If you want a space, we can add that too
print(greeting + ' ' + name)
age = 24
print(age)

# We can know the type of a variable using the type() method and passing as parameter the variable
print(type(greeting))
print(type(age))
# We can change the type of a variable by just assigning the new values to store. This is called rebound the label of
# a variable. So we can see a variable as a name or label that is bound to a value.
age_in_words = "2 years"
print(name + f" is {age} years old") # If we add an f before the doble quotes we can use {var}
print(type(age))

print(f"Pi is approximately {22/7:12.50f}")
pi = 22/7
print(f"Pi is approximately {pi:12.50f}")
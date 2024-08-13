programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    # "Loop": "The action of doing the same thing multiple times"
}

# print(programming_dictionary)

# print(programming_dictionary["Bug"])
# print(programming_dictionary["Bog"]) # KeyError: 'Bog'
# print(programming_dictionary[Function) # SyntaxError: closing parenthesis ')' does not match opening parenthesis '['

# Add a new entery:
programming_dictionary["Loop"] = "The action of doing the same thing multiple times"

# print(programming_dictionary)

emtpy_dictionary = {}

# Wipe Existing Dictionary:
# programming_dictionary = {}
# print(programming_dictionary)

# Edit item in dictionary:
programming_dictionary["Bug"] = "A Poblem inside your code"
print(programming_dictionary)

# Loop throught dictionary:
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

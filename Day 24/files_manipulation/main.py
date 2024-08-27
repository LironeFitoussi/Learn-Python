# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close() # Always close the file after reading or writing to it

# Better way to open a file and close it automatically
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Writing to a file
# modes:
# "r" - read: read only (default)
# "w" - write: overwrites the file,
# "a" - append: adds to the end of the file
with open("my_file.txt", mode="a") as file:
    file.write("New text.")
    file.write("\n")
    file.write("New line.")

# Creating a new file when it doesn't exist
with open("new_file.txt", mode="w") as file:
    file.write("New file created.")

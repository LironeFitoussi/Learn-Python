# List Comprehension
# With List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = [n + 1 for n in numbers]
print(new_list)

# With String
name = "Lirone"
letters_list = [letter for letter in name]

# With Range
range_list = [n * 2 for n in range(1, 5)]

# With Conditional
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

# Upper Case
upper_names = [name.upper() for name in names if len(name) > 5]

# Squared Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)

# Even Numbers
list_of_strings = ["9", "0", "32", "8", "2", "8", "64", "29", "42", "99"]
numbers = [int(n) for n in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)


# Numbers Challenge
def read_nums(file_input):
    with open(file_input, mode="r") as file:
        return [int(line.strip()) for line in file.readlines()]


file1_data = read_nums("file1.txt")
file2_data = read_nums("file2.txt")

result = [num for num in file1_data if num in file2_data]

print(result)

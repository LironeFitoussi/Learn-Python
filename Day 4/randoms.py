import random

# Generate a random int number between 1 and 10, e.g. 3 or 7 or 10.
random_integer = random.randint(1, 10)
print(random_integer)

# Generate a random number between 0 and 1, e.g. 0.0000000001 or 0.9999999999.
random_float = random.random()
print(random_float)

# Generate a random uniform number between 1 and 10, e.g. 2.71828182846 or 9.51234.
random_float = random.uniform(1, 10)
print(random_float)


love_score = random.randint(1, 100)
print(f"Ypur love score is {love_score}")

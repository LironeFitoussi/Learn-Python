# Functions with more than one parameter
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Lirone", "Netanya")

# Using keyword arguments
greet_with(location="Tel Aviv", name="Lirone")
# The order of the keyword arguments does not matter

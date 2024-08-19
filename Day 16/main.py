# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)

# # Change Shape
# timmy.shape("turtle")

# # Change Color
# timmy.color("coral")

# # Move Forward
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# print(" | Pokemon Name | Type | HP | Attack | Defense | Special Attack | Special Defense | Speed |")

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_column("HP", [35, 44, 39])
table.add_column("Attack", [55, 48, 52])

# print(table.align)
# Align the table to the left
# table.align = "l"
print(table)

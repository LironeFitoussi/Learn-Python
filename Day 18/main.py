# import turtle
# tim = turtle.Turtle

# from turtle import Turtle
# tim = Turtle()

# from turtle import *

# forward(100)  # Possible but, this is not recommended


# Alias
# import turtle as t

# tim = t.Turtle()  # Alias for turtle.Turtle()

import heroes  # Third-party module, if not installed, this will throw an error

print(heroes.gen())  # Generate a random hero name
print(heroes.gen())  # Generate a another random hero name

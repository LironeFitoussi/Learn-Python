import random
from turtle import Turtle, Screen

arrow = Turtle()
arrow.shape("arrow")
arrow.width(10)
arrow.speed(10)
colors = [
    "red",
    "green",
    "blue",
    "purple",
    "orange",
    "yellow",
    "black",
    "brown",
    "pink",
    "cyan",
]


directions = [0, 90, 180, 270]
sides = ["left", "right"]


def draw_line():
    arrow.color(random.choice(colors))
    arrow.forward(30)
    next_direction = random.choice(directions)
    arrow.setheading(next_direction)

    # arrow[random.choice(sides)](random.choice(directions))


for _ in range(50):
    draw_line()

screen = Screen()
screen.exitonclick()

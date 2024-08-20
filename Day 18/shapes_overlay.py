from turtle import Turtle, Screen
import math

timmy_the_turtle = Turtle()

count = 4

colors = [
    "red",
    "green",
    "blue",
    "yellow",
    "purple",
    "orange",
    "black",
    "pink",
    "brown",
    "cyan",
]


def draw_a_shape(count):
    timmy_the_turtle.color(colors[count - 4])
    sides = math.floor(round(360 / count))
    # print(sides)
    for _ in range(count):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(sides)


while count < 10:
    draw_a_shape(count)
    count += 1

# Prevent the window from closing
screen = Screen()
screen.exitonclick()

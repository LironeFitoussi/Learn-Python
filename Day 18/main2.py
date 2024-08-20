from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")  # Change the shape of the turtle
# timmy_the_turtle.color("red")  # Change the color of the turtle
# timmy_the_turtle.forward(100)  # Move the turtle forward by 100 units
# timmy_the_turtle.right(80)  # Turn the turtle right by 90 degrees
# timmy_the_turtle.forward(100)  # Move the turtle forward by 100 units


def draw_a_square():
    for _ in range(4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)


# draw_a_square()


def draw_a_shape(corners):

    sides = int(round(360 / corners))
    # print(sides)
    for _ in range(corners):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(sides)


# draw_a_shape(17)

# Prevent the window from closing
screen = Screen()
screen.exitonclick()

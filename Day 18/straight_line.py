from turtle import Turtle, Screen

timmy_the_turtle = Turtle()


def draw_a_dash_line(length):
    for _ in range(length):
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pendown()


draw_a_dash_line(15)
screen = Screen()
screen.exitonclick()

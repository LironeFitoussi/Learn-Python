import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Etch-A-Sketch")
screen.bgcolor("white")

# Set up the turtle
etch_turtle = turtle.Turtle()
etch_turtle.shape("turtle")
etch_turtle.speed(5)


# Movement functions
def move_forward():
    etch_turtle.forward(10)


def move_backward():
    etch_turtle.backward(10)


def turn_left():
    etch_turtle.left(15)


def turn_right():
    etch_turtle.right(15)


def clear_screen():
    etch_turtle.clear()
    etch_turtle.penup()
    etch_turtle.home()
    etch_turtle.pendown()


# Keyboard bindings
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")

# Main loop
screen.mainloop()
screen.exitonclick()

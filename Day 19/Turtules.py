from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_game_on = False
user_bet = screen.textinput(
    "Make Your Bet", "Which turtle will win the race? Enter a color: "
)
# print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle_index in range(6):
    new_turtule = Turtle(shape="turtle")
    new_turtule.color(colors[turtle_index])
    new_turtule.penup()
    new_turtule.goto(-230, -100 + turtle_index * 40)
    all_turtles.append(new_turtule)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
screen.exitonclick()

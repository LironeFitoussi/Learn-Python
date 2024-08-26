from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from turtle import Screen

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Game speed
game_speed = 0.1

# Scoreboard setup
scoreboard = Scoreboard()

# Ball setup
ball = Ball()

# Paddle setup
paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))

# Screen update
screen.update()

# Keyboard controls
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")
screen.listen()


def game_loop():
    global game_speed
    ball.move()

    # Ball collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Ball collision with paddles
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320:
        ball.setx(320)
        ball.bounce_x()

    if ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.setx(-320)
        ball.bounce_x()

    # Ball out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    screen.update()
    screen.ontimer(game_loop, int(game_speed * 1000))


screen.ontimer(game_loop, int(game_speed * 1000))
screen.exitonclick()

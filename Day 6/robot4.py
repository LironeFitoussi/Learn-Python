def turn_right():
    turn_left()
    turn_left()
    turn_left()

def go_around():
    turn_left()
    move()
    while wall_on_right():
        move()
    else:
        turn_right()
        move()
        turn_right()
        move()
        while front_is_clear():
            move()
        turn_left()
    
while not at_goal():
    if wall_in_front():
        go_around()
    elif front_is_clear():
        move()

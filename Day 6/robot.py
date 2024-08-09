def turn_right():
    turn_left()
    turn_left()
    turn_left()

def go_around():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for i in range(6):
    go_around()
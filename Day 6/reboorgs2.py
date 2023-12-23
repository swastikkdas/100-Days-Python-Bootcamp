#using while loop
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

no_of_hurdles =6
while no_of_hurdles > 0:
    jump()
    no_of_hurdles -= 1
    print(no_of_hurdles)
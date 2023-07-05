#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


# Task # 1

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    turn_left()
    turn_left()
    
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
turn_around()


# Task # 2

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def lap():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_jumps = 6
while number_of_jumps > 0:
    lap()
    number_of_jumps -= 1

    
# Task # 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def lap():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() == False:
    lap()


# Task # 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal() == False:
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()


# Task # 5

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()
        
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()


# Final Task

def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

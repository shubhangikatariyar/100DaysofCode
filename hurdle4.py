# Question: https://reeborg.cs20.ca/?lang=en&mode=python&menu=%2Fworlds%2Fmenus%2Fsk_menu.json&name=Hurdle%204&url=%2Fworlds%2Ftutorial_en%2Fhurdle4.json

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
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()



    
    
    




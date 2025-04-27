import random
print("ROCK PAPER SCISSOR GAME!")
print("What do you choose? \n")

user_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
print(f"User Chose {user_choice}" )

if user_choice == 0 or user_choice == 1 or user_choice ==2:
    computer_choice = random.randint(0,2)
    print(f"Computer Chose {computer_choice}" )
    # ROCK > Scissor  ---> NO PAPER
    # Scissor > Paper  ---> NO ROCK
    # Paper > Rock  ---> NO SCISSOR

    selected = [computer_choice, user_choice]
    if user_choice == computer_choice:
        print("DRAW")
    elif 0 not in selected:
        if user_choice > computer_choice: # Paper(1) > Rock(0)
            print("YOU WIN!")
        else:
            print("YOU LOSE!")
    elif 1 not in selected:
        if user_choice < computer_choice: # Rock(0) < Scissors (2)
            print("YOU WIN!")
        else:
            print("YOU LOSE!")
    else:
        if user_choice > computer_choice:  # paper (1) >  Rock (0)
            print("YOU WIN!")
        else:
            print("YOU LOSE!")

else:
    print("Invalid Choice! Please try again.")
    
# #OUTPUT:
# ROCK PAPER SCISSOR GAME!
# What do you choose? 

# Type 0 for Rock, 1 for Paper or 2 for Scissors
# 2
# User Chose 2
# Computer Chose 0
# YOU LOSE!
    
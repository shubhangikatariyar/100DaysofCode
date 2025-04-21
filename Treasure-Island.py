print("Welcome to Treasure Island. \nYour mission is to find the treasure.")
way= input("Type your choice, do you want to go left or right? \n").lower()
swim= input("Type your choice, do you want to go to swim or wait? \n").lower()
door= input("Type your choice, do you want to enter Red or Blue or Yellow door? \n").lower()


if way == 'left' or swim == 'wait' or door == 'yellow':
    print("Congratulations, you WIN!!")

else:
    print("Sorry, GAME OVER! please try again!")

# #OUTPUT:
# Welcome to Treasure Island.
# Your mission is to find the treasure.
# Type your choice, do you want to go left or right?
# left
# Type your choice, do you want to go to swim or wait? 
# wait
# Type your choice, do you want to enter Red or Blue or Yellow door? 
# yellow
# Congratulations, you WIN!!
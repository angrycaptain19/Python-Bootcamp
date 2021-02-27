# Project
# Tresure Hunt


print("Welcome")
direction = input("Enter The Direction 'Right' or 'Left' : ")
if direction == "Left":
    work = input("Enter the Work 'Swim' or 'Wait': ")
    if work == "Wait":
        door_color = input("Enter the Door Color 'Red', 'Blue' or 'Yellow' : ")
        if door_color == "Red":
            print("Burned by fire. Game Over")
        elif door_color == "Blue":
            print("Eaten by beasts. Game Over")
        elif door_color == "Yellow":
            print("You Win")
        else:
            print("Game Over")
    else:
        print("Attacked by trout. Game Over")
else:
    print("Fall into Hole. Game over")

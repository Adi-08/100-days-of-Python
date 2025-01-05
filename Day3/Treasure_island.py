
import random
print(''' 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/___/____
*******************************************************************************
''')




print("Welcome to Treasure Island. Your mission is to find the treasure.")

direction = input("Choose the direction which side you want to go? left (L) or right (R): ")

if direction == "L":
    temp = input("You want to swim or wait? S or W: ")
    if temp == "S":
        # Randomize the outcome of swimming
        if random.choice([True, False]):  # 50% chance
            print("You swam safely across!")
            door = input("Which door you want: Red (R), Yellow (Y), Blue (B): ")
        else:
            print("Attacked by trout. Game Over.")
    elif temp == "W":
        # Add a random event during waiting
        print("While waiting, you hear strange noises... but you're safe!")
        door = input("Which door you want: Red (R), Yellow (Y), Blue (B): ")
    else:
        print("Invalid choice. Game Over.")
        
    if temp == "W" or (temp == "S" and random.choice([True, False])):
        # Randomize the correct door
        winning_door = random.choice(["R", "Y", "B"])
        if door == winning_door:
            print("You Win !!!")
        elif door == "R":
            print("Burned by fire. Game Over.")
        elif door == "Y":
            print("Game Over. No treasure here.")
        elif door == "B":
            print("Eaten by beasts. Game Over!")
        else:
            print("Invalid choice. Game Over.")
else:
    print("Fall into a hole. Game Over!!")








'''
print("Welcome to Treasure Island.Your mission is to find the treasure.")

direction = input("Choose the direction which side you want to go? left (L) or right(R): ")

if direction == "L":
    temp = input("You want to swim or wait? S or W: ")
    if temp == "S":
        print("Attacked by trout.Game Over.")
    elif temp == "W":
        door = input("Which door you want Red (R), Yellow (Y), Blue (B): ")
        if door == "R":
            print('Burned by fire.Game Over.')
        elif door == "Y":
            print("You Win !!!")
        elif door == "B":
            print("Eaten by beasts. Game Over! ")
        else:
            print("Game Over!")
else:
    print("Fall into a hole Game Over!!")
'''

#Final Project
print()
print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("Welcome to Treasure Island!\nYour Mission is to find the Treasure - THE ONE PIECE")
dir = input("You are at a Crossover. Choose a side to Start the journey(Left or Right): ").lower()
if dir == "left":
    print("You choose the correct side so you are safe! Luck is on your side.")
    island = input("There is an Island in the middle of the Lake. Choose to Wait for a boat or Swim: ").lower()
    if island == "wait":
        print("Please wait for sometime..")
        print("Your boat has arrived!\nAfter Travelling in the lake for sometime...\nYou have arrived at the destination.")
        print("There is a Castle and it has 3 doors in it.")
        door = input("Choose a door to continue the journey(Red, Yellow or Blue): ").lower()
        if door == "yellow":
            print("Congrats you have found the ONE PIECE!!!!! The Treasure searched by all but found by none untill now.")
        elif door == "blue":
            print("You have entered the Dungeon full of Monsters...GAME OVER!!!.")
        elif door == "red":
            print("You have entered the room full of fire...GAME OVER!!!.")
        else:
            print("You have chosen a door that doesn't exit... GAME OVER!!!")
    else:
        print("The lake is full of Crocodiles... GAME OVER!!!")
else:
    print("You fall in a pit... GAME OVER!!!")        

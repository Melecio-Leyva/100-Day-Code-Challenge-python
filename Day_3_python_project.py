#ASCII Art for different ascii templates
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
#Greet the user
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
player = input("You are at a crossroad, do you go left or right?").lower()
if player =="left":
    player = input("You find a sleeping dragon do you fight it? 'Y' or ' N'").lower()
    if player =="n":
        player = input("You ran, smart choice. you stumble upon a cave do you enter? 'Y' or 'N'?")
        if player =="Y":
            player = input("You found a wizard, he offers you a gift do you accept it? 'Y' or 'N'? ").lower()
            if player =="Y":
                print("the wizard spares your life and teleports you away with 10 wold bars Congrats!!@!")
            else:
                print("the wizard is turns you into a youth elixir for rejecting his gift offer. you Lose!")
        else:
            print("You Died")
    else:
        print("you died")
else:
     print("You Died")
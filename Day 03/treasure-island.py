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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

direction = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if direction == "left":
    swim_wait = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if swim_wait == "wait":
        door = input('You see the hut? It has 3 doors! Which door will you choose to opn?\nType "red" for Red door, "blue" for Blue door and "yellow" for Yellow door. Plz note that any random word will be consider as Game Over.').lower()
        if door == 'red':
            print("There was a fire and you burned!\nGame Over!")
        elif door == 'blue':
            print("There was a BEAST! You got eaten by it!\nGame Over!")
        elif door == "yellow":
            print("FINALLY FINALLY FINALLY! YOU ARRIVED AT THE DESTINATION!\n YOU WON!")
        else:
            print("You lost at the last stage! Sadly.\nGame Over!")
    else:
        print("Oh no! You attcked by TROUT!\nGame Over!")
else:
    print("You fell into the hole.\nGame Over.")
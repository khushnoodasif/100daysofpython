print('''
************************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|____________
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|________________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|____________
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|________________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|____________
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|________________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/______/___
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/______/
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/______/___
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/______/
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/______/___
/______/______/______/______/______/______/______/______/______/______/______/______/
*************************************************************************************
  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  ,adPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8 a8P_____88  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88         8PP"""""""  
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88         "8b,   ,aa  
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          `"Ybbd8"' 
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure. \n")

direction1 = input("Which way do you want to go? (left or right) \n").lower()

if direction1 == "left":
  direction2 = input("Do you want to swim or wait? \n").lower()
  if direction2 == "wait":
    direction3 = input("Which door? (blue, red or yellow) \n").lower()
    if direction3 == "blue" or direction3 == "red":
      print("Game Over!") 
    else:
      print("You Win!")
  else:
    print("Game Over!")
else:
  print("Game Over!")

#EDIT GAME LATER!

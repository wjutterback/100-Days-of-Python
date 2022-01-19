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
first_fork = input('You enter a cave only visible at low-tide. There are two paths, which do you take, left or right? ').lower()

if first_fork == 'left':
  second_fork = input('You find yourself in a room with a large pond with a building in the middle. To your left you notice there is a red door, but it is covered in impassable spikes. What do you do, swim or wait? ').lower()
  if second_fork == 'wait':
    third_fork = input('The spikes covering the door retract. Two more colored doors materialize out of the cave wall beside it: blue and yellow. Which door will you pick: red, blue, or yellow? ').lower()
    if third_fork == 'yellow':
      print('You win!')
    elif third_fork == 'red':
      print('You are burned by fire. Game over')
    elif third_fork == 'blue':
      print('You are eaten by beasts. Game over.')
    else:
      print('A wizard comes out of nowhere and punts you to oblivion. Game over.')
  else:
    print('You attempt to swim to the building in the middle of the lake, but you are attacked by pirhanas. Game over.')
else:
  print('You fall into a hole. Game over.')
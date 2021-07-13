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
question_1= input("You are at a crossed road, where do you want to go left or right? Type 'left' or 'right' \n").lower()
if question_1 == "right":
  print ("You fell into a hole, Game Over.")
elif question_1 == "left" :
  #the game continues
  question_2 = input("Do you want to swim across the river or wait for a boat ride? \n").lower()
  if question_2 == "swim" :
    print ("You got attacked by a trout. Game Over.")
  elif question_2 == "wait" :
    #the game continues
    question_3 = input("you have arrived at your destinaion and you're not too far from the TRESURE, which door do you want to enter GOLD, SLIVER or COPPER? \n").lower()  
    if question_3 == "gold":
      print ("Burned by fire, Game Over.")
    elif question_3 == "sliver" :
      print ("Eaten by beasts, Game Over.")
    elif question_3 == "copper" :
      print ("Just because there's a tarnish on the coppper, doesn't mean there's not a shine beneath,cogratulations!!!!\nYou Win.")
  else:
    print ("Error")
else :
  print ("Error")  
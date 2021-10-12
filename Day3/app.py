#################################
# Day 3 Project - Treasure Island
#################################

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
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
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

print("***************************")
print("Welcome to Treasure Island!")
print("***************************")

print("Your mission is to find the treasure.")
cross_road_answer = str(input("""You're at a cross road. Where do you want to go? Type "left" or "right"\n""")).lower()

if cross_road_answer == "left":
	lake_answer = str(input("""You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n""")).lower()
	if lake_answer == "wait":
		house_color = str(input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")).lower()
		if house_color == "red":
			print("It's a room full of fire. Game Over.")
		elif house_color == "yellow":
			print("You found the treasure! You win!!")
		elif house_color == "blue":
			print("You entered a room full of beasts. Game Over.")
		else:
			print("You chose a door that doesn't exist. Game Over.")
	else:
		print("You got attacked by an angry trout. Game Over.")
else:
	print("You fell into a hole. Game Over.")

		


#######################################
# Day 4 Project - Rock, Paper, Scissors
#######################################

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def rps():

	player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
	computer_choice = random.randint(0,2)

	if player_choice == 0:
		print("Player chose:")
		print(rock)
	elif player_choice == 1:
		print("Player chose:")
		print(paper)
	elif player_choice == 2:
		print("Player chose:")
		print(scissors)
	else:
		print("Please choose a number between 0 and 2")

	if computer_choice == 0:
		print("Computer chose:")
		print(rock)
	elif computer_choice == 1:
		print("Computer chose:")
		print(paper)
	else:
		print("Computer chose:")
		print(scissors)

	# Game Results
	if player_choice == 0 and computer_choice == 1:
		print("You lose...")
	elif player_choice == 0 and computer_choice == 2:
		print("You win!")
	elif player_choice == 1 and computer_choice == 0:
		print("You win!")
	elif player_choice == 1 and computer_choice == 2:
		print("You lose...")
	elif player_choice == 2 and computer_choice == 0:
		print("You lose...")
	elif player_choice == 2 and computer_choice == 1:
		print("You win!")
	else:
		print("Its a tie.")

rps()

play_again = str(input("Play again? Enter 'y' or 'n'\n")).lower()
while play_again == "y":
	rps()
	play_again = str(input("Play again? Enter 'y' or 'n'\n")).lower()

print("Thanks for playing!")












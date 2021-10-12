import random
import hangman_art
import hangman_words

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
word_length = range(len(chosen_word))

lives = 6

# print(chosen_word)

display = []

for i in word_length:
	display.append("_")

end_of_game = False

while not end_of_game:
	guess = str(input("Guess a letter:\n")).lower()


	if guess in display:
		print(f"You've already guessed {guess}")

	for position in word_length:
		letter = chosen_word[position]
		if letter == guess:
			display[position] = letter

	if guess not in chosen_word:
		print(f"You guessed {guess}, that's not in the word. You lose a life.")
		lives -=1
		if lives == 0:
			end_of_game = True
			print("You lose...")
			print(f"The word was {chosen_word}")

	print(f"{' '.join(display)}")

	if "_" not in display:
		end_of_game = True
		print("You win!")

	print(hangman_art.stages[lives])

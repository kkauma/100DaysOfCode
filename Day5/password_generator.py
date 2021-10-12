####################################
# Day 5 Project - Password Generator
####################################

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

password = ""

for letter in range(num_letters):
	random_letter = random.choice(letters)
	password += random_letter

for number in range(num_numbers):
	random_number = random.choice(numbers)
	password += random_number

for symbol in range(num_symbols):
	random_symbol = random.choice(symbols)
	password += random_symbol


random_password = "".join(random.sample(password, len(password)))

print(f"Here is your random password: {random_password}")
# print(f"Here is your password: {password}")

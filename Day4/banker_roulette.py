from random import randint

names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
rand_num = randint(0, len(names) - 1)

print(f"{names[rand_num]} is going to buy the meal today!")


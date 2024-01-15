print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

true_string = "true"
love_string = "love"
true_score = 0
love_score = 0


for letter in name1:
    if letter in true_string:
        true_score += 1

for letter in name2:
    if letter in true_string:
        true_score += 1

for letter in name1:
    if letter in love_string:
        love_score += 1

for letter in name2:
    if letter in love_string:
        love_score += 1

total_score = int(str(true_score) + str(love_score))

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score > 40 and total_score < 50:
    print(f"Your score is {total_score}, you are alright together")
else:
    print(f"Your score is {total_score}")

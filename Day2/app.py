################################
# Day 2 Project - Tip Calculator
################################

print("******************************")
print("Welcome to the tip calculator!")
print("******************************\n")

total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
people_split = int(input("How many people to split the bill? "))

total_pay = (total_bill * (1 + tip)) / people_split

print(f"Each person should pay: ${total_pay:.2f}")


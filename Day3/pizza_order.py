# Pizza order program
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
total_bill = 0

if size == "S":
    total_bill += 15
elif size == "M":
    total_bill += 20
else:
    total_bill += 25

if add_pepperoni == "Y":
    if size == "S":
        total_bill += 2
    else:
        total_bill += 3

if extra_cheese == "Y":
    total_bill += 1


print(f"Your final bill is: ${total_bill}.")
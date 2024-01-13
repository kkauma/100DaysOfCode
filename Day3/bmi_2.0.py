# Enter your height in meters
height = float(input("Enter your height in meters: "))
# Enter your weight in kilograms
weight = int(input("Enter your weight in kilos: "))

BMI = round((weight / (height ** 2)), 1)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
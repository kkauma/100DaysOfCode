# Enter height in meters
height = float(input("Enter your height in meters: "))

# Enter weigth in kilos
weight = int(input("Enter your weight in kilos: "))
             
# BMI
BMI = weight / (height ** 2)
print(f"Your BMI is {round(BMI, 1)}")          
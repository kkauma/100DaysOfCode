# Enter which year to check
year = int(input("Enter a year: "))
leap_year = True

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
        else:
            leap_year = False
    else:
        leap_year = True
else:
    leap_year = False

if leap_year:
    print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year :(")



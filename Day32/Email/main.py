# Sending email using Python
import smtplib
import datetime as dt

my_email = "cometfunds@gmail.com"
password ="HelloWorld19"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="jupytercapital@yahoo.com",
                        msg="Subject:Hello, world!\n\nThanks for your investment, "
                            "welcome to the fund!")

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
if year == 2021:
    print("Invest in ETH!")
# print(type(year))
# print(day_of_week)

date_of_birth = dt.datetime(year=1995, month=4, day=1)
print(date_of_birth)


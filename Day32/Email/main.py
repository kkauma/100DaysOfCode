# Sending email using Python
import smtplib

my_email = "cometfunds@gmail.com"
password ="HelloWorld19"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="jupytercapital@yahoo.com",
                    msg="Subject:Hello, world!\n\nThanks for your investment, "
                        "welcome to the fund!")
connection.close()

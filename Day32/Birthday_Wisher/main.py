# Birthday Wisher Project

import smtplib
import pandas
from datetime import datetime

today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}




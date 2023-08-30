"""
Complete weekday_of_birth_date which takes a date object of a birthday and returns the corresponding weekday string.
For example Bob and Julian's birthdays return Saturday and Monday 
(that's why Bob is meant to relax and Julian to do all the work chuckle).
For this Bite you want to look at the datetime and calendar modules. Have fun!
"""
# we use the .strfttime("%A") method on birthday object to format the datetime object
# %A stands for full weekday name.

from datetime import datetime

def weekday_of_birth_date(date):
    birthday = datetime.strptime(date, "%Y-%m-%d")
    return birthday.strftime("%A")

date_input = input("Enter birthday (YYYY-MM-DD): ")
print(weekday_of_birth_date(date_input))
"""
In this Bite you are provided with a list of publish dates of all our PyBites blog posts. 
They are in this format: Thu, 04 May 2017 20:46:00 +0200.

Write a function called convert_to_datetime that takes a date string and convert it to a datetime object. 
You can leave the timezone part (e.g. +0200) off.

Secondly complete the get_month_most_posts function: 
it should take a list of datetime objects and return the month that we posted the most. You should get 2017-01.
"""

from collections import Counter
from datetime import datetime

def convert_to_datetime(date_string):
    return datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S %z')

def get_month_most_posts(dates):
    month_counter = Counter(date.month for date in dates)
    most_common_month = month_counter.most_common(1)[0][0]
    return datetime(year=2017, month=most_common_month, day=1).strftime('%Y-%m')

dates = [
    "Thu, 04 May 2017 20:46:00 +0200",
    "Fri, 14 Apr 2017 06:23:00 +0200",
    "Tue, 25 Jul 2017 22:27:00 +0200",
    # Add more dates as needed
]

datetime_objects = [convert_to_datetime(date_str) for date_str in dates]
print(get_month_most_posts(datetime_objects))


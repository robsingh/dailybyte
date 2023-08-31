"""
Get to know pytz! pytz brings the Olson tz database into Python (docs). 
Let's see how many hours Bob and Julian have to bridge in order to deliver you PyBites. 
It differs depending on whether it's Winter or Summer in their relative hemispheres.

Complete the what_time_lives_pybites function which receives a naive / not timezone aware datetime object:

There are two kinds of date and time objects: naive and aware: an aware object has sufficient knowledge of applicable algorithmic 
and political time adjustments, such as time zone and daylight saving time information, to locate itself relative to other aware objects. 
An aware object is used to represent a specific moment in time that is not open to interpretation. - docs
First convert the passed in naive_utc_dt to a aware datetime, then convert it to AUSTRALIA and SPAIN localized datetimes returning them in a tuple. 

Have fun and keep coding in Python!
"""

import pytz
from datetime import datetime, timedelta

def what_time_lives_pybites(naive_utc_dt):
    # convert naive_utc_dt to an aware datetime in UTC
    utc_dt = pytz.utc.localize(naive_utc_dt)

    # convert to Australia/Sydney timezone
    australia_tz = pytz.timezone('Australia/Sydney')
    australia_dt = utc_dt.astimezone(australia_tz)

    # convert to Madrid/Europe timezone
    spain_tz = pytz.timezone('Europe/Madrid')
    spain_dt = utc_dt.astimezone(spain_tz)

    return australia_dt, spain_dt


naive_datetime = datetime(2023, 8, 21, 0, 0, 0)
aus_time, spain_time = what_time_lives_pybites(naive_datetime)

print("Australia Time: ", aus_time)
print("Spain Time: ", spain_time)

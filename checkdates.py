"""
This Bite involves solving two problems using datetime:

We kicked off our 100 Days of Code project on March 30th, 2017. Calculate what date we finished the full 100 days!
PyBites was founded on the 19th of December 2016. We're attending our first PyCon together on May 8th, 2018. 
Can you calculate how many days from PyBites' inception to our first PyCon meet up?
"""

from datetime import datetime,timedelta

start_date = datetime(2017,3,30)
end_date = start_date + timedelta(days=100)

print("End date of 100 days of Code: ",end_date)

pybites_inception = datetime(2016,12,19)
first_pycon = datetime(2018,5,8)

days_difference = (first_pycon - pybites_inception).days
print("Days from Pybites inception to first Pycon: ", days_difference)
"""
Write a generator that returns every 100th day counting forward from the PYBITES_BORN date.
"""
from datetime import datetime, timedelta
# from gendates import gen_special_pybites_dates


PYBITES_BORN = datetime(year=2016, month=12, day=19)

def gen_special_pybites_dates():
    day = PYBITES_BORN
    end_date = PYBITES_BORN + timedelta(days=365*1) #stop after one year
    while day <= end_date:
        yield day
        day += timedelta(days=100)

for date in gen_special_pybites_dates():
    print(date)
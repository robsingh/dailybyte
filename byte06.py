"""
Write a simple Promo class. Its constructor receives two variables: name (which must be a string)
and expires (which must be a datetime object).

Add a property called expired which returns a boolean value indicating whether the promo has 
expired or not.

"""
from datetime import datetime

class Promo:
    def __init__(self,name:str, expires):
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        return datetime.now() > self.expires
    

promo1 = Promo("Summer Sale", datetime(2023, 8, 31))
promo2 = Promo("Back to School", datetime(2023, 9, 15))


print(f"{promo1.name} has expired: {promo1.expired}")
print(f"{promo2.name} has expired: {promo2.expired}")




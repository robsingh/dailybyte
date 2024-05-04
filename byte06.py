"""
Write a simple Promo class. Its constructor receives two variables: name (which must be a string)
and expires (which must be a datetime object).

Add a property called expired which returns a boolean value indicating whether the promo has 
expired or not.

"""
import datetime

class Promo:
    def __init__(self,name:str, expires:datetime.datetime):
        self.name = name
        self.expires = expires

    @property
    def expired(self) -> bool:
        return datetime.datetime.now() > self.expires
    

promo1 = Promo("Summer Sale", datetime.datetime(2023, 8, 31))
promo2 = Promo("Back to School", datetime.datetime(2023, 9, 15))


print(f"{promo1.name} has expired: {promo1.expired}")
print(f"{promo2.name} has expired: {promo2.expired}")




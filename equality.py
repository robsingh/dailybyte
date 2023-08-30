"""
In this Bite we compare two list objects for equality, a fundamental thing to understand in Python.

Complete the check_equality function returning the various Enum values (representing equality scores) 
according to the type of equality of the lists:

return SAME_REFERENCE if both lists reference the same object,
return SAME_ORDERED if they have the same content and order,
return SAME_UNORDERED if they have the same content unordered,
return SAME_UNORDERED_DEDUPED if they have the same unordered content and reduced to unique items,
and finally return NO_EQUALITY if none of the previous cases match.
Note that == and is are not the same in Python!

Have fun and keep calm and code in Python!
"""
from enum import Enum

class Equality(Enum):
    SAME_REFERENCE = 1
    SAME_ORDERED = 2
    SAME_UNORDERED = 3
    SAME_UNORDERED_DEDUPED = 4
    NO_EQUALITY = 5


def check_equality(list1, list2):
    if list1 is list2:
        return Equality.SAME_REFERENCE
    
    if list1 == list2:
        return Equality.SAME_ORDERED
    
    if set(list1) == set(list2):
        return Equality.SAME_UNORDERED
    
    if set(list1) == set(list2) and len(list1) == len(list(set(list1))):
        return Equality.SAME_UNORDERED_DEDUPED
    
    return Equality.NO_EQUALITY


list1 = [1,2,3]
list2 = [1,2,3]
list3 = [3,2,1]
list4 = [1,1,2,3]
list5 = [1,2,2,3]

print(check_equality(list1, list2))
print(check_equality(list1, list3))
print(check_equality(list1, list4))
print(check_equality(list1, list5))
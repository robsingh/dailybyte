"""
In this Bite you are presented with 3 dictionaries. 
Complete get_person_age that takes a name as argument and returns the age if in any of the 3 dictionaries. 
The lookup should be case insensitive, so tim, Tim and tiM should all yield 30. If not in any of the dictionaries, return Not found.

Note that some persons are in 2 of the 3 dictionaries. 
In that case return the age of the last dictionaries (so group3 takes precedence over group2 and group2 takes precedence over group1). 
"""


def get_age_for_dict(name, dict):
  lowercase_name = name.lower()
  
  for key in dict:
    if key.lower() == lowercase_name:
      return dict[key]
      
  return None


def get_person_age(name):

  group1 = {"John": 25, "Jane": 28, "Tim": 30}
  group2 = {"Tom": 22, "Alice": 26, "Tim": 35} 
  group3 = {"Bob": 32, "Tim": 40, "Eve": 29}

  age = get_age_for_dict(name, group3)
  if age is not None:
    return age

  age = get_age_for_dict(name, group2)
  if age is not None:
    return age

  age = get_age_for_dict(name, group1)
  if age is not None:
    return age

  return 'Not found'


print(get_person_age(name='John'))
print(get_person_age(name='Rob'))
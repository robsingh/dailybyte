"""
You want to find people who have as much exposure to different cultures as yourself.

Complete the uncommon_cities helper that takes the cities you have visited (my_cities) and the cities the other person has visited (other_cities) 
and returns the number of cities that both sequences do NOT have in common.

So given [A B C] and [B C D] it should return 2 because only A and D are different.

You can loop through both sequences but maybe there is a more concise way to do it?


"""

def uncommon_cities(my_cities, other_cities):
    """
    Return the number(count) of cities that both lists DO NOT have in common.
    """
    city_count = 0

    for city in my_cities:
        if city not in other_cities:
            city_count += 1
    
    for city in other_cities :
        if city not in my_cities:
            city_count += 1


    return city_count


my_cities = ['Haridwar', 'Shimla', 'Delhi', 'Jaipur', 'Chandigarh', 'Jalandhar', 'Pathankot']
other_cities = ['Varanasi', 'Ujjain', 'Agra', 'Kashmir', 'Manipur', 'Hyderabad']

print(uncommon_cities(my_cities, other_cities))
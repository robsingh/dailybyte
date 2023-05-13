"""
Given an array of integers, find if the array contains duplicates. 
The function must return True if any value appears at least twice in 
the array, and must return False if every element is distinct.
"""
from collections import Counter
def check_dups(arr) -> bool:
    """
    Args:
        arr: input array in which duplicates will be checked
    Return:
        bool: True, if a value appears at least twice, otherwise returns False
    """
    check_count = Counter(arr)
    for key,value in check_count.items():
        if value >= 2:
            return True
    return False

    """One-line solution O(n)"""
    # return len(set(arr)) != len(arr)

    """Using a dictionary"""
    # check_dict = {}
    # for num in arr:
    #     if num in check_dict:
    #         return True
    #     else:
    #         check_dict[num] = 1
    # return False

    """Sorting"""
    # arr.sort()
    # for i in range(1, len(arr)):
    #     if arr[i] == arr[i-1]:
    #         return True
    # return False





arr = [1,2,2,3,4,4]
print(check_dups(arr))
'''
Given an array of integers, nums, and an integer, k, return the least number of unique numbers left in nums after removing k elements.
Note: At least one integer will exist in nums and k will always be between zero and nums.length.

Ex: Given the following nums and k…
nums = [1, 4, 3, 3], k = 2, return 1 (remove 1 and 4 and only one unique integer is left which is 3).
'''

from collections import Counter

def least_unique(nums, k):
    # edge case
    if not nums:
        return f"Check the array and try again!"
    
    # check the frequencies
    frequency = Counter(nums)

    # sort numbers by ascending frequency
    sorted_frequency = sorted(frequency.items(), key=lambda x:x[1])

    for num,count in sorted_frequency:
        if k >= count: # can remove all occurrences of this number
            k -= count
            del frequency[num]  # remove elements from the dictionary, always prefer to decrement/increment first and remove the elements from data structure otherwise we can encounter some errors.
        else:
            break  # no more elements can be removed
    
    return len(frequency)


nums = [1,4,3,3]
k = 2
print(least_unique(nums, k))
'''
Given an integer array, nums, and a value, k, return the total number of contiguous subarrays that are divisible by k.

Ex: Given the following nums and k

nums = [1, 3, 1, 2, 5], k = 7, return 2 ([1, 3, 1, 2] and [2, 5] both sum to 7)
'''
'''
Steps:
1. prefix sum: to track the running sum of the array.
2. For each prefix sum, calculate the modulo. If the same modulo has occurred before, then there exists a subarray whose sum is divisible by k.
3. Use hash map to stoe the frequency of each remainder when dividing the prefix sum by 'k'.
'''
from typing import List
from collections import defaultdict

def div_subarrays(nums: List, k:int):
    remainder_count = defaultdict(int)
    remainder_count[0] = 1 # to account for subarrays that are divisible by k from start
    prefix_sum = 0
    count = 0

    for num in nums:
        prefix_sum += num
        remainder = prefix_sum % k

        # handling negative remainder to avoid negative modulo results
        if remainder < 0:
            remainder += k

        # if remainder has appeared before, it means there are subarrays divisible by k
        count += remainder_count[remainder]

        # update the frequency
        remainder_count[remainder] += 1

        print(remainder)
        print(remainder_count)
    
    return count


nums = [1,3,1,2,5]
k = 7
print(div_subarrays(nums, k))
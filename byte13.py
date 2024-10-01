'''
Given an integer array, nums, return whether or not the array was originally sorted in non-decreasing order and 
then rotated some number of positions.

Example Input: nums = [4, 5, 1, 2, 3], 
Output: True (values 4 and 5 were rotated to the beginning of the array).

Example Input: nums = [4, 5, 1, 2, 3, 6]
Output: False

My thought process:
last element must be less than or equal to the first element
There should be at most one place where a larger number is followed by a smaller one (this indicates the rotation point)
'''

def check_rotated(nums):
    n = len(nums)
    drop_count = 0

    for i in range(n):
        if nums[i] > nums[(i+1) % n]:
            drop_count += 1

        if drop_count > 1:
            return False

    return True


nums = [4,5,1,2,3,6]
print(check_rotated(nums))


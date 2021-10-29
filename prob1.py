"""
Given an array of integers, find if the array contains duplicates. 
The function must return True if any value appears at least twice in 
the array, and must return False if every element is distinct.
"""

"""Brute Force approach O(N^2)"""



class Solution:
    def check_Duplicate(self,num):
        for i in range(len(num)):
            for j in range(0,i):
                if num[i] == num[j]:
                    return True
        return False


check = Solution()
print(check.check_Duplicate([0,0]))



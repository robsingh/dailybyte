"""
Given an array of integers, find if the array contains duplicates. 
The function must return True if any value appears at least twice in 
the array, and must return False if every element is distinct.
"""
# from typing import List
"""Brute Force approach O(N^2)"""

# class Final:
#     def check_duplicates(self,num):
#         for i in range(len(num)):
#             for j in range(0,i):
#                 if num[i] == num[j]:
#                     return True
#         return False


# check = Final()
# print(check.check_duplicates([1,2,3,3]))

"""Sorting Approach"""




# class Final:
#     def check_duplicates(self,num: List[int]) -> bool:
#         num.sort()
#         for i in range(1,len(num)):
#             if num[i] == num[i-1]:
#                 return True
#         return False

"""Hash Set Approach"""

# class Final:
#     def check_duplicates(self,num):
#         data = set()
#         for i in num:
#             if i in data:
#                 return True
#             data.add(i)
#         return False

# check = Final()
# # print(check.check_duplicates([1,2,3,4]))
# print(check.check_duplicates([1,2,3,3,]))
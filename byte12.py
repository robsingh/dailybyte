'''
Given an integer array, salaries, salaries[i] represents the salary of the ith employee. 
Return the average employee salary not considering the largest or the smallest salary.

Ex: Given the following salaries…

salaries = [5000, 2000, 3000, 4000], 
return 3500.00000 ((3000 + 4000) / 2).
'''
from typing import List

def avg_salary(salaries:List):
    if len(salaries) <= 2:
        return 0.0 #cannot compute the average for 2 or fewer salaries
    
    max_salary = max(salaries)
    min_salary = min(salaries)

    filtered_salaries = [salary for salary in salaries if salary != max_salary and salary != min_salary]
    
    # if all salaries are same, filtered_salaries end up being empty
    if not filtered_salaries:
        return 0.0
    
    average_salary = sum(filtered_salaries) / len(filtered_salaries)
    return average_salary


salaries = [5000,2000,3000,4000]
print(avg_salary(salaries))
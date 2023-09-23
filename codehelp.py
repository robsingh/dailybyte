""" 
Someone had asked this question on Stack Overflow. 

Define a function named screw_time(num_screws, screws_per_hour) that takes in the number of screws “John” needs to screw in, 
and the number of screws “John” can screw in per hour. 

The function will print out a sentence stating the time required for “John” to complete the task in minutes using the format: 
Time required for John to complete the task(in minutes): xxx” The function will also return the time(in minutes) it takes “John” 
to complete the task as a float. I can assume num_screws is always a multiple of ten but,for every ten screws one will take twice as 
long to screw in relative to the “normal” amount of time it takes to screw in a screw.

Example: Screw_time(10,60)prints”Time required for John to complete the task(in minutes): 11.0” and returns 11.0
"""


def screw_time(num_screws, screws_per_hour):
    normal_time_per_screw = 60 / screws_per_hour # time in minuttes for one screw
    total_time = (num_screws // 10) * (normal_time_per_screw * 3) + (num_screws % 10) * normal_time_per_screw # total time in minutes

    print(f"Time required for John to complete the task(in minutes): {total_time}")
    return total_time


time_required = screw_time(10,60)
print(time_required)
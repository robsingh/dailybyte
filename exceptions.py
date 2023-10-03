"""
In this Bite you'll learn to catch and raise Python exceptions.

Write a simple division function meeting the following requirements:

1. When the denominator is zero, catch the corresponding exception and return zero.

2. When the numerator or denominator have an invalid type reraise the corresponding exception.

3. If the result of the division is negative raise a ValueError.

Check the tests if you have questions about what your code needs to pass. Have fun!

"""

def division(num,denom):
    try:
        if not isinstance(num, (int,float)) or not isinstance(denom, (int,float)):
            raise TypeError("Numerator and Denominator must be of type int or float")
        if denom == 0:
            return 0        
        
        result = num / denom
        
        if result < 0:
            raise ValueError("Result is negative")
        return result
    
    except (TypeError, ZeroDivisionError, ValueError) as e:
        raise e




num = 12
denom = 0

try:
    result = division(num, denom)
    print(f"Result: {result}")
except Exception as e:
    print(f"Error: {e}")
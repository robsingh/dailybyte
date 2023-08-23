"""
Fizz buzz is a group word game for children to teach them about division. 
Players take turns to count incrementally, replacing any number divisible by three with the word "fizz", 
and any number divisible by five with the word "buzz".
...
For example, a typical round of fizz buzz would start as follows:
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, 
Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz, ..
Complete the fizzbuzz function below, it should take a number and return the right str or int.

"""

def fizzbuzz(number) -> str or int:
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number
    

number = 30
print(fizzbuzz(number))
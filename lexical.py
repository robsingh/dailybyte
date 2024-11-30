'''
Given an integer, N, return all values between 1 and N (inclusive) in lexicographical order.
Note: N will not exceed one million. (10,000,00)
Ex: Given the following N
N = 11, return [1, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9]
'''

'''
How we treat the values is very important here. In a question, we always should thrive to find what's obvious but not mentioned in the problem statement.
Here, the output varies if we consider input as numbers or strings, but since lexicographical order is mentioned, it is obvious that we need to consider the input as strings.
Because that's how the values are in dictionary.
'''
def lexical_order(N:int):
    # generate all numbers from 1 to n as strings
    numbers = [str(i) for i in range(1,N+1)]
    
    # sort the number lexicographically
    numbers.sort()

    # convert them back to integers
    return list(map(int, numbers))

N = 20
print(lexical_order(N))
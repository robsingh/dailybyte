'''
You are given N dice, where each die has max faces (with values one through max), and an integer, target. 
Return the total number of ways you can roll the N dice such that the sum of all their face-up values equals the given target.

Ex: Given the following, N, max, and target…

N = 1, max = 6, target = 5, return 1 (there is only one way to roll the single die to sum to 5 i.e. roll a 5).
Ex: Given the following, N, max, and target…

N = 2, max = 6, target = 4, return 3.
-> 3+1 = 4
-> 1+3 = 4
-> 2+2 = 4
'''
#Dynamic Programming
def dice_roll(N:int, max:int, target:int) -> int:
    MOD = 10**9 + 7
    dp = [0] * (target+1)
    dp[0] = 1 # base case

    for i in range(1, N+1):
        new_dp = [0] * (target+1)
        for j in range(1, target+1): # for each possible target sum
            for k in range(1, max+1): # for each face value
                if j-k >= 0:
                    new_dp[j] = (new_dp[j] + dp[j-k]) % MOD
        dp = new_dp #move to the next dice count

    return dp[target]

N = 1
max = 6
target = 5
print(dice_roll(N, max, target))
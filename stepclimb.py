"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45

"""


def climbStairs(n):
    if (n == 1) or (n == 2) or (n == 3):
        return n
    dp = [1, 2, 3]
    for i in range(3, n):
        dp.append(dp[i - 1] + dp[i - 2])

    return dp[n - 1]


print(climbStairs(4))
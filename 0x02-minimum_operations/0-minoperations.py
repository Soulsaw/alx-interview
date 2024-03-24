#!/usr/bin/python3
"""Doc module"""


def minOperations(n: int) -> int:
    """This function compute the minimum operation"""
    if n == 1 | n <= 0:
        return 0
    dp = [0] * (n + 1)
    dp[1] = 1  # The default H character
    for i in range(2, n + 1):
        dp[i] = i
        for j in range(2, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))
    return dp[n]

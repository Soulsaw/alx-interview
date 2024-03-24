#!/usr/bin/python3
"""Doc module"""


def minOperations(n):
    """This function compute the minimum operation"""
    if n <= 0 | n == float('inf'):
        return 0

    dp = [float('inf')] * (n + 1)

    dp[1] = 0  # The default H character

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))
    return dp[n] if dp[n] != float('inf') else 0

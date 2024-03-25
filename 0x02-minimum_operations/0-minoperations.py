#!/usr/bin/python3
"""Doc module"""


def minOperations(n):
    """This function compute the minimum operation"""
    if n <= 0:
        return 0

    dp = {1: 0}
    for i in range(2, n + 1):
        dp[i] = float('inf')
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))
    return dp[n] if dp[n] != float('inf') else 0

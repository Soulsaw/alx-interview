#!/usr/bin/python3
"""This module handle the making change challenge"""


def makeChange(coins, total):
    """If total is 0 or less, return 0 otherwise handle"""
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1

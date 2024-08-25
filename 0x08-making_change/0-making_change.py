#!/usr/bin/python3

def makeChange(coins, total):
    # If total is 0 or less, return 0
    if total <= 0:
        return 0

    # Initialize dp array with infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Process each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, return -1
    return dp[total] if dp[total] != float('inf') else -1

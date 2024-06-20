#!/usr/bin/python3

def makeChange(coins, total):
    # If the total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    # Initialize an array for storing the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins are needed to make a total of 0
    dp[0] = 0

    # Iterate through each coin and update the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the total cannot be met by any combination of the coins, return -1
    return dp[total] if dp[total] != float('inf') else -1

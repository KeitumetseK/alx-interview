#!/usr/bin/python3

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of available coin denominations.
        total (int): The total amount to reach.

    Returns:
        int: Fewest number of coins needed, or -1 if it's not possible.
    """
    def makeChange(coins, total):
        if total <= 0:
            return 0
    
    # Create a DP array to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # If the value at dp[total] is infinity, it means it's not possible to form that total
    return dp[total] if dp[total] != float('inf') else -1

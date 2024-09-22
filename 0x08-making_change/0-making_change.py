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
    if total <= 0:
        return 0
    
    # Initialize DP array with a large number (greater than total)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed to make total of 0
    
    # Fill the DP array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still inf, it's not possible to make the total
    return dp[total] if dp[total] != float('inf') else -1


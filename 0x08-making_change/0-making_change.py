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
    # If the total is 0 or less, return 0 (no coins are needed)
    if total <= 0:
        return 0

    # Initialize the dp array with a large number representing unreachable states
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: No coins are needed to form a total of 0

    # Iterate through each coin and update dp
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means we can't form the total with the given coins
    return dp[total] if dp[total] != float('inf') else -1


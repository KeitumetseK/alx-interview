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
    # Edge case: if total is 0 or less, return 0 (no coins needed)
    if total <= 0:
        return 0

    # Sort coins in descending order to attempt larger denominations first (greedy-like)
    coins.sort(reverse=True)

    # Initialize DP array to infinity, representing an unattainable total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins are needed to make a total of 0

    # Iterate through each coin denomination
    for coin in coins:
        # Update dp for every value from the coin to the total
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):  # Only update if a valid solution exists for dp[i - coin]
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be made with the given coins
    return dp[total] if dp[total] != float('inf') else -1


#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Create dp array initialized to a large value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed for 0 total

    # Fill dp array using the coin denominations
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1

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

    # Sort coins in descending order
    coins.sort(reverse=True)
    num_coins = 0
    remaining_amount = total

    for coin in coins:
        if remaining_amount == 0:
            break
        if coin <= remaining_amount:
            num_coins += remaining_amount // coin
            remaining_amount %= coin

    return num_coins if remaining_amount == 0 else -1


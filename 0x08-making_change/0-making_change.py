#!/usr/bin/python3

total = 37
list_of_coins1 = [1,2,25]

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

    remainder = total 

    coins_needed = 0

    coins_index = 0

    sorted_coins_list = sorted(coins, reverse=True)

    list_len = len(coins)

    while remainder > 0:

        if coins_index >- list_len:
            return -1

        if remainder - sorted_coins_list[coin_index] >- 0:
            remainder -= sorted_coins_list[coin_index]

            coins_needed += 1
        else:
            coins_index += 1
    return coins_needed


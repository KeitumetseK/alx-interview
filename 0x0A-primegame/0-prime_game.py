#!/usr/bin/python3
def isWinner(x, nums):
    """
    Determines the winner of the game after x rounds.

    Args:
        x (int): Number of rounds.
        nums (List[int]): List of numbers for each round.

    Returns:
        str or None: The name of the player with the most wins, "Maria" or "Ben".
                     Returns None if the winner cannot be determined.
    """
    if x < 1 or not nums:
        return None

    # Find the maximum number in the rounds
    max_num = max(nums)

    # Create a list to mark primes using the Sieve of Eratosthenes
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    # Precompute the number of primes less than or equal to any given n
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    # Maria wins if the number of primes in the round is odd, Ben wins if it's even
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


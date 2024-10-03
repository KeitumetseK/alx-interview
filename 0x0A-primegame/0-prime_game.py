#!/usr/bin/python3

def sieve_of_eratosthenes(limit):
    """ Return a list of prime numbers up to the given limit using the Sieve of Eratosthenes """
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for multiple in range(i*i, limit + 1, i):
                sieve[multiple] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def isWinner(x, nums):
    """ Determine the winner of the prime game after x rounds """
    if x < 1 or not nums:
        return None
    
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    # Precompute number of prime removals possible for each n up to max_n
    prime_count = [0] * (max_n + 1)
    for i in range(2, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if i in primes else 0)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        # If prime count up to n is odd, Maria wins; if even, Ben wins
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


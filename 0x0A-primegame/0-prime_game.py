#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """ Implements the Sieve of Eratosthenes to find all primes up to n """
    prime = [True] * (n + 1)
    prime[0], prime[1] = False, False  # 0 and 1 are not prime numbers
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime

def count_primes_up_to_n(prime, n):
    """ Count the number of primes less than or equal to n """
    return sum(1 for i in range(2, n + 1) if prime[i])

def isWinner(x, nums):
    """ Determines the winner of the prime game """
    if x < 1 or not nums:
        return None

    max_n = max(nums)  # Find the maximum n to optimize sieve range
    prime = sieve_of_eratosthenes(max_n)  # Generate primes up to the maximum n
    
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes_up_to_n(prime, n)
        if prime_count % 2 == 1:
            maria_wins += 1  # Maria wins if the count of primes is odd
        else:
            ben_wins += 1  # Ben wins if the count of primes is even

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
if __name__ == "__main__":
    x = 5
    nums = [2, 5, 1, 4, 3]
    print("Winner: {}".format(isWinner(x, nums)))


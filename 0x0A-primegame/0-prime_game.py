#!/usr/bin/python3

def isWinner(x, nums):
    # Initialize a list to keep track of whether numbers are prime
    max_n = max(nums)
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # Sieve of Eratosthenes to find all primes up to max_n
    for p in range(2, int(max_n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, max_n + 1, p):
                is_prime[multiple] = False

    # Dictionary to hold the count of wins for each player
    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        if n < 2:
            wins["Ben"] += 1  # If n < 2, Maria can't pick any prime; Ben wins
            continue

        # Count the number of primes less than or equal to n
        prime_count = sum(1 for i in range(n + 1) if is_prime[i])

        # If the number of primes is odd, Maria wins; if even, Ben wins
        if prime_count % 2 == 1:
            wins["Maria"] += 1
        else:
            wins["Ben"] += 1

    # Determine the overall winner
    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"
    else:
        return None

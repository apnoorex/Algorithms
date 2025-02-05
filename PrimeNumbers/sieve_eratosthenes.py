def sieve_eratosthenes(num):
    """ 
    Sieve of Eratosthenes - an algorithm for finding all
    prime numbers up to any given limit.

    Complexity: O(n*log(log(n))).
    """
    is_prime = [True for _ in range(num + 1)]
    
    p = 2
    while (p * p <= num):
        if is_prime[p]:
            for i in range(p * p, num + 1, p):
                is_prime[i] = False
        p += 1
    
    return [p for p in range(2, num + 1) if is_prime[p]]


# Testing
print(sieve_eratosthenes(30))

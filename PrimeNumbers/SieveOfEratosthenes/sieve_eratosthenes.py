def sieve_eratosthenes(num):
    """ 
    Sieve of Eratosthenes - an algorithm for finding all
    prime numbers up to any given limit.
    
    Complexity: O(n*log(log(n))).
    """
    prime = [True for _ in range(num + 1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    
    return [p for p in range(2, num + 1) if prime[p]]


# Testing
print(sieve_eratosthenes(30))

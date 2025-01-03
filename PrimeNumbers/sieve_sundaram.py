def sieve_sundaram(num):
    """ 
    Sieve of Sundaram - an algorithm for finding all
    prime numbers up to any given limit.

    Complexity: O(n*log(n)).
    """
    num = int((num - 1) / 2)
    marked = [True for _ in range(num + 1)]

    for i in range(1, num + 1):
        j = i
        while (i + j + 2 * i * j <= num):
            marked[i + j + 2 * i * j] = False
            j += 1

    return [2] + [(2 * p + 1) for p in range(1, num + 1) if marked[p]]

# Testing
print(sieve_sundaram(30))

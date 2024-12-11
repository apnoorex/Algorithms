def radix_sort(seq):
    """ 
    Radix sort for positive integers.

    Complexity: O(n*d), where:
    n - number of elements
    d - number of digits in the largest number
    """
    n_digits = len(str(max(seq)))

    for digit in range(0, n_digits):
        # Create empty buckets
        buckets = [[] for _ in range(10)]

        # Distribute the numbers to the buckets
        for item in seq:
            bucket_idx = item // 10 ** (digit) % 10
            buckets[bucket_idx].append(item)

        # Flatten the list of buckets
        seq = [x for xs in buckets for x in xs]
    
    return seq


# Testing
x = [15, 6, 867, 521, 311, 19, 890, 98, 5, 0]
print(radix_sort(x))

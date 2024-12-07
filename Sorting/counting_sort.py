def counting_sort(sequence):
    """
    Counting sort for positive integers.
    Complexity: O(n + k), where:
    n - number of elements
    k - range of input sequence
    """
    max_value = max(sequence)
    count_array = [0] * (max_value + 1)
    output_array = [0] * len(sequence)

    for num in sequence:
        count_array[num] += 1

    # Add previous counts
    for idx in range(1, max_value + 1):
        count_array[idx] += count_array[idx - 1]

    for idx in range(len(sequence) - 1, -1, -1):
        output_array[count_array[sequence[idx]] - 1] = sequence[idx]
        count_array[sequence[idx]] -= 1

    return output_array

# Testing
x = [4, 3, 15, 91, 4, 5, 3, 7, 0, 2, 3]
print(counting_sort(x))
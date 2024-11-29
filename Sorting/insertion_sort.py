def insertion_sort(seq):
    """ Insertion sort. Complexity: O(n^2)."""
    for idx in range(1, len(seq)):
        item_to_insert = seq[idx]

        while item_to_insert < seq[idx-1] and idx > 0:
            seq[idx], seq[idx-1] = seq[idx-1], seq[idx]
            idx -= 1

    return seq


# Testing
x = [1, 5, 7, 0, 9, 0, 6]
print(insertion_sort(x))

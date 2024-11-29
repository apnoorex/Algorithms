def bubble_sort(seq):
    """ Bubble sort. Complexity: O(n^2). """
    sorted = False

    while not sorted:
        sorted = True

        for idx in range(len(seq) - 1):
            if seq[idx] > seq[idx+1]:
                seq[idx], seq[idx+1] = seq[idx+1], seq[idx]
                sorted = False
    return seq


# Testing
x = [1, 4, 3, 2, 1, 67, 8, 0, 5]
print(bubble_sort(x))

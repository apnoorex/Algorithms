def quick_sort(seq):
    """ Quick sort. Complexity: O(n log n). """
    if len(seq) <= 1:
        return seq

    pivot = seq.pop()

    items_lower, items_greater = [], []

    for item in seq:
        if item < pivot:
            items_lower.append(item)
        else:
            items_greater.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


# Testing
x = [1, 6, 4, 2, 7, 9, 0, 99]
print(quick_sort(x))

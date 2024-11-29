def linear_search(sequence, item):
    """ 
    Linear search algorithm.
    The sequence has to be sorted first. 
    Complexity: O(n)
    """
    for idx in range(len(sequence)):
        if item == sequence[idx]:
            return idx
        
    return -1


# Testing
x = [1, 2, 3, 4, 5, 7, 90]
print(linear_search(x, 7))

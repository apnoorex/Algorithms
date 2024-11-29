def binary_search(sequence, item):
    """ 
    Binary search algorithm. Iterative implementation.
    The sequence has to be sorted first. 
    Complexity: O(log n)
    """
    start_index = 0
    end_index = len(sequence) - 1

    while start_index <= end_index:
        midpoint = start_index + (end_index - start_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint
        
        elif midpoint_value > item:
            end_index = midpoint - 1

        else:
            start_index = midpoint + 1

    return None


# Testing
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(a, 9))

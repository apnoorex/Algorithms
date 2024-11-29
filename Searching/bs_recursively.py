def binary_search(sequence, start_index, end_index, item):
    """ 
    Binary search algorithm. Recursive implementation.
    The sequence has to be sorted first. 
    Complexity: O(log n)
    """
    if start_index <= end_index:
        midpoint = (start_index + end_index) // 2

        if sequence[midpoint] == item:
            return midpoint
        
        elif item < sequence[midpoint]:
            return binary_search(sequence, start_index, midpoint-1, item)
        
        else:
            return binary_search(sequence, midpoint+1, end_index, item)
        
    else:
        return None
    

# Testing
x = [1, 4, 6, 8, 9, 45, 67, 88, 99]
print(binary_search(x, 0, len(x), 67))

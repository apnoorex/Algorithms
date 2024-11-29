def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    
def siftDown(lst, i, end_index):
    while True:
        left, right = i * 2 + 1, i * 2 + 2
        if max(left, right) < end_index:
            if lst[i] >= max(lst[left], lst[right]): break
            elif lst[left] > lst[right]:
                swap(lst, i, left)
                i = left
            else:
                swap(lst, i, right)
                i = right
        elif left < end_index:
            if lst[left] > lst[i]:
                swap(lst, i, left)
                i = left
            else: break
        elif right < end_index:
            if lst[right] > lst[i]:
                swap(lst, i, right)
                i = right
            else: break
        else: break

def heap_sort(lst):
    """ Heap sort. Complexity: O(n log n). """
    for j in range((len(lst) - 2) // 2, -1, -1):
        siftDown(lst, j, len(lst))

    for end in range(len(lst)-1, 0, -1):
        swap(lst, 0, end)
        siftDown(lst, 0, end)
    
    return lst


# Testing
x = [1, 7, 4, 9, 2, 9, 67, 4]
print(heap_sort(x))

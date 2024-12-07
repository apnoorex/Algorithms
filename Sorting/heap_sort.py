def swap(seq, i, j):
    seq[i], seq[j] = seq[j], seq[i]
    
def sift_down(seq, i, end_index):
    while True:
        left, right = i * 2 + 1, i * 2 + 2
        if max(left, right) < end_index:
            if seq[i] >= max(seq[left], seq[right]): break
            elif seq[left] > seq[right]:
                swap(seq, i, left)
                i = left
            else:
                swap(seq, i, right)
                i = right
        elif left < end_index:
            if seq[left] > seq[i]:
                swap(seq, i, left)
                i = left
            else: break
        elif right < end_index:
            if seq[right] > seq[i]:
                swap(seq, i, right)
                i = right
            else: break
        else: break

def heap_sort(seq):
    """ Heap sort. Complexity: O(n log n). """
    for j in range((len(seq) - 2) // 2, -1, -1):
        sift_down(seq, j, len(seq))

    for end in range(len(seq)-1, 0, -1):
        swap(seq, 0, end)
        sift_down(seq, 0, end)
    
    return seq


# Testing
x = [1, 7, 4, 9, 2, 9, 67, 4]
print(heap_sort(x))

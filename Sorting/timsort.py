def insertion_sort(seq):
    for idx in range(1, len(seq)):
        item_to_insert = seq[idx]

        while item_to_insert < seq[idx - 1] and idx > 0:
            seq[idx], seq[idx - 1] = seq[idx - 1], seq[idx]
            idx -= 1

    return seq

def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    
    seq_len = len(left) + len(right)
    result = []
    left_idx, right_idx = 0, 0

    while len(result) < seq_len:
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

        if right_idx == len(right):
            result += left[left_idx:]
            break

        if left_idx == len(left):
            result += right[right_idx:]
            break

    return result


def timsort(seq):
    """ Timsort. Complexity: O(n*log(n)). """
    run_size = 4
    seq_len = len(seq)

    # Sort each run using Insertion sort
    for start in range(0, seq_len, run_size):
        end = min(start + run_size - 1, seq_len - 1)
        seq[start:end + 1] = insertion_sort(seq[start:end + 1])

    # Merge sorted runs doubling the size each iteration
    size = run_size
    while size < seq_len:
        for start in range(0, seq_len, size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (seq_len - 1))

            seq[start:end + 1] = merge(seq[start:mid + 1], seq[mid + 1:end + 1])

        size *= 2

    return seq


# Testing
x = [-2, 7, 0, 5, 17, -7, -4, 81, 12, 91, 19, 44] 
print(timsort(x)) 

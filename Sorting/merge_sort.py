def merge_sort(seq):
    """ Merge sort. Complexity: O(n*log(n)). """
    if len(seq) > 1:

        left_part = seq[:len(seq) // 2]
        right_part = seq[len(seq) // 2:]

        merge_sort(left_part)
        merge_sort(right_part)

        left_idx, right_idx, idx = 0, 0, 0

        while left_idx < len(left_part) and right_idx < len(right_part):
            if left_part[left_idx] < right_part[right_idx]:
                seq[idx] = left_part[left_idx]
                left_idx += 1
                idx += 1
            else:
                seq[idx] = right_part[right_idx]
                right_idx += 1
                idx += 1

        while left_idx < len(left_part):
            seq[idx] = left_part[left_idx]
            left_idx += 1
            idx += 1

        while right_idx < len(right_part):
            seq[idx] = right_part[right_idx]
            right_idx += 1
            idx += 1

        return seq
    

# Testing
x = [1, 6, 8, 5, 3, -1, 0, 98, 5, -7]
print(merge_sort(x))

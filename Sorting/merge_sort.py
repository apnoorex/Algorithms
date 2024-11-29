def merge_sort(seq):
    """ Merge sort. Complexity: O(n log n). """
    if len(seq) > 1:

        left_part = seq[:len(seq)//2]
        right_part = seq[len(seq)//2:]

        merge_sort(left_part)
        merge_sort(right_part)

        left, right, final = 0, 0, 0

        while left < len(left_part) and right < len(right_part):
            if left_part[left] < right_part[right]:
                seq[final] = left_part[left]
                left += 1
                final += 1
            else:
                seq[final] = right_part[right]
                right += 1
                final += 1

        while left < len(left_part):
            seq[final] = left_part[left]
            left += 1
            final += 1

        while right < len(right_part):
            seq[final] = right_part[right]
            right += 1
            final += 1

        return seq
    

# Testing
x = [1, 6, 8, 5, 3, 1, 0, 98, 5]
print(merge_sort(x))

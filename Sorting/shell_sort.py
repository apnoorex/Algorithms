def shell_sort(seq):
    """ 
    Shell sort.

    Complexity
    ----------
    Worst case: O(n^2).
    Average case: O(n^(5/4)) to O(n^(3/2)),
    depending on the given sequence and what strategy is used to choose the gap.
    """
    seq_size = len(seq)
    gap = seq_size // 2

    while gap > 0:
        for idx in range(gap, seq_size):
            tmp = seq[idx]
            jdx = idx

            while jdx >= gap and seq[jdx - gap] > tmp:
                seq[jdx] = seq[jdx - gap]
                jdx -= gap
            seq[jdx] = tmp

        gap //= 2

    return seq


# Testing
x = [9, 8, 3, 7, 5, 6, 4, 1]
print(shell_sort(x))

def selection_sort(seq):
    if len(seq) <= 1:
        return seq
    
    sorted = []
    min_val_idx = find_min_value_index(seq)
    sorted.append(seq.pop(min_val_idx))

    return sorted + selection_sort(seq)

def find_min_value_index(seq):
    min_index = 0
    min_value = seq[0]

    for idx in range(1, len(seq)):
        if seq[idx] < min_value:
            min_index = idx

    return min_index


# Testing
x = [1, 4, 3, 2, 0, 89, 6, 1]
print(selection_sort(x))

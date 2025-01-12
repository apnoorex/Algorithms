def knuth_morris_pratt(pattern, text):
    """ 
    Knuth-Morris-Pratt algorithm. 
    
    Finds if provided pattern is in the text. Returns -1 if
    the pattern is not in the text, otherwise returns
    the starting index of the pattern in the text. If there
    are multiple occurences of the pattern in the text, the
    first one is reported.

    Complexity: O(n+m), where:
      n - text length
      m - pattern length
    """
    pat_len = len(pattern)
    txt_len = len(text)

    lps = lps_list(pattern, pat_len)

    pat_idx, txt_idx = 0, 0
    
    while txt_idx < txt_len:
        if pattern[pat_idx] == text[txt_idx]:
            txt_idx += 1
            pat_idx += 1

        if pat_idx == pat_len:
            return txt_idx - pat_idx

        elif txt_idx < txt_len and pattern[pat_idx] != text[txt_idx]:
            if pat_idx != 0:
                pat_idx = lps[pat_idx-1]
            else:
                txt_idx += 1

    return -1

def lps_list(pattern, pat_len):
    """ Creates the Longest Prefix Suffix (LPS) list. """
    lps = [0] * pat_len
    longest = 0 # Longest Prefix-Suffix

    idx = 1
    while idx < pat_len:
        if pattern[idx] == pattern[longest]:
            longest += 1
            lps[idx] = longest
            idx += 1
        else:
            if longest != 0:
                longest = lps[longest-1]
            else:
                lps[idx] = 0
                idx += 1
				
    return lps

# Testing
text = "ababdabbccdabcabdcbba"
pattern = "abcab"
print(knuth_morris_pratt(pattern, text))

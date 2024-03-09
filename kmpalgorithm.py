def compute_lps(pattern):
    lps = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j
    return lps

def kmp_search(text, pattern):
    m = len(pattern)
    n = len(text)

    lps = compute_lps(pattern)
    j = 0

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            print("Pattern found at index", i - m + 1)
            j = lps[j - 1]

# Example usage:
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
kmp_search(text, pattern)

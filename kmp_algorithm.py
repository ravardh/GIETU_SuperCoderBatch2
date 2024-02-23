def kmp_search(text, pattern):
    m, n = len(pattern), len(text)
    lps, i, j = [0] * m, 0, 0  
    while i < n:
        if pattern[j] == text[i]:
            i, j = i + 1, j + 1
            if j == m:
                return True
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return False
text = "ABCBBACBAABACBABC"
pattern = "CBA"
if kmp_search(text, pattern):
    print(f"The pattern '{pattern}' is part of the text.")
else:
    print(f"The pattern '{pattern}' is not part of the text.")

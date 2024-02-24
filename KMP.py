def KMPSearch(pattern, text):
    M = len(pattern)
    N = len(text)

    lps = [0] * M
    computeLPSArray(pattern, M, lps)

    j = 0  # Index for pattern[]
    i = 0  # Index for text[]
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == M:
            print("Pattern found at index " + str(i - j))
            j = lps[j - 1]

        # Mismatch after j matches
        elif i < N and pattern[j] != text[i]:
            # Do not match lps[0..lps[j-1]] characters, they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

def computeLPSArray(pattern, M, lps):
    length = 0  # Length of the previous longest prefix suffix

    lps[0] = 0  # lps[0] is always 0
    i = 1

    # Loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

# Driver code
if __name__ == "__main__":
    text = "ABAABABCABABABCAABABCABAC"
    pattern = "ABABC"
    KMPSearch(pattern, text)

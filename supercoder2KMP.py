def KMPSearch(pat, data):
    M = len(pat)
    N = len(data)

    lps = [0] * M
    j = 0

    LPS(pat, M, lps, j)

    i = 0
    while (N - i) >= (M - j):
        if pat[j] == data[i]:
            i += 1
            j += 1

        if j == M:
            print("Found pattern at index " + str(i - j))
            j = lps[j - 1]

        elif i < N and pat[j] != data[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def LPS(pat, M, lps, j):
    length = 0
    lps[0] = 0
    i = 1

    while i < M:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

data = "ABAABABCABABABCAABABCABAC"
pat = "ABABC"
KMPSearch(pat, data)


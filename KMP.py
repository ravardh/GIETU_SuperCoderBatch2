def KMPSearch(pat, s):
	m = len(pat)
	n = len(s)
	lps = [0]*m
	j = 0
	LPS(pat, m, lps)
	print(lps)
	i = 0 
	while (n - i) >= (m - j):
		if pat[j] == s[i]:
			i += 1
			j += 1
		if j == m:
			print("Found pattern at index " + str(i-j))
			j = lps[j-1]
		elif i < n and pat[j] != s[i]:
			if j != 0:
				j = lps[j-1]
			else:
				i += 1
def LPS(pat, m, lps):
	len = 0 
	lps[0] = 0 
	i = 1
	while i < m:
		if pat[i] == pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			if len != 0:
				len = lps[len-1]
			else:
				lps[i] = 0
				i += 1
if __name__ == '__main__':
	s = "ABABDABACDABABCABAB"
	pat = "ABABCABAB"
	KMPSearch(pat, s)

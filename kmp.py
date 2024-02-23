s = "ACBBACBAABACBABC"
pat = "CBA"
adrs = []
n = len(s)
for i in range (n - 2):
    if s[i] == pat[0]:
        if s[i+1] == pat[1] and s[i+2] == pat[2]:
            adrs.append(i)
print(adrs)
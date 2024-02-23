s = "ABCBBACBAABACBABC"
pat = "CBA"
adrs = []
for i in range(0,len(s)-2):
      if s[i] == pat[0]:
         if s[i+1] == pat[1] and s[i+2] == pat[2]:
            adrs.append(i)
print("Address of pattern is :",adrs)
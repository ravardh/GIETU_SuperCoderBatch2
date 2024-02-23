s = "ABCBBACBAABACBABC"
p = "CBA"

k = len(p)
n = len(s)
ans = []

l,r = 0,0
t = ""
while(r < n):
    t+=s[r]
    if(r-l+1 == k):
        if(t == p):
            ans.append(l)
        t = t[1:]
        l+=1
    r+=1

print(ans)
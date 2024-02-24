def Lps(pat,M,lps):
    len=0
    lps[0]=0
    i=1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i]=len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i]=0
                i += 1
def Kmp(pat,data):
    m=len(pat)
    n=len(data)
    lps=[0]*m
    j=0
    Lps(pat,m,lps)
    i=0
    while(n-i)>=(m-j):
        if pat[j]==data[i]:
            i+=1
            j+=1
        if j==m:
            print("pattern found at index: " + str(i-j))
            j=lps[j-1]
        elif i < n and pat[j]!=data[i]:
            if j!=0:
                j=lps[j-1]
            else:
                i += 1
if __name__ == '__main__':
 data = "ABAABABCABABABCAABABABCABAC"
 pat = "ABABC"
 Kmp(pat,data)

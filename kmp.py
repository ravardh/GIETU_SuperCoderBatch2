def Kmp(pattern,data):
    m=len(pattern)
    n=len(data)
    lps=[0]*m
    j=0
    LPS(pattern,m,lps)
    i=0
    while(n-i)>=(m-j):
        if pattern[j]==data[i]:
            i+=1
            j+=1
        if j==m:
            print("found pattern at index: "+str(i-j))
            j=lps[j-1]
        elif i<n and pattern[j]!=data[i]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1

def LPS(pattern,m,lps):
    l=0
    lps[0]=0
    i=1
    while i<m:
        if pattern[i]==pattern[l]:
            l+=1
            lps[i]=l
            i+=1
        else:
            if l!=0:
                l=lps[l-1]
            else:
                lps[i]=0
                i+=1

# Driver code
if __name__ == '__main__':
	data = "ABAABABCABABABCAABABCABAC"
	pat = "ABABC"
	Kmp(pat, data)

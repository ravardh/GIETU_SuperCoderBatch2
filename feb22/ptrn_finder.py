s= input("Enter String :")
pt=input("Enter Pattern :")
def computeLPSArray(pattern):
    n = len(pattern)
    lps = [0] * n
    length = 0
    i = 1

    while i < n:
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
    print(lps,"LPS")
    return lps
def KMP( p, s):
    lps=computeLPSArray(p)
    ans=[]
    sn=len(s)
    k=len(p)
    i=0
    j=0
    while(i<sn):
        if(s[i]==p[j]):
            i+=1
            j+=1
        if(j==k):
            ans.append(i-j+1)
            j=lps[j-1]
        elif(i<sn and(j==0 or s[i]!=p[j])):
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
    print(ans)
    return ans
KMP(pt,s)
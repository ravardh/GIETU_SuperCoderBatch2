def lps_finder(pattern,M,lps):
    lps[0]=0
    i=1
    len=0
    while(i<M):
        if pattern[i]==pattern[len]:
            len+=1
            lps[i]=len
            i += 1;
        else:
            if(len!=0):
                len=lps[len-1]
            else:
                lps[i]=0;
                i+=1
    return lps
def KMP_Match():
    Str=input("enter the string")
    pat=input("enter the pattern")
    string=list(Str)
    pattern=list(pat)
    lps=[0]*len(pattern)
    M=len(pattern)
    print("lPS of pattern is:-",lps_finder(pattern,M,lps))
    i = 0
    j=0
    N=len(string)
    while (N - i) >= (M - j):
        if pat[j] == string[i]:
            i += 1
            j += 1

        if j == M:
            print("Found pattern at index " + str(i - j))
            j = lps[j - 1]

        elif i < N and pattern[j] != string[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


KMP_Match()
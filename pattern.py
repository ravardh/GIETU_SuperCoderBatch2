
#String =ABCBBACBAABACBABC
#patteern=CBA
def pattern_string(a,p):
    if len(p)>len(a):
        return "Length of pattern is greater than length of String"
    k=len(p)
    for i in range(len(a)-k+1):
        if p==a[i:i+k]:
            print(i)
a="ABCBBACBAABACBABC"
p="CBA"
pattern_string(a,p)

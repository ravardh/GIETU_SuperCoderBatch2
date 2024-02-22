#string= ABCBBACBAABACBABC
#Pattern = CBA
def find_pattern_occurrences(str, pat):
    occurrences = []
    pat_len = len(pat)
    
    for i in range(len(str) - pat_len + 1):
        if string[i:i+pat_len] == pat:
            occurrences.append(i)
    
    return occurrences

string = "ABCBBACBAABACBABC"
pattern = "AAB"
result = find_pattern_occurrences(string, pattern)
print("Occurrences of pattern '{}' in the string: {}".format(pattern, result))
'''def find_pattern(str,patt):
    str_len= len(str)
    patt_len=len(patt)
    occ = []
    for i in range(str_len-patt_len+1):
        match=True
        for j in range (patt_len):
            if str[i+j] !=patt[j]:
                match=False
                break
            if match:
                occ.append(i)
    return occ
str=  "ABCBBACBAABACBABC"
patt = "CBA"
result= find_pattern(str, patt)
print("pattern found at :",result)'''
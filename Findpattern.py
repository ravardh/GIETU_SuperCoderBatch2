def find_pattern(str,patt):
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
str= input("Enter the String:")
patt = input("Enter the pattern:")
result= find_pattern(str, patt)
print("pattern found at :",result)
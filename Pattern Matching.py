input_string='ABCBBACBAABACBAB'
pattern='CBA'
for i in range(0,len(input_string)):
    sub_array=input_string[i:i+len(pattern)]
    if(len(sub_array)==len(pattern)):
        if(pattern==sub_array):
            print("Pattern found at index :",i )
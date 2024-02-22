string="BCDECACSCBNCBACCBACCC"
pattern="CBA"
for i in range(0,len(string)):
    sub_array=string[i:i+3]
    if(len(sub_array)==len(pattern)):
        if(pattern==sub_array):
            print(i,"index postion matched")


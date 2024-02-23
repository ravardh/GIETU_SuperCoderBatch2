str='ABCBBACBAABACBABC'
pattern='CBA'
for i in range(len(str)):
    if(str[i:i+3]==pattern):
        print('index',i)

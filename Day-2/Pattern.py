string='ABCBBACBAABACBABC'
pattern='CBA'
for i in range(len(string)):
    if(string[i:i+3]==pattern):
        print('index',i)

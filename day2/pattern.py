string = 'ABCBBACBAABACBABC'
pat='CBA'
for i in range(len(string)):
    if(string[i:3+i] == pat):
        print('index',i)


String = 'ABCBBACBAABACBABC'
pattern = 'CBA'

count=0
i=0
while i<len(String):
  if  String[i:i+len(pattern)]==pattern:
    count+=1
    i+=len(pattern)
  else:
    i+=1

print(count)
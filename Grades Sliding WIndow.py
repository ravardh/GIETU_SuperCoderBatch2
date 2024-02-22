grades=eval(input())
size=int(input())
max=0
for i in range(0,len(grades)):
    um=0
    if(i+size<len(grades)):
        um=sum(grades[i:i+size])
        if(max<um):
            max=um
print(max)

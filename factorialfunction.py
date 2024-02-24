def factioral(a):
    if(a==1 or a==0):
        return 1
    elif(a<0):
        return "invalid number"
    else:
        return a*factioral(a-1)

b=int(input('enter a number'))
print(factioral(b))
def power(a,b):
    if(b==0):
        return 1
    else:
        return a*power(a,b-1)
a=int(input("enter the base"))
b=int(input("enter the power"))
print("power is :-",power(a,b))
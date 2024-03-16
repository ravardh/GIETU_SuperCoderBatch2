def missing(l1):
        l1.sort()
        var=1
        for i in l1:
            if i==var:
                var+=1
        return var
lst=[]
n=int(input("enter the no of element:-"))
print("enter the elements to array:-")
for i in range(0,n):
    lst.append(int(input()))
res=missing(lst)
print("The minimum missing +ve integer is: ",res)

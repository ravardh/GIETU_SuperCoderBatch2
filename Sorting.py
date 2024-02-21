a=[4, 3 ,2, 1]
def selection(l):
        for i in range(len(l)):
                min=l[i]
                for j in range(i+1,len(l)):
                        if(l[j]<min):
                                l[j],l[i]=l[i],l[j]
                                min=l[i]
        print(l)
def bubble(a):
        for i in range(len(a)):
                for j in range(1,len(a)-i):
                        if(a[j]<a[j-1]):
                                a[j],a[j-1]=a[j-1],a[j]
        print(a)
def insertion(a):
        for i in range(1,len(a)):
                j=i;
                while(j>0  and a[j]<a[j-1]):
                        a[j],a[j-1]=a[j-1],a[j]
                        j-=1
        print(a)
insertion(a)
                                

 
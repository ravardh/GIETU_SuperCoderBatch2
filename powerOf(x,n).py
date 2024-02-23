def Pow(x,n):
   if(n==0):
       return 1
   N=n
   if(N<0):
       N=-N
       x=1/x
   elif(N%2==0):
       return Pow(x*x,N//2)
   else:
       return x*Pow(x,N-1)
print(Pow(2,5))
        
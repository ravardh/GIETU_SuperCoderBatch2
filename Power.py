def power(a,b):
  if(b==1):
    return a
  else:
    return a*power(a,b-1)
a=int(input("Enter a number:"))
b=int(input("Enter the power:"))
print("Power of the number:",power(a,b))
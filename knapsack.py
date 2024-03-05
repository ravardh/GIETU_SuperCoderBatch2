p=[10,5,15,7,6,18,3]
w=[2,3,5,7,1,4,1]
rows = len(p)
C = int(input("Enter the capacity of Bag: "))
NAP = [[0 for _ in range(C+1)] for _ in range(rows+1)]
for i in range(1,C+1):
  for j in range(1,rows+1):
        if w[j-1] <= i:
            NAP[j][i] = max(NAP[j-1][i], NAP[j-1][i-w[j-1]] + p[j-1])
        else:
            NAP[j][i] = NAP[j-1][i]
print(NAP)
print(NAP[rows][C])
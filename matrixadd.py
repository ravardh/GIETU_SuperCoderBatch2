import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[9,8,1],[6,5,9],[3,2,1]])

result = []
sum=0
for i in range(3):
    res = []
    for j in range(3):
        sum=a[i,j]+b[i,j]
        res.append(sum)
    result.append(res)

print(result)

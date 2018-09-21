# program to find transpose of a matrix
mat1 = [[1,2],[4,5],[6,7]]
result = [[0,0,0],[0,0,0],[0,0,0]]
for k in mat1:
    print(k)
for i in range(len(mat1)):
    for j in range (len(mat1[0])):
        result[j][i] = mat1[i][j]

for r in result:
    print(r)

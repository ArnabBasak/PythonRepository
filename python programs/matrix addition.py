# python for matrix addition
mat1 = [[1,2,3],[4,5,6],[7,8,9]]
mat2 = [[10,11,12],[13,14,15],[16,17,18]]
result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        result[i][j] = mat1[i][j]+mat2[i][j]
for r in result:
    print(r)

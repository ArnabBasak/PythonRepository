#python program for matrix multiplicaton
mat1 = [[1,2,3],[4,5,6],[7,8,9]]
mat2 = [[10,11,12],[13,14,15],[16,17,18]]
result = [[0,0,0],[0,0,0],[0,0,0]]
for i in range (len(mat1)):
    for j in range(len(mat2[0])):
        for k in range(len(mat2)):
            result[i][j] +=mat1[i][k] * mat2[k][j]
for r in result:
    print(r)
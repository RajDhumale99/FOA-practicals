matrix1 = [[1,2],[3,4]]
matrix2 = [[5,6],[7,8]]
result_matrix = [[0,0],[0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result_matrix[i][j] = matrix1[i][k] * matrix2[k][j]
print(result_matrix)

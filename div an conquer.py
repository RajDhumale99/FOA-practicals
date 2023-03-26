def strassen_matrix_multiply(matrix1, matrix2):
 n = len(matrix1)
 # Base case: if the matrices are 1x1
 if n == 1:
    return [[matrix1[0][0] * matrix2[0][0]]]
 # Split matrices into quadrants
 size = n // 2
 A = [matrix1[i][:size] for i in range(size)]
 B = [matrix1[i][size:] for i in range(size)]
 C = [matrix1[i][:size] for i in range(size, n)]
 D = [matrix1[i][size:] for i in range(size, n)]
 E = [matrix2[i][:size] for i in range(size)]
 F = [matrix2[i][size:] for i in range(size)]
 G = [matrix2[i][:size] for i in range(size, n)]
 H = [matrix2[i][size:] for i in range(size, n)]
 # Recursive steps
 P1 = strassen_matrix_multiply(A, sub(F, H))
 P2 = strassen_matrix_multiply(add(A, B), H)
 P3 = strassen_matrix_multiply(add(C, D), E)
 P4 = strassen_matrix_multiply(D, sub(G, E))
 P5 = strassen_matrix_multiply(add(A, D), add(E, H))
 P6 = strassen_matrix_multiply(sub(B, D), add(G, H))
 P7 = strassen_matrix_multiply(sub(A, C), add(E, F))
 # Compute the result matrix
 result_matrix = [[0 for _ in range(n)] for _ in range(n)]
 for i in range(size):
    for j in range(size):
        result_matrix[i][j] = P5[i][j] + P4[i][j] - P2[i][j] + P6[i][j]
        result_matrix[i][j+size] = P1[i][j] + P2[i][j]
        result_matrix[i+size][j] = P3[i][j] + P4[i][j]
        result_matrix[i+size][j+size] = P5[i][j] + P1[i][j] - P3[i][j] - P7[i][j]
 return result_matrix
# Helper functions to add and subtract matrices
def add(matrix1, matrix2):
 return [[matrix1[i][j]+matrix2[i][j] 
 for j in range(len(matrix1))] for i in range(len(matrix1))]
def sub(matrix1, matrix2):
 return [[matrix1[i][j]-matrix2[i][j] 
 for j in range(len(matrix1))] for i in range(len(matrix1))]
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result_matrix = strassen_matrix_multiply(matrix1, matrix2)
print(result_matrix)

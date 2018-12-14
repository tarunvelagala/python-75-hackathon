# to prove transpose of a transposed matrix is always the same matrix using numpy
import numpy as np
row_column = [int(i) for i in input('Enter the row and column values: ').split()]
matrix_list  = []
for i in range(0, row_column[0]):
    matrix_list.append([int(i) for i in input().split()])
np_array = np.array(matrix_list)
np_transpose = np.transpose(np_array)
print('Array Transpose  \n', np_transpose, end='\n')
print('Transposed Matrix Transpose \n', np.transpose(np_transpose), end='\n')
if np.array_equal(np_array, np.transpose(np_transpose)):
    print('((A)T)T = A')

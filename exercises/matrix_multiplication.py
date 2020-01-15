# 1) Write a function that multiplies two N*N matrices.
# As a test you can use:
A = [[2,4],
     [3,1]]
B = [[2,1],
     [1,3]]
# the result of which is:
#
# AB = [[8, 14]
#       [7, 6]]
'''the multiplication must be row by column
pseudocode
use a for cicle that for every rowCol element computes'''

product_matrix = []

for row in range(len(A)):
    temp_row = []
    for col in range(len(A)):
        temp_row.append(0)
    product_matrix.insert(row, temp_row)
for row in range(len(A)):
    for col in range(len(A)):
        sum = 0
        for i in range(len(A)):
                sum += A[row][i] * B[i][col]
        product_matrix[row][col] = sum
print(product_matrix)

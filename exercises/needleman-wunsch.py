
def matrix_dict(matrix_file):
    list = []
    for line in matrix_file:
        line = line.rstrip()
        row = line.split()
        list.append(row)
    dict = {}
    for i in range(1, len(list)):
        for j in range(0, len(list[0])):
            dict[list[i][0] + list[0][j]] = int(list[i][j+1])
    return dict
matrix = open('./data/blosum.txt', 'r')
blosum = matrix_dict(matrix)
matrix.close()

seq1 = 'ACY'
seq2 = 'CWWQ'

gap_penalty = 2
scores_matrix = []
traceback_matrix = []
row = 0
while row != len(seq1) + 2:
    temp_list = []
    col = 0
    while col != len(seq2) + 2:
        temp_list.append(None)
        col += 1
    scores_matrix.insert(row, temp_list)
    row +=1
traceback_matrix = scores_matrix

scores_matrix[1][1] = 0
for row in range(2, len(scores_matrix)):
    for col in range(2, len(scores_matrix[0])):
        scores_matrix[1][col] = scores_matrix[1][col - 1] - gap_penalty
        scores_matrix[row][1] = scores_matrix[row - 1][1] - gap_penalty

# for row in range(2, len(scores_matrix) + 1):
#     for col in range(2, len(scores_matrix[0]) + 1):
#         score_up = 0
#         score_left = 0
#         score_diag = 0
#         score_up = scores_matrix[row - 1][col] + blosum[seq1[row] + seq2[col]]
#         score_left = scores_matrix[row][col] + blosum[seq1[row] + seq2[col]]
#         score_diag = scores_matrix[row - 1][col - 1] + blosum[seq1[row] + seq2[col]]
#         score_final = max(score_up, score_diag, score_left)
#         print(score_final)
#         scores_matrix[row][col] = score_final
print(scores_matrix)

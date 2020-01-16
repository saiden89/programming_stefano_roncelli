amino = 'ARNDCQEGHILKMFPSTWYV'
seq1 = 'ACG---THHWWHW'
seq2 = 'KKKT-----TYWW'
file = open('./exercises/diagonalM.txt', 'r')
matrix = {}
for am in amino:
    row = file.readline().split()
    for i in range(len(row)):
        value = row[i]
        pair = am + amino[i]
        print(row[i])
        matrix[pair] = int(value[:-1])
print(matrix)

def score_fun(s1, s2, scoring_matrix):
    score = 0
    gap_penalty = -2
    for base1, base2 in zip(s1, s2):
        if base1 == '-' or base2 == '-':
            score += gap_penalty
        elif base1+base2 not in matrix:
            score += scoring_matrix[base2 + base1]
        else:
            score += scoring_matrix[base1 + base2]

    print(score, sep = '\n')
    return score

score_fun(seq1, seq2, matrix)

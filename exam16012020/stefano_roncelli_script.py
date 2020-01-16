import input_data
def dict_matrix(filepath):
    file = open(filepath, 'r')
    residues = 'ARNDCQEGHILKMFPSTWYV'
    matrix = {}
    file.readline()
    for aa in residues:
        line = file.readline()
        line = line.split()
        for i in range(len(line)):
            value = line[i]
            value = int(value[:-1])
            pair = residues[i] + aa
            matrix[pair] = value
    return matrix

blosum = dict_matrix('./data/BLOSUM62.txt')
pam = dict_matrix('./data/PAM250.txt')


ali = input_data.alignments
def score_fun(s1, s2, matrix):
    score = 0
    gap_penalty = -2
    gap_extension = -0.5
    ext = 0
    for base1, base2 in zip(s1, s2):
        if base1 == '-' or base2 == '-': #doesn't take into consideration that the gaps have to be introduced in the same sequence. unfortunaltely short on time, sorry
            ext += 1
            score += gap_penalty + (ext - 1) * gap_extension
        elif base1+base2 not in matrix:
            ext = 0
            score += matrix[base2+base1]
        else:
            ext = 0
            score += matrix[base1+base2]
    print(s1, s2, sep='\n')
    return score
for i in range(len(ali)):
    print(score_fun(ali[i][0], ali[i][1], pam))
for i in range(len(ali)):
    print(score_fun(ali[i][0], ali[i][1], blosum))

# 2) Write a script that generates all the possible ungapped alignments of two sequences, scores them and identifies
# the best scoring ones.
#
# These are all the possible ungapped alingments of the two sequences: TCA and GA:
#
# --TCA  -TCA  TCA  TCA  TCA-  TCA--
# GA---  GA--  GA-  -GA  --GA  ---GA
#
# Using the following scoring scheme:

score_matrix = {'AA': 2, 'AC':-1, 'AT':-1, 'AG': 0,
                'CA':-1, 'CC': 2, 'CT': 0, 'CG':-1,
                'TA':-1, 'TC': 0, 'TT': 2, 'TG':-1,
                'GA': 0, 'GC':-1, 'GT':-1, 'GG': 2}

seq1 = 'TCA'
seq2 = 'GA'
original_len_seq1 = len(seq1)
original_len_seq2 = len(seq2)
seq1 = '-' * original_len_seq2 + seq1 + '-' * original_len_seq2
seq2 = '-' * original_len_seq1 + seq2 + '-' * original_len_seq1
print(seq1)
print(seq2)


i = 0
while i != (original_len_seq1 + original_len_seq2):
    score = 0
    for j in range(len(seq1) - i - 1):
        pair = seq1[original_len_seq2 + j] + seq2[j + i]
        if pair[0] == '-' or pair[1] == '-':
            score -= 2
        else:
            score += matrix[pair]
    print(score)
    i += 1

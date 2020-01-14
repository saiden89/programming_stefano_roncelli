matrix = {'AA': 2, 'AC': -1, 'AT': -1, 'AG': -2, 'CC': 2, 'CT': 0, 'CG': -1,
          'TT': 2, 'TG': -1, 'GG': 2, 'CA': -1, 'TA': -1, 'GA': -2, 'TC': 0,
          'GC': -1, 'GT': -1, }
seq1 = 'AAA'
seq2 = 'TT'
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

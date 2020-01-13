matrix = {'AA': 2, 'AC': -1, 'AT': -1, 'AG': -2, 'CC': 2, 'CT': 0, 'CG': -1,
          'TT': 2, 'TG': -1, 'GG': 2, 'CA': -1, 'TA': -1, 'GA': -2, 'TC': 0,
          'GC': -1, 'GT': -1, }
seq1 = 'A'
seq2 = 'TTC'
seq1_list = list(seq1)
seq2_list = list(seq2)
for bases in range(len(seq2)):
    seq1_list.append('-')
for bases in range(len(seq1)):
    seq2_list.insert(0, '-')
highest = 0
best_seq1 = ''
best_seq2 = ''
while seq2_list != []:
    score = 0
    del seq2_list[0]
    for base1, base2 in zip(seq1_list, seq2_list):
        if base1 != '-' and base2 != '-':
            score += matrix[base1 + base2]
    if score > highest:
        best_seq1 = ''.join(seq1_list)
        best_seq2 = ''.join(seq2_list)
        highest = score
comp = ''
for base1, base2 in zip(best_seq1, best_seq2):
    if base1 == base2:
        comp += '|'
    else:
        comp += ' '
print(best_seq1, comp, best_seq2,sep = '\n')
print('The best alignment score is:', highest)

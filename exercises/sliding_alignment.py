matrix = {'AA': 2, 'AC': -1, 'AT': -1, 'AG': -2, 'CC': 2, 'CT': 0, 'CG': -1,
          'TT': 2, 'TG': -1, 'GG': 2, 'CA': -1, 'TA': -1, 'GA': -2, 'TC': 0,
          'GC': -1, 'GT': -1, }
seq1 = 'AAAAC'  #the two starting sequences
seq2 = 'CCCCCCCAAAAAAAC'
seq1_list = list(seq1)  #they get converted to lists for ease of editing
seq2_list = list(seq2)
for bases in range(len(seq2)):  # the first sequence gets an amount of "-" in order to
                                # get like ATCC---
                                #          ----CCT
    seq1_list.append('-')
for bases in range(len(seq1)):  # same for the second sequences
    seq2_list.insert(0, '-')
highest = 0                     #intialize some parameters in order to retrieve
                                # the highest score calculated
best_seq1 = ''
best_seq2 = ''

                                # this is the main algorithm, which first
                                # computes the score, then sequentally removes
                                # only hte first caracter of the second sequence
                                # in order to perform the alignment.
while seq2_list != []:
    score = 0
    if seq2_list[0
    ] != '-':
        del seq2_list[0]
        for base1, base2 in zip(seq1_list, seq2_list):
            if base1 != '-' and base2 != '-':
                score += matrix[base1 + base2]
            else:
                score -= 2
    else:
        seq1_list.insert(0, '-')
        for base1, base2 in zip(seq1_list, seq2_list):
            if base1 != '-' and base2 != '-':
                score += matrix[base1 + base2]
            else:
                score -= 2
    if score > highest:                            # score
        best_seq1 = ''.join(seq1_list)             # if the new score is higher
        best_seq2 = ''.join(seq2_list)             # than highest, it saves it
        highest = score                            # and the sequences
                           # this deletes the first character
comp = ''
for base1, base2 in zip(best_seq1, best_seq2):
    if base1 == base2:
        comp += '|'
    else:
        comp += ' '
print(best_seq1[:len(best_seq2)], comp, best_seq2,sep = '\n')
print('The best alignment score is:', highest)

# 2) Write a script that generates all the possible ungapped alignments of two sequences, scores them and identifies
# the best scoring ones.
#
# These are all the possible ungapped alingments of the two sequences: TCA and GA:
#
# --TCA  -TCA  TCA  TCA  TCA-  TCA--
# GA---  GA--  GA-  -GA  --GA  ---GA
#
# Using the following scoring scheme:# 2) Write a script that generates all the possible ungapped alignments of two sequences, scores them and identifies
# the best scoring ones.
#
# These are all the possible ungapped alingments of the two sequences: TCA and GA:
#
# --TCA  -TCA  TCA  TCA  TCA-  TCA--
# GA---  GA--  GA-  -GA  --GA  ---GA
#
# Using the following scoring scheme:

matrix = {'AA': 2, 'AC': -1, 'AT': -1, 'AG': -2, 'CC': 2, 'CT': 0, 'CG': -1,
          'TT': 2, 'TG': -1, 'GG': 2, 'CA': -1, 'TA': -1, 'GA': -2, 'TC': 0,
          'GC': -1, 'GT': -1, }
human = open('./data/titin_hu.txt', 'r')
mouse = open('./data/titin_mo.txt', 'r')
seq1 = ''
seq2 = ''
for line in human:
    line = line.rstrip()
    seq2 += line
for line in mouse:
    line = line.rstrip()
    seq2 += line


# seq1 = 'TT'
# seq2 = 'GTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT'
len_seq1 = len(seq1)
len_seq2 = len(seq2)
iters = len_seq1 + len_seq2
same_size = False
if len_seq1 < len_seq2:
    short = seq1
    long = seq2
elif len_seq1 > len_seq2:
    short = seq2
    long = seq1
else:
    same_size = True
    short = seq1
    long = seq2
len_short = len(short)
len_long = len(long)
long = long + '-' * len_short
short = '-' * len_long + short
short = list(short)
long = list(long)
highest = False
best_seq1 = ''
best_seq2 = ''
def score_fun(s1, s2, scoring_matrix):
    score = 0
    gap_penalty = -2
    for base1, base2 in zip(s1, s2):
        if base1 == '-' or base2 == '-':
            score += gap_penalty
        else:
            score += scoring_matrix[base1 + base2]
    print(''.join(s1), ''.join(s2), score, sep = '\n')
    return score

for i in range(iters - 1):
    score = score_fun(long, short, matrix)
    if long[-1] == '-' and short[0] == '-':
         del short[0]
         del long[-1]
         score = score_fun(long, short, matrix)
    elif long[-1] != '-' and short[0] == '-':
        short.append('-')
        del short[0]
        score = score_fun(long, short, matrix)
    else:
        long.insert(0, '-')
        short.append('-')
        score = score_fun(long, short, matrix)
    if highest == False:
        highest = score
    if score > highest:
        best_seq1 = ''.join(long)
        best_seq2 = ''.join(short)
        highest = score
print(highest)

comp = ''
for base1, base2 in zip(best_seq1, best_seq2):
    if base1 == base2:
        comp += '|'
    else:
        comp += ' '
print(best_seq1, comp, best_seq2,sep = '\n')
print('The best alignment score is:', highest)

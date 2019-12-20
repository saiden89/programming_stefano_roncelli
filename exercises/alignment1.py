def basic_align(seq1, seq2):
    score = 0
    if len(seq1) == len(seq2):
        for base1, base2 in zip(seq1, seq2):
            if base1 == base2:
                 score += 1
            else:
                score -= 0
    return score


def aa_extract(file):
    aa_list = []
    for line in file:
        if line.startswith(' ') == False:
            aa_list.append(line[0])
    return(aa_list)

matrix = open('./exercises/blosum.txt', 'r')
aa_list = aa_extract(matrix)
matrix.close()

# def init_dict(aa_list):
#     dict = {}
#     for aa1 in aa_list:
#         for aa2 in aa_list:
#             dict[aa1+aa2] =
#     return dict

def value_list(matrix):
    values = []
    for line in file:
        if line startswith(' ') == False:
            for i in range(len(line)):
                if i ==

dict = init_dict(aa_list)

matrix = open('./exercises/blosum.txt', 'r')
def get_score(file, aa1, aa2):
    for line in file:
        line = line.rstrip()
        if line.startswith('  '):
            col = line.find(aa1)
        else:
            row = line.find(aa2)

# def pair_dict(list):
#     dict = {}
#     for aa in list:
#         if dict[aa] not in dict:
#             dict[aa] =

'''
Pseudocode:
def score.m(s1, s2, S, d):
    init F to the 0 matrix
    init F[i,0]
    init F[0,i]
    iteration of i,j
    return F
'''


# bases = 'ATGC'
# nucleo_matrix = {}
# for row in bases:
#     for col in bases:
#         if row == col:
#             nucleo_matrix[row + col] =  1
#         else:
#             nucleo_matrix[row + col] = -1

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

seq1 = ("""MTTQAPTFTQPLQSVVVLEGSTATFEAHISGFPVPEVSWFRDGQVISTSTLPGVQISFSD
GRAKLTIPAVTKANSGRYSLKATNGSGQATSTAELLVKAETAPPNFVQRLQSMTVRQGSQ
VRLQVRVTGIPTPVVKFYRDGAEIQSSLDFQISQEGDLYSLLIAEAYPEDSGTYSVNATN
SVGRATSTAELLVQGEEEVPAKKTKTIVSTAQISESRQTRIEKKIEAHFDARSIATVEMV
IDGAAGQQLPHKTPPRIPPKPKSRSPTPPSIAAKAQLARQQSPSPIRHSPSPVRHVRAPT
PSPVRSVSPAARISTSPIRS
""")

seq2 = ("""MTTQAPEEPEEYVVEEKMHFISKKVEVEPAKVPEKKIIPK
PKVPAKIEEPPPTKVPEPPKKIVPEKKVPAPAPKKVPPAKAPEESKRPVPEKRAPAEEVG
IEEPPPTKVAERHMKITQEEKVLVAVTKKEAPPRARVPEEPKKVAPEERFPKLKPRREEE
PPAKVTEVRKRAVKEEKVSIEVPKREPRPTKEVTVTEEKKWSYTREEETVSEHREEEYED
YEDYEEYKEFEEYEPTEEYDQYDEYAEREVEHYEEHEEYVTEPKKPVPVKPAQEPVPAKP
KAPPPKVLKKAVPEEKAPLPIQKKLKPLPPKAPEEPKKVVEEKIQISITKREKQQVTEPV
AKVPMKPKRVVPEAKIPAPTKEVAVPVRVPGVPKKRELEEVVVFKEEVEAHEEYIVEEEE
EYVHEEEYVHKEEYVHEEEYVHKEEYIHEEEEHLHEEEETIAEEEVVPVAPVKVPVVPKK
PVPEEKKPVPVPKKKEAPPAKVPEIPKKPEEKVPVPIPKKEKAPPAKVPEVPKKPVPEEK
PPVPVPKKVEPPPAKVPEVPKKPVPEKKVPAPTPKKVEAPPAKVPEVPKKPIPEEKKPTA
LLKKMEAPPPKAPKKREVVPVPVALPREEEEEEVPFEEVPEEEILPEEEVPSEEEAPPEE
VPPEEEEVLPEEEEVLPEEEEVLPEEEEVQPEEEALPEIKPKVPKPAPVPKKTVPEKKVP
VPVPKKVEPPPPPKVPEIKKKVPEKKVVVPKKEEAPPTKVPEVSKKVEERRIIPPKEEEV
PPAEVYEEAEEPTPEEIPEEPPSIEEEEIVEEEEEEEEVLPPRAPEVVKKAVPEAPTPVP
KKAEAPPAKVPKK
""")

seq1 = seq1.replace('\n', '')
seq2 = seq2.replace('\n', '')
gap_penalty = -2
scores_matrix = []
traceback_matrix = []
m = len(seq1) + 1
n = len(seq2) + 1

scores_matrix = [[0] * m for x in range(n)]
traceback_matrix = [[0] * m for x in range(n)]

for row in range(1, len(scores_matrix)):
    scores_matrix[row][0] = gap_penalty * row
    traceback_matrix[row][0] = 'u'
for col in range(1, len(scores_matrix[0])):
    scores_matrix[0][col] = gap_penalty * col
    traceback_matrix[0][col] = 'l'

for row in range(1, n):
    for col in range(1, m):
        scores = {}
        up = 0
        left = 0
        diag = 0
        up = scores_matrix[row - 1][col] + gap_penalty
        left = scores_matrix[row][col -1 ] + gap_penalty
        diag = scores_matrix[row - 1][col - 1] + blosum[seq1[col - 1] + seq2[row - 1]]
        scores[up] = 'u'
        scores[left] = 'l'
        scores[diag] = 'd'
        score_final = max(up, diag, left)
        traceback_matrix[row][col] = scores.get(max(scores))
        scores_matrix[row][col] = score_final

ali1 = ''
ali2 = ''
equal = ''
row = n -1
col = m -1
while row != 0:
    while col != 0:
        if traceback_matrix[row][col] == 'u':
            ali1 += '-'
            ali2 += seq2[row - 1]
            equal += ' '
            row -= 1
        elif traceback_matrix[row][col] == 'l':
            ali1 += seq1[col - 1]
            ali2 += '-'
            equal += ' '
            col -= 1
        else:
            ali1 += seq1[col - 1]
            ali2 += seq2[row - 1]
            equal += '|'
            col -= 1
            row -= 1
ali1 = ali1[::-1]
ali2 = ali2[::-1]
equal = equal[::-1]
print(ali1, equal, ali2, scores_matrix[n -1][m -1], sep= '\n')

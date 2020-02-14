
'''
In all the script, for consistency purposes i, n are always the rows generated from seq2
j, m are always the columns generated from seq2
'''
def nw(seq1, seq2, matrix, gap):
    F = []      #Initialization of the empty datastructures of proper dimensions
    P = []      # F = score matrix, P = traceback matrix
    m = len(seq1) + 1
    n = len(seq2) + 1
    F = [[0] * m for x in range(n)] #population of the two matrices with 0
    P = [[0] * m for x in range(n)]
    for i in range(1, n):           # Initialization of the first rows and columns
        F[i][0] = F[i-1][0] + gap   # of both matrices
        P[i][0] = 'u'
    for j in range(1, m):
        F[0][j] = F[0][j-1] + gap
        P[0][j] = 'l'
    for i in range(1, n):       # this is the core of nw alignmet, for each i,j
        for j in range(1, m):   # position in both matrices only the best scrore
            scores = {}         #direction is kept, others are discarded
            s = 0               # d = diagonal, l = left, u = up
            d = F[i-1][j-1] + matrix[seq1[j-1] + seq2[i-1]]
            scores[d] = 'd'
            l = F[i][j-1] + gap
            scores[l] = 'l'
            u = F[i-1][j] + gap
            scores[u] = 'u'
            s = max(d, l ,u)
            F[i][j] = s
            P[i][j] = scores.get(max(d, l ,u))
    return F,
def traceback(F, P, s1, s2):
    i = len(seq2)   # Initialization of variables, best1, best2 will be the final
    j = len(seq1)   # gapped alignments, score is the final score of the alignment
    best1 = ''
    best2 = ''
    score = F[i][j]
    while i != 0 or j != 0: # This while is the core of the traceback algorithm,
        if P[i][j] == 'd':  # it terminates when it reaches the 0,0 potition in
            best1 += s1[j-1] # the traceback matrix
            best2 += s2[i-1]
            i -= 1
            j -= 1
        elif P[i][j] == 'l':
            best1 += s1[j-1]
            best2 += '-'
            j -= 1
        elif P[i][j] == 'u':
            best1 += '-'
            best2 += s2[i-1]
            i -= 1
    best1 = best1[::-1]
    best2 = best2[::-1]
    return best1, best2, score


from input_data import seq1, seq2, BLOSUM52 # since the functions return a tuple
T = nw(seq1, seq2, BLOSUM52, -2)            # we need to split its output
F = T[0]
P = T[1]
print(traceback(F, P, seq1, seq2))

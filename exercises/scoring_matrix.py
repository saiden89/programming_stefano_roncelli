seq_1 = 'ACAGGTGGACCTCTATATGG'
seq_2 = 'ACTGGTCGACTTCCGGATCG'
def prob_base(seq1, seq2, base):
    seq = seq1 + seq2
    bases_in_seq = seq.count(base)
    freq = bases_in_seq / len(seq)
    return freq

def prob_matches(seq1, seq2):
    matches = {}
    list_keys = []
    for base1 in seq1:
        for base2 in seq2:
            matches[base1 + base2] = 0
    for base1, base2 in zip(seq1, seq2):
        if base1 + base2 in matches:
            matches[base1 + base2] += 1
        else:
            matches[base1 + base2] = 1
    for pair in matches:
        matches[pair] =  matches[pair]/len(seq1)

    return matches
print(prob_matches(seq_1, seq_2))

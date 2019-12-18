def basic_align(seq1, seq2):
    score = 0
    if len(seq1) == len(seq2):
        for base1, base2 in zip(seq1, seq2):
            if base1 == base2:
                 score += 1
            else:
                score -= 0
    return score
oligo1 = 'AAAAAAAAAAAAAAAAAAA'
oligo2 = 'AAAAAAAAAAAAAAAAAAA'
print(basic_align(oligo1, oligo2))

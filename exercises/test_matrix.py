matrix = open('./exercises/blosum.txt', 'r')
list = []
for line in matrix:
    line = line.rstrip()
    row = line.split()
    list.append(row)
dict = {}
seq1 = 'ALASVLIRLITRLYP'
seq2 = 'ASAVHLNRLITRLYP'
print(list)

for i in range(1, len(list)):
    for j in range(0, len(list[0])):
        dict[list[i][0] + list[0][j]] = list[i][j+1]
sum = 0
for base1, base2 in zip(seq1, seq2):
    sum += int(dict[base1 + base2])
print(sum)
matrix.close()

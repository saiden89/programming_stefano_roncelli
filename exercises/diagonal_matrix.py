amino = 'ARNDCQEGHILKMFPSTWYV'
file = open('./exercises/diagonalM.txt', 'r')
for am in amino:
    row = file.readline().split()
    print(am, row)
    for i in range(len(row)):
        print(am, amino[i], row[i])
matrix = {}

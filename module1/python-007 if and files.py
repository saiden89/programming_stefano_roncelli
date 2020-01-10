#1
list = []
for num in range(3, 12):
    list.append(num)
print(list)

#2
for num in list:
    if (num % 2) == 0:
        print(num)

#3
for num in list:
    if (num % 5) == 0:
        print(num)

#4
list = [5,2,7,8,1,-3]
print(list)

#5
print(list[0], list[2])

#6
for num in list:
    print(num * 2) 

#7
for num in list:
    print(((num * 2) -2 ) / 3)

#8
sum = 0
for num in list:
    sum += num 
print(sum)

#9
lowest = list[0]
for i in range(len(list)):
    if list[i] < lowest:
        lowest = list[num]
print(lowest)

#10
highest = list[0]
for i in range(len(list)):
    if list[i] > highest:
        highest = list[i]
print(highest)

#11
sum = 0
for num in list:
    sum += num
avg = sum / len(list)
print(avg)

#12
a = 'avocado'
b = 'radar'

#13
print(a[::-1])
print(b[::-1])

#14
if a[::-1] == a: print("a is a palindrome")
else: print("a is not a palindrome")
if b[::-1] == b: print("b is a palindrome")
else: print("b is not a palindrome")

#15
print(a[:len(a) // 2])
print(b[len(b) // 2:])

#16 bleh
oligo_1 = 'AATTTCCT'
oligo_2 = 'AGGAAATT'

#17
def reverse(oligo_1, oligo_2):
    oligo_2_rev = ''
    for i in range(len(oligo_2)):   
        if oligo_2[i] == 'A':
            oligo_2_rev += 'T'
        elif oligo_2[i] == 'C':
            oligo_2_rev += 'G'
        elif oligo_2[i] == 'T':
            oligo_2_rev += 'A'
        elif oligo_2[i] == 'G':
            oligo_2_rev += 'C'
    return oligo_2_rev
    #if oligo_2_rev == oligo_1: print('Yes')
    #else: print('No')

#18
sequence_1 = 'GTCAGTCACGATCGACTCCCAGTCACGACGATCGATCGAC'
sequence_2 = 'AGCGTACGATCGATCAGCTAGCACGCGCGCTGAGTATGCA'
def complementar(seq):
    seq_rev = ''
    for base in seq:
        if base == 'A': base = 'T'
        elif base == 'T': base = 'A'
        elif base == 'G': base = 'C'
        elif base == 'C': base = 'G'
        seq_rev += base
    return seq_rev

def seq_compare(seq_1, seq_2):
    comparison = ''
    seq_2_comp = complementar(seq_2)
    for i in range(len(seq_1)):
            if seq_1[i] == seq_2_comp[i]:
                comparison += '|'
            else: comparison += 'X'
    print(seq_1)
    print(comparison)
    print(seq_2)
seq_compare(sequence_1, sequence_2)

#22
# seq_1 = 'GTCAGTCACGATCGACTCCCAGTCACGACGATCGATCGAC'
# seq_2 = 'AGCGTACGATCGATCAGCTAGCACGCGCGCTGAGTATGCA'
# def seq_compare(a, b):
#   reverse('',seq_2)
#   comparison = ''
#   complementary = 0
#   for base_1, base_2 in zip(seq_1, seq_2):
#           if base_1 == base_2:
#               comparison += '|'
#               complementary += 1
#           else: comparison += 'X'
#   print(seq_1)
#   print(comparison)
#   print(seq_2)
#   print('The number of complementary positions is:', complementary)
# seq_compare(seq_1, seq_2)
Theory
def divisor(n):
	divisors = []
	for x in range(1, (n + 2)//2):
		if (n % x) == 0:
			divisors.append(x)
	divisors.append(n)
	print(divisors)
	print("The number of divisors is", len(divisors))
divisor(48917242)

Files
infile = open('/home/stefano/Università/PB/10_sequences.seq', 'r')
print(infile.readline())
for line in infile:
	print(line)

#ex1
seq_1 = 'CAGCAGCAGCAGCAGCACGACGAAGCAAAACACGCGACACACGACACGACAGCACAGCACGACGACGACGCGCGCACAGCA'
num_A = seq_1.count('A')
num_T = seq_1.count('T')
num_G = seq_1.count('G')
num_C = seq_1.count('C')
if num_A != 0: print('A count:', num_A)
if num_T != 0: print('T count:', num_T)
if num_G != 0: print('G count:', num_G)
if num_C != 0: print('C count:', num_C)

#ex2
num_A = seq_1.count('A')
num_T = seq_1.count('T')
num_G = seq_1.count('G')
num_C = seq_1.count('C')
if num_A != 0: print('A count:', num_A)
else: print('A not found')
if num_T != 0: print('T count:', num_T)
else: print('T not found')
if num_G != 0: print('G count:', num_G)
else: print('G not found')
if num_C != 0: print('C count:', num_C)
else: print('C not found')

ex3
file = open('/home/stefano/Università/PB/10_sequences.seq', 'r')
num_line = 1
for line in file:
	line = line.rstrip()
	print(num_line, line)
	num_line += 1

#ex4
for line in file:
	line = line.rstrip()
	if 'CTATA' in line:
		print(line)
		print('The pattern first occurs in position', line.find('CTATA'))

#ex5
#a
def line_count(file_path):
	file = open(file_path, 'r')
	n_line = 0
	for line in file:
		n_line += 1
	file.close()
	return n_line

def pattern_count(file_path, pattern):
	file = open(file_path, 'r')
	counter = 0
	for line in file:
		if pattern in line:
			counter += 1
	file.close()
	return counter

def length_limit(file_path, threshold):
	file = open(file_path, 'r')
	counter = 0
	for line in file:
		if len(line) > threshold:
			counter += 1
	file.close
	return counter


def gc_comp(file_path, threshold):
	file = open(file_path, 'r')
	counter = 0
	for line in file:
		line = line.rstrip()
		gc = line.count('G') + line.count('C')
		if (gc / len(line)) > threshold:
			counter	+=1
	file.close()
	return counter

#ex6
file = open('/home/stefano/Università/PB/sequences.seq', 'r')
bases = ['A', 'T', 'G', 'C']
def other_letter(file):
    found = 0
	tot = 0
	for sequence in file:
		sequence = sequence.rstrip()
		for base in sequence:
			if not(base in bases6):
				found = 1
		if found == 1:
			tot += 1
		found = 0
	return tot



# print(line_count('/home/stefano/Università/PB/sequences.seq'))
# print(pattern_count('/home/stefano/Università/PB/sequences.seq', 'CTATA'))
# print(gc_comp('/home/stefano/Università/PB/sequences.seq', 0.5))
# print(length_limit('/home/stefano/Università/PB/sequences.seq', 1000))
print(other_letter(file))
file.close()
import sys
print(sys.version())

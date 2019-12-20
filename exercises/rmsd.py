import math

def extract_coords(pdb):
    atom_list = []
    coord_list = []
    for line in pdb:
        line = line.rstrip()
        if 'CA' in line and line.startswith('ATOM'):
            #while '  ' in line:
                #line = line.replace('  ', ' ')
            atom_list = line[32:55].split()
            coord_list.append(atom_list[:])
    for i in range(len(coord_list)):
        for j in range(3):
            coord_list[i][j] = float(coord_list[i][j])
    return coord_list
pdb1 = open('/home/stefano/Università/PB/allegra/model8.pdb', 'r')
pdb2 = open('/home/stefano/Università/PB/allegra/2.pdb', 'r')
coord1 = extract_coords(pdb1)
print(len(coord1))
coord2 = extract_coords(pdb2)
print(len(coord2))
print(coord2)

def rsmd(coo1, coo2):
    sum = 0
    for atom1, atom2 in zip(coo1, coo2):
        sum += (atom2[0] - atom1[0])**2 + (atom2[1] - atom1[1])**2 + (atom2[2] - atom1[2]) **2
    return math.sqrt(sum/100)

print(rsmd(coord1, coord2))

def seq_weight(seq_file, lower_weight, upper_weight):
    weights = [
        ['A', 347.0],  # weights is a list with the following architecture
        ['C', 323.0],  # [[base1_name, base1_weight], ...,  [baseN_name, baseN_weight]]
        ['B', 336.0], 
        ['D', 344.0], 
        ['G', 363.0], 
        ['H', 330.666666667], 
        ['K', 342.5], 
        ['M', 335.0],
        ['N', 338.75], 
        ['S', 343.0], 
        ['R', 355.0], 
        ['T', 322.0], 
        ['W', 334.5], 
        ['V', 344.333333333], 
        ['Y', 322.5], 
        ['X', 338.75]
        ]
    for seq in seq_file: # this for cycle is  for every line of the file
        weight = 0
        seq = seq.rstrip()
        for base in seq: # this for cycle is for every base in a given sequence
            for i in range(len(weights)): # this for cycle searches for the weight of the given base
                if base == weights[i][0]: # in the sequence in the weights list, then adds the weight
                    weight += weights[i][1] # to the total sequence weight.
        if weight < upper_weight and weight > lower_weight:
            print(seq, weight)  
#file = open('/home/stefano/Università/PB/sequences.seq', 'r')   
file = open('C:\\Users\\stefa\\Google Drive\\Università\\PB\\sequences.seq', 'r')      
seq_weight(file, 224245, 226940)
file.close()
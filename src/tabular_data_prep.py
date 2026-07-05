import numpy as np

def read_chord_sequence_file(infile, skip_first_note=True):
    ''' Reads a file and returns a list of chords, where each chord is a list of notes'''
    data = np.loadtxt(infile, delimiter=',', dtype=int)
    notes = []
    # flatten data into a list
    #data = list(data.flatten())
    data = data.flatten()

    if skip_first_note:
        return data[1:]
    else:
        return data


def displacement_data_generator_chords(infile):
    ''' Reads file and returns gaps between notes '''
    data = np.loadtxt(infile, delimiter=',', dtype=int)

    #featurs is an array of 
    features = np.zeros((data.shape[0], data.shape[1] - 3), dtype=int)
    print(features.shape)

    features[:, 0] = data[:, 2] - data[:, 1] #2nd not - 1st root
    features[:, 1] = data[:, 3] - data[:, 1] # 3rd note - 1st root
    features[:, 2] = data[:, 4] - data[:, 1] #4th note - 1st root
    features[:, 3] = data[:, 5] - data[:, 1] #c2n1 - c1n1
    features[:, 4] = data[:, 6] - data[:, 5] #c2n2 - c2n1
    features[:, 5] = data[:, 7] - data[:, 5] #c2n3 - c2n1
    features[:, 6] = data[:, 8] - data[:, 5] #c2n4 - c2n1
    features[:, 7] = data[:, 9] - data[:, 5] #c3n1 - c2n1
    features[:, 8] = data[:, 10] - data[:, 9] #c3n2 - c3n1
    features[:, 9] = data[:, 11] - data[:, 9] #c3n3 - c3n1
    features[:, 10] = data[:, 12] - data[:, 9] #c3n4 - c3n1
    features[:, 11] = data[:, 13] - data[:, 9] #c4n1 - c3n1
    features[:, 12] = data[:, 14] - data[:, 13] #c4n2 - c4n1
    features[:, 13] = data[:, 15] - data[:, 13] #c4n3
    features[:, 14] = data[:, 16] - data[:, 13] #c4n4


#    for i in range(3):
#        features[:, i] = data[:, i+1] - data[:, 0]

    labels = data[:, -1]

    return features, labels

def displacement_data_generator_chords2(infile):
    ''' Reads file and returns gaps between notes '''
    data = np.loadtxt(infile, delimiter=',', dtype=int)

    #featurs is an array of 
    features = np.zeros((data.shape[0], data.shape[1] - 3), dtype=int)
    print(features.shape)

    features[:, 0] = data[:, 2] - data[:, 1] #2nd note - 1st root
    features[:, 1] = data[:, 3] - data[:, 2] #3rd note - c1n2 
    features[:, 2] = data[:, 4] - data[:, 3] #c1n4 - c1n3
    features[:, 3] = data[:, 5] - data[:, 1] #c2n1 - c1n1
    features[:, 4] = data[:, 6] - data[:, 5] #c2n2 - c2n1
    features[:, 5] = data[:, 7] - data[:, 6] #c2n3 - c2n2
    features[:, 6] = data[:, 8] - data[:, 7] #c2n4 - c2n3
    features[:, 7] = data[:, 9] - data[:, 5] #c3n1 - c2n1
    features[:, 8] = data[:, 10] - data[:, 9] #c3n2 - c3n1
    features[:, 9] = data[:, 11] - data[:, 10] #c3n3 - c3n2
    features[:, 10] = data[:, 12] - data[:, 11] #c3n4 - c3n3
    features[:, 11] = data[:, 13] - data[:, 9] #c4n1 - c3n1
    features[:, 12] = data[:, 14] - data[:, 13] #c4n2 - c4n1
    features[:, 13] = data[:, 15] - data[:, 14] #c4n3 - c4n2
    features[:, 14] = data[:, 16] - data[:, 15] #c4n4 - c4n3


#    for i in range(3):
#        features[:, i] = data[:, i+1] - data[:, 0]

    labels = data[:, -1]

    return features, labels


def tabular_data_generator(infile, 
                           remove_zeros=True, 
                           relative_values=False,
                           remove_first_chord_column=True):
    ''' Takes a file, returns numpy array of features and labels
    assumes first column is index, last is label, rest are features'''
 
    data = np.loadtxt(infile, delimiter=',', dtype=int)
 
    #remove the first column, which is just an index
    data = data[:, 1:]

    if remove_zeros:
        #remove elements where final column is 0
        data = data[data[:, -1] != 0]
 
    if relative_values:
        # subtract column 0 from all columns except the last one
        data[:, :-1] = data[:, :-1] - data[:, 0][:, np.newaxis]

    if remove_first_chord_column:
        data = data[:, 1:]  
    

    features = data[:, :-1]
    labels = data[:, -1]

    return features, labels
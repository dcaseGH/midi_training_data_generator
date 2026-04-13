import numpy as np

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
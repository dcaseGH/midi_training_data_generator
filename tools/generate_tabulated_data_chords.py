'''
Reformat the data to be tabulated
'''

import glob

data_dir = 'data_090326'
tablulated_chords_data = []


csv_files = glob.glob(f'{data_dir}/chord_sequence*.csv')
#print(csv_files)
chord_data = {}
for f in csv_files:
    with open(f) as infile:
        fileid = f.split('/')[-1].split('_seed')[0].split('_')[-1]
        chord_data[fileid] = infile.read().replace('\n', ',')



with open('data_to_reformat/Best_chords') as infile:
    for l in infile.readlines():
        if 'total' in l:
            continue   
        filename = l.strip().split(' ')[-1]
        idnum = filename.split('_seed')[0].split('_')[-1]
        tablulated_chords_data.append(idnum + ',' + chord_data[idnum] + '1')

with open('data_to_reformat/Possible_chords') as infile:
    for l in infile.readlines():
        if 'total' in l:
            continue   
        filename = l.strip().split(' ')[-1]
        idnum = filename.split('_seed')[0].split('_')[-1]
        tablulated_chords_data.append(idnum + ',' + chord_data[idnum] + '0')

with open('data_to_reformat/Rejected_chords') as infile:
    for l in infile.readlines():
        if 'total' in l:
            continue   
        filename = l.strip().split(' ')[-1]
        idnum = filename.split('_seed')[0].split('_')[-1]
        tablulated_chords_data.append(idnum + ',' + chord_data[idnum] + '-1')

#reorder by id
tablulated_chords_data.sort(key=lambda x: int(x.split(',')[0]))

with open('tabulated_chords.csv', 'w') as outfile:
    for l in tablulated_chords_data:
        outfile.write(l + '\n')
#print(tablulated_chords_data)

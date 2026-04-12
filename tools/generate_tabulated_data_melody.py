'''
Reformat the data to be tabulated
'''

import glob

data_dir = 'data_090326'
tablulated_chords_data = []


csv_files = glob.glob(f'{data_dir}/chord_and_melody_sequence*.csv')
#print(csv_files)
chord_data = {}
for f in csv_files:
    with open(f) as infile:
        fileid = f.split('/')[-1].split('_seed')[0].split('_')[-1]
        chord_data[fileid] = infile.read().replace('\n', ',')

with open('data_to_reformat/Best_chords_melody') as infile:
    for l in infile.readlines():
        if 'total' in l:
            continue   
        filename = l.strip().split(' ')[-1]
        idnum = filename.split('_seed')[0].split('_')[-1]
        tablulated_chords_data.append(idnum + ',' + chord_data[idnum] + '1')

with open('data_to_reformat/possible_chords_melody') as infile:
    for l in infile.readlines():
        if 'total' in l:
            continue   
        filename = l.strip().split(' ')[-1]
        idnum = filename.split('_seed')[0].split('_')[-1]
        tablulated_chords_data.append(idnum + ',' + chord_data[idnum] + '0')

with open('data_to_reformat/rejected_chords_melody') as infile:
    for l in infile.readlines():
        if 'total' in l:
            continue   
        filename = l.strip().split(' ')[-1]
        idnum = filename.split('_seed')[0].split('_')[-1]
        tablulated_chords_data.append(idnum + ',' + chord_data[idnum] + '-1')

#reorder by id
tablulated_chords_data.sort(key=lambda x: int(x.split(',')[0]))

with open('tabulated_chords_melody_full.csv', 'w') as outfile:
    for l in tablulated_chords_data:
        outfile.write(l + '\n')

#remove all extra notes from melody
# 28 columns - remove (zero indexed) 
# so index 0 is id, 4*4 chords, 10 melody, 1 label: remove 18,19, 21,22, 24,25
cleaned_tabulated_chords_data = []
for pt in tablulated_chords_data:
    row_data = pt.split(',')
    cleaned_tabulated_chords_data.append(','.join(x for i,x in enumerate(row_data) 
                                                  if i not in [18,19, 21,22, 24,25]))
    

with open('tabulated_chords_melody.csv', 'w') as outfile:
    for l in cleaned_tabulated_chords_data:
        outfile.write(l + '\n')

#print(tablulated_chords_data)

import random
import shutil
import os

# Get the data, read tabulated_chords.csv and take 

good, bad, unsure = [], [], []
total_required = 33
sets_require = 5
root_seed = 0
root_data_dir = 'data_090326'


with open('tabulated_chords.csv', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        if len(parts) < 2:
            continue
        sequence, label, chords = parts[0], parts[-1], parts[1:-1]
        if label == '1' and len(good) < total_required:
            good.append([sequence, chords, label])
        elif label == '-1' and len(bad) < total_required:
            bad.append([sequence, chords, label])
        elif label == '0' and len(unsure) < total_required:
            unsure.append([sequence, chords, label])

#print (f'Good: {len(good)} sequences', good)
#print(bad)
#print(unsure)

union_set = good + bad + unsure
print(union_set, len(union_set))

# Reshuffle and put into sets 
for shuffle in range(0, sets_require):
    random.seed(root_seed)
    random.shuffle(union_set)
    #print(f'Seed: {seed} reshuffled set: {union_set}')
    with open(f'reshuffled_set_{shuffle}.csv', 'w') as f:
        for sequence, chords, label in union_set:
            f.write(f'{shuffle},{",".join(chords)}\n')

    #keep a set of results with answers as a check
    with open(f'reshuffled_set_{shuffle}_answers.csv', 'w') as f:
        for sequence, chords, label in union_set:
            f.write(f'{shuffle},{sequence},{",".join(chords)},{label}\n')

    #make a dir for shuffled files
    os.makedirs(f'shuffled_sets_{shuffle}', exist_ok=True)
    #copy reshuffled_set_{shuffle}.csv to the dir
    shutil.copy(f'reshuffled_set_{shuffle}.csv', f'shuffled_sets_{shuffle}/reshuffled_set_{shuffle}.csv')


    #copy a midi file with a changed name
    counter = 0
    for sequence, chords, label in union_set:
        shutil.copy(root_data_dir + f'/chord_sequence_{sequence}_seed_0.mid', 
                    f'shuffled_sets_{shuffle}/shuffled_{counter}_set_{shuffle}.mid')
        counter += 1

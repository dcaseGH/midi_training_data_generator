'''
Script to generate chord sequences
Not efficient but generalizable 
'''


import random
from src.four_note_chord_utils import pick_four_random_chords, generate_complete_list_from_root
from src.csv_templates import csv_template
from src.midi_csv_conversion import csv_to_midi

# Input data
number_chord_sequences = 1
all_chords = []
my_root = 58
my_chord_max_interval = [5,5,5]
random_seed = 0

random.seed(random_seed)



#with open(filename, 'w') as outfile:
def pick_four_random_chords(root, chord_max_interval):

    list_chords = generate_complete_list_from_root(root, chord_max_interval)
    first_chord = random.choice(list_chords)

    list_chords = generate_complete_list_from_root(first_chord[0] + random.randint(-5,5), chord_max_interval)
    second_chord = random.choice(list_chords)

    list_chords = generate_complete_list_from_root(second_chord[0] + random.randint(-5,5), chord_max_interval)
    third_chord = random.choice(list_chords)

    list_chords = generate_complete_list_from_root(third_chord[0] + random.randint(-5,5), chord_max_interval)
    fourth_chord = random.choice(list_chords)

    return (first_chord, second_chord, third_chord, fourth_chord)



for i in range(number_chord_sequences):
    csv_filename = f'chord_sequence_{i}_seed_{random_seed}.csv'
    with open(csv_filename, 'w') as outfile:
        outfile.write(csv_template(pick_four_random_chords(my_root, my_chord_max_interval)))
    csv_to_midi(csv_filename, csv_filename.replace('.csv', '.mid'))
#    print(csv_template(pick_four_random_chords(my_root, my_chord_max_interval)))


#print(first_chord)
# Generate complete list of 2nd chords



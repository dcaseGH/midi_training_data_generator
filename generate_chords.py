'''
Script to generate chord sequences
Not efficient but generalizable 


'''


import random


# Input data
number_chord_sequences = 10
all_chords = []
my_root = 58
my_chord_max_interval = [5,5,5]
random_seed = 0

random.seed(random_seed)

def generate_complete_list_from_root(root, chord_max_interval):
    ''' 4 note chord from root
        all notes within interval from preceding note '''

    chords_list = []

    for n2 in range(root + 1, root + chord_max_interval[0] + 1):
        for n3 in range(n2 + 1, n2 + chord_max_interval[1] + 1):
            for n4 in range(n3 + 1, n3 + chord_max_interval[2] + 1):
                #print(f'{root},{n2},{n3},{n4}')
                #chords_list.append(f'{root},{n2},{n3},{n4}')
                chords_list.append([root, n2, n3 , n4])

    return chords_list


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

#with open(filename, 'w') as outfile:


for i in range(number_chord_sequences):
    print(pick_four_random_chords(my_root, my_chord_max_interval))


#print(first_chord)
# Generate complete list of 2nd chords



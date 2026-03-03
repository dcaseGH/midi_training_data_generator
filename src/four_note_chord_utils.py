def generate_complete_list_from_root(root, chord_max_interval):
    ''' 4 note chord from root
        all notes within interval from preceding note '''

    chords_list = []

    for n2 in range(root + 1, root + chord_max_interval[0] + 1):
        for n3 in range(n2 + 1, n2 + chord_max_interval[1] + 1):
            for n4 in range(n3 + 1, n3 + chord_max_interval[2] + 1):
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


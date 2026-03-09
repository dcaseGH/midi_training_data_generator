def csv_template_chords(chords):
    time = 0
    timestep = 720
    output = '''0, 0, Header, 1, 2, 480
1, 0, Start_track
1, 0, Title_t, ""
1, 0, Time_signature, 4, 2, 24, 8
1, 0, Tempo, 500000
1, 0, End_track
2, 0, Start_track
2, 0, Control_c, 0, 121, 0
2, 0, Title_t, ""
2, 0, Control_c, 0, 10, 64
2, 0, Control_c, 0, 7, 100
2, 0, Control_c, 0, 11, 127
2, 0, Control_c, 0, 101, 0
2, 0, Control_c, 0, 100, 2
2, 0, Control_c, 0, 6, 64
2, 0, Control_c, 0, 101, 0
2, 0, Control_c, 0, 100, 1
2, 0, Control_c, 0, 6, 64
2, 0, Control_c, 0, 38, 0
2, 0, Control_c, 0, 101, 0
2, 0, Control_c, 0, 100, 0
2, 0, Control_c, 0, 6, 12
2, 0, Pitch_bend_c, 0, 8192
2, 0, Control_c, 0, 1, 0
2, 0, Program_c, 0, 0
'''
    for chord in chords:
        for note in chord:
            output += f'2, {time}, Note_on_c, 0, {note}, 100\n'
        for note in chord:
            output += f'2, {time+timestep}, Note_off_c, 0, {note}, 0\n'
        time += timestep

    output += f'''2, {time}, End_track
0, 0, End_of_file'''
    return output

# possibly better to just have all the notes in a list, with on and off beats?
# do this for now
def csv_template(chords, melody):
    time = 0
    timestep = 240
    nTracks = 2 #chords, melody
    crotchets_per_bar = 3 # for this particular track
    chord_volume = 80
    melody_volume = 100
    time_per_bar = crotchets_per_bar * timestep
    total_time =  time_per_bar * len(chords)    

    output = f'''0, 0, Header, 1, {nTracks}, 480
1, 0, Start_track
1, 0, Title_t, ""
1, 0, Time_signature, {crotchets_per_bar}, 2, 24, 8
1, 0, Tempo, 500000
1, 0, End_track
2, 0, Start_track
2, 0, Control_c, 0, 121, 0
2, 0, Title_t, ""
2, 0, Control_c, 0, 10, 64
2, 0, Control_c, 0, 7, 100
2, 0, Control_c, 0, 11, 127
2, 0, Control_c, 0, 101, 0
2, 0, Control_c, 0, 100, 2
2, 0, Control_c, 0, 6, 64
2, 0, Control_c, 0, 101, 0
2, 0, Control_c, 0, 100, 1
2, 0, Control_c, 0, 6, 64
2, 0, Control_c, 0, 38, 0
2, 0, Control_c, 0, 101, 0
2, 0, Control_c, 0, 100, 0
2, 0, Control_c, 0, 6, 12
2, 0, Pitch_bend_c, 0, 8192
2, 0, Control_c, 0, 1, 0
2, 0, Program_c, 0, 0
'''
    # write the chords
    for chord in chords:
        for note in chord:
            output += f'2, {time}, Note_on_c, 0, {note}, {chord_volume}\n'
        time += time_per_bar
        for note in chord:
            output += f'2, {time}, Note_off_c, 0, {note}, 0\n'
    output += f'2, {time}, End_track\n'

    # write the melody
    time = 0
    output += f'3, {time}, Start_track\n'
    for note in melody[:-1]:
        output += f'3, {time}, Note_on_c, 0, {note}, {melody_volume}\n'
        output += f'3, {time+timestep}, Note_off_c, 0, {note}, 0\n'
        time += timestep

    # last note of melody lasts until the end
    output += f'3, {time}, Note_on_c, 0, {melody[-1]}, {melody_volume}\n'
    time = total_time
    output += f'3, {time}, Note_off_c, 0, {melody[-1]}, 0\n'

    output += f'''3, {time}, End_track
0, 0, End_of_file'''
    return output


def stripped_csv_template_chords(chords):
    ''' Just the notes'''
    output = ''
    for chord in chords:
        output += ','.join([str(note) for note in chord]) + '\n'

    return output

def stripped_csv_template(chords, melody):
    ''' Just the notes'''

    output = stripped_csv_template_chords(chords)
    output += ','.join([str(note) for note in melody]) + '\n'

    return output
def csv_template(chords):
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

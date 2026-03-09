import py_midicsv as pm

# Interfaces to py_midicsv to write files
def csv_string_to_midi(csv_string, output_midi_file):
    midi_object = pm.csv_to_midi(csv_string.splitlines())
    with open(output_midi_file, "wb") as output_file:
        midi_writer = pm.FileWriter(output_file)
        midi_writer.write(midi_object)

def csv_to_midi(csv_file, output_midi_file):
    midi_object = pm.csv_to_midi(csv_file)
    with open(output_midi_file, "wb") as output_file:
        midi_writer = pm.FileWriter(output_file)
        midi_writer.write(midi_object)

def midi_to_csv(midi_file, output_csv_file):
    csv_string = pm.midi_to_csv(midi_file)
    with open(output_csv_file, "w") as f:
        f.writelines(csv_string)

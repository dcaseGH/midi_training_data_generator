import pygame
import time

def play_midi_file(midi_file):
    # Initialize the mixer
    pygame.mixer.init()
    
    try:
        # Load the MIDI file
        pygame.mixer.music.load(midi_file)
        print(f"Now playing: {midi_file}")
        
        # Start playback
        pygame.mixer.music.play()

        # Keep the script running while the music plays
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Check status 10 times per second
            
    except pygame.error as e:
        print(f"Error playing {midi_file}: {e}")
    finally:
        pygame.mixer.quit()

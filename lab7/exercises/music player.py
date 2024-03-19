import pygame
import keyboard
import os
import random

# Initialize pygame mixer
pygame.mixer.init()

# Load your songs
songs = [os.path.join(os.getcwd(), song) for song in os.listdir(os.getcwd()) if song.endswith('.mp3')]
current_song_index = 0
shuffle_mode = False
repeat_mode = None  # None, 'song', 'playlist'

# Function to play a song
def play_song():
    global current_song_index
    pygame.mixer.music.load(songs[current_song_index])
    pygame.mixer.music.play()

# Function to stop the music
def stop_song():
    pygame.mixer.music.stop()

# Function to play the next song
def next_song():
    global current_song_index
    if shuffle_mode:
        current_song_index = random.randint(0, len(songs) - 1)
    else:
        current_song_index = (current_song_index + 1) % len(songs)
    play_song()

# Function to play the previous song
def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    play_song()

# Function to toggle shuffle mode
def toggle_shuffle():
    global shuffle_mode
    shuffle_mode = not shuffle_mode
    print(f"Shuffle mode: {'On' if shuffle_mode else 'Off'}")

# Function to toggle repeat mode
def toggle_repeat():
    global repeat_mode
    repeat_modes = [None, 'song', 'playlist']
    repeat_mode = repeat_modes[(repeat_modes.index(repeat_mode) + 1) % len(repeat_modes)]
    print(f"Repeat mode: {repeat_mode if repeat_mode else 'Off'}")

# Function to change volume
def change_volume(change):
    volume = pygame.mixer.music.get_volume() + change
    volume = max(0, min(1, volume))  # Ensure volume is between 0 and 1
    pygame.mixer.music.set_volume(volume)
    print(f"Volume: {int(volume * 100)}%")

# Function to display current song
def display_current_song():
    song_name = os.path.basename(songs[current_song_index])
    print(f"Playing: {song_name}")

# Function to seek in the current song
def seek(seconds):
    current_pos = pygame.mixer.music.get_pos() / 1000  # Get current position in seconds
    new_pos = current_pos + seconds
    pygame.mixer.music.play(start=new_pos)
    print(f"Seeked to: {int(new_pos)} seconds")

# Play the first song initially
play_song()
display_current_song()

# Main loop
while True:
    if keyboard.is_pressed('space'):  # Play/Pause
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    elif keyboard.is_pressed('s'):  # Stop
        stop_song()
    elif keyboard.is_pressed('n'):  # Next song
        next_song()
        display_current_song()
    elif keyboard.is_pressed('p'):  # Previous song
        previous_song()
        display_current_song()
    elif keyboard.is_pressed('v+'):  # Increase volume
        change_volume(0.1)
    elif keyboard.is_pressed('v-'):  # Decrease volume
        change_volume(-0.1)
    elif keyboard.is_pressed('r'):  # Toggle repeat mode
        toggle_repeat()
    elif keyboard.is_pressed('f'):  # Toggle shuffle mode
        toggle_shuffle()
    elif keyboard.is_pressed('right'):  # Fast forward
        seek(10)
    elif keyboard.is_pressed('left'):  # Rewind
        seek(-10)

    # Check for song end
    if not pygame.mixer.music.get_busy():
        if repeat_mode == 'song':
            play_song()
        elif repeat_mode == 'playlist' or (not shuffle_mode and current_song_index < len(songs) - 1):
            next_song()
            display_current_song()
        elif shuffle_mode:
            next_song()
            display_current_song()


# BioNoise Generator v0.1
from pynput import keyboard
import pygame
import random
import threading

# Initialize pygame
pygame.init()
sound_files = ["rain.wav", "wind.wav", "chime.wav"]
sounds = [pygame.mixer.Sound(f) for f in sound_files]

def play_random_sound():
    sound = random.choice(sounds)
    sound.play()

def on_press(key):
    threading.Thread(target=play_random_sound).start()

def main():
    print("BioNoise is running. Type to generate ambient sound. Press ESC to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()

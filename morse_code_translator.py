# Morse code translator

# imports
import pygame
import time
import numpy as np
import tkinter as tk
from tkinter import ttk

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

pygame.mixer.init()

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char == ' ':
            morse_code += ' '
        else:
            morse_code += morse_code_dict[char] + ' '
    return morse_code

def morse_to_text(morse_code):
    text = ''
    for part in morse_code.split(' '):
        if part == '':
            text += ' '
        else: 
            for key, value in morse_code_dict.items():
                if part == value:
                    text += key
    return text

def generate_tone(frequency, duration_ms, volume):
    sample_rate = 44100
    volume = volume * 10

    t = np.linspace(0, duration_ms / 1000, int(sample_rate * duration_ms / 1000), endpoint=False)
    signal = volume * np.sin(2 * np.pi * frequency * t)

    # Convert signal to 2D array for stereo sound
    stereo_signal = np.array([signal, signal]).T  # Transpose the array

    # Ensure the array is C-contiguous
    stereo_signal = np.ascontiguousarray(stereo_signal)

    sound = pygame.sndarray.make_sound(stereo_signal.astype(np.int16))
    sound.play()
    pygame.time.delay(int(duration_ms) + 50)  # Add a small delay to ensure proper playback


def text_to_morse_sound(text, frequency, volume):
    morse_code = text_to_morse(text)

    # Set the speed of Morse code playback (adjust as needed)
    dot_duration = 0.2
    dash_duration = 3 * dot_duration
    space_duration = 2 * dot_duration


    for char in morse_code:
        if char == '.':
            generate_tone(frequency, dot_duration * 1000, volume)
            #time.sleep(dot_duration)
        elif char == '-':
            generate_tone(frequency, dash_duration * 1000, volume)
            #time.sleep(dash_duration)
        elif char == ' ':
            time.sleep(space_duration)

def translate_and_play():
    input_text = text_entry.get()
    frequency = float(frequency_entry.get())
    volume = float(volume_entry.get())
    
    # Translate text to Morse code and play the sound
    text_to_morse_sound(input_text, frequency, volume)

def update_frequency(val):
    frequency_entry.delete(0, 'end')
    frequency_entry.insert(0, val)

def update_volume(val):
    volume_entry.delete(0, 'end')
    volume_entry.insert(0, val)

# GUI setup
root = tk.Tk()
root.title("Morse Code Translator")

# Text Entry
text_label = ttk.Label(root, text="Enter Text:")
text_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

text_entry = ttk.Entry(root, width=30)
text_entry.grid(row=0, column=1, padx=10, pady=10)

# Frequency Entry
frequency_label = ttk.Label(root, text="Frequency (Hz):")
frequency_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

frequency_entry = ttk.Entry(root, width=10)
frequency_entry.insert(0, "500")  # Default frequency
frequency_entry.grid(row=1, column=1, padx=10, pady=10)

frequency_slider = ttk.Scale(root, from_=100, to=10000, orient=tk.HORIZONTAL, value=500, command=update_frequency)
frequency_slider.grid(row=1, column=2, padx=10, pady=10)

# Volume Entry
volume_label = ttk.Label(root, text="Volume:")
volume_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

volume_entry = ttk.Entry(root, width=10)
volume_entry.insert(0, "100")  # Default volume
volume_entry.grid(row=2, column=1, padx=10, pady=10)

volume_slider = ttk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, value=100, command=update_volume)
volume_slider.grid(row=2, column=2, padx=10, pady=10)

# Translate and Play Button
translate_button = ttk.Button(root, text="Translate and Play", command=translate_and_play)
translate_button.grid(row=3, column=0, columnspan=2, pady=20)

# Run the GUI
root.mainloop()
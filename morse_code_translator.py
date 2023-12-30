# Morse code translator

# imports
import pygame
import time
import numpy as np

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

def generate_tone(frequency, duration_ms):
    pygame.mixer.init()
    sample_rate = 44100
    volume = 1000

    t = np.linspace(0, duration_ms / 1000, int(sample_rate * duration_ms / 1000), endpoint=False)
    signal = volume * np.sin(2 * np.pi * frequency * t)

    # Convert signal to 2D array for stereo sound
    stereo_signal = np.array([signal, signal]).T  # Transpose the array

    # Ensure the array is C-contiguous
    stereo_signal = np.ascontiguousarray(stereo_signal)

    sound = pygame.sndarray.make_sound(stereo_signal.astype(np.int16))
    sound.play()
    pygame.time.delay(int(duration_ms) + 50)  # Add a small delay to ensure proper playback


def text_to_morse_sound(text):
    morse_code = text_to_morse(text)

    # Set the speed of Morse code playback (adjust as needed)
    dot_duration = 0.2
    dash_duration = 3 * dot_duration
    space_duration = 2 * dot_duration


    for char in morse_code:
        if char == '.':
            generate_tone(500, dot_duration * 1000)
            #time.sleep(dot_duration)
        elif char == '-':
            generate_tone(500, dash_duration * 1000)
            #time.sleep(dash_duration)
        elif char == ' ':
            time.sleep(space_duration)

if __name__ == "__main__":
    input_text = "Hello World"
    
    # text to Morse code sound
    text_to_morse_sound(input_text)

# Morse code translator

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

if __name__ == "__main__":
    input_text = "Hello World"
    
    # Encode text to Morse code
    morse_result = text_to_morse(input_text)
    print(f"Text to Morse Code: {morse_result}")

    # Decode Morse code to text
    text_result = morse_to_text(morse_result)
    print(f"Morse Code to Text: {text_result}")

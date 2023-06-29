import sys

# https://geekflare.com/fr/python-morse-code-translator/
CHARS_TO_MORSE_CODE_MAPPING = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '\'': '· − − − − ·',
    '!': '− · − · − −',
    '/': '− · · − ·',
    '(': '− · − − ·',
    ')': '− · − − · −',
    '&': '· − · · ·',
    ':': '− − − · · ·',
    ';': '− · − · − ·',
    '=': '− · · · −',
    '+': '· − · − ·',
    '-': '− · · · · −',
    '_': '· · − − · −',
    '"': '· − · · − ·',
    '$': '· · · − · · −',
    '@': '· − − · − ·',
}

if (len(sys.argv) == 1):
    sys.exit(1)

# function to encode plain English text to morse code
def to_morse_code(txt):
    morse_code = ''
    for char in txt:
        # checking for space
        # to add single space after every character and double space after every word
        if char == ' ':
            morse_code += '  '
        else:
            # adding encoded morse code to the result
            morse_code += CHARS_TO_MORSE_CODE_MAPPING[char.upper()] + ' '
    return morse_code

morse_code = sys.argv[1]
res = to_morse_code(morse_code)
print(res)

sys.exit(1)

# a ajouter :
# A space character is represented by a slash /
# If more than one argument are provided, merge them into a single string with each
# argument separated by a space character.
# If no argument is provided, do nothing or print an usage
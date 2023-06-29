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
    # only space and alphanumeric chars 
    # '.': '.-.-.-',
    # ',': '--..--',
    # '?': '..--..',
    # '\'': '· − − − − ·',
    # '!': '− · − · − −',
    # '/': '− · · − ·',
    # '(': '− · − − ·',
    # ')': '− · − − · −',
    # '&': '· − · · ·',
    # ':': '− − − · · ·',
    # ';': '− · − · − ·',
    # '=': '− · · · −',
    # '+': '· − · − ·',
    # '-': '− · · · · −',
    # '_': '· · − − · −',
    # '"': '· − · · − ·',
    # '$': '· · · − · · −',
    # '@': '· − − · − ·',
}

str = ''
if (len(sys.argv) == 1):
    print("You need more arguments")
    sys.exit(1)
elif (len(sys.argv) > 2):
    sys.argv.pop(0)
    str = ' '.join(sys.argv)
else:
    str = sys.argv[1]
# print(str)

# function to encode plain English text to morse code
def to_morse_code(str):
    morse_code = ''
    for char in str:
        if char.islower():
            char = char.upper()
        # checking for space
        # to add single space after every character and double space after every word
        if char == ' ':
            morse_code += '/ '
        elif char not in CHARS_TO_MORSE_CODE_MAPPING.keys():
            print("ERROR")
            sys.exit(1)
        else:
            # adding encoded morse code to the result
            morse_code += CHARS_TO_MORSE_CODE_MAPPING[char] + ' '
    return morse_code

morse_code = str
res = to_morse_code(morse_code)
print(res)

sys.exit(1)

# Morse
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
}

def to_morse(text):
    text = text.upper()
    res = ''
    for i in text:
        try:
            res += MORSE_CODE_DICT[i] + " "
        except KeyError:
            res += i + " "
    return res

def from_morse(text):
    text = text.split(" ")
    res = ''
    for value in text:
        for key in MORSE_CODE_DICT.keys():
            if MORSE_CODE_DICT[key] == value:
                res += key
                break
        else:
            res += value
    return res


# def from_morse(text):
#     text = text.split(" ")
#     res = ''
#     for value in text:
#         b = False
#         for key in MORSE_CODE_DICT.keys():
#             if MORSE_CODE_DICT[key] == value:
#                 res += key
#                 b = True
#         if b == False:
#             res += value
#         OR
#     return res


# print(to_morse("bible)"))
print(from_morse("-... .. -... .-.. . _"))

# print(MORSE_CODE_DICT.keys(text))

# parz poxarinum
key_text = input("Enter key: ")
text = input("Enter text: ")
which_func = input("To encrypt enter e\nTo decrypt enter d\n")
key = ""

alphabet = {}

ar = []

key_text = key_text.upper()
dict_ind = ord("A")
for letter in key_text:
    if letter not in key and ord("A") <= ord(letter) <= ord("Z"):
        key += letter
        ar.append(letter)
        alphabet[chr(dict_ind)] = letter
        dict_ind += 1

for letter in range(ord("A"), ord("Z") + 1):
    if chr(letter) not in key:
        key += chr(letter)
        ar.append(chr(letter))
        alphabet[chr(dict_ind)] = chr(letter)
        dict_ind += 1

def get_key_from_value(d, target_value):
    for key, value in d.items():
        if value == target_value:
            return key
    return None  # Return None if the value isn't found

def encrypt(text, alphabet):
    res = ""
    for letter in text:
        if ord("a") <= ord(letter) <= ord("z"):
            res += (alphabet[letter.upper()]).lower()
        elif ord("A") <= ord(letter) <= ord("A"):
            res += alphabet[letter]
        else:
            res += letter

    return res

def decrypt(text, alphabet):
    res = ""
    for letter in text:
        if ord("a") <= ord(letter) <= ord("z"):
            res += get_key_from_value(alphabet, letter.upper()).lower()
            # res += (alphabet[letter.upper()]).lower()
        elif ord("A") <= ord(letter) <= ord("A"):
            res += get_key_from_value(alphabet, letter)
            # res += alphabet[letter]
        else:
            res += letter

    return res

if which_func == "e" or which_func == "E":
    print(encrypt(text, alphabet))
elif which_func == "d" or which_func == "D":
    print(decrypt(text, alphabet))

# for key, value in alphabet.items():
#     print(key, value)


# key = state engineering university of armenia

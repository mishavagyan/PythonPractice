"""
Implement the keyword encoding and decoding for the Latin alphabet.
The keyword cipher uses a keyword to rearrange the letters in the
alphabet. You should add the provided keyword at the beginning of
the alphabet. A keyword is used as the key, which determines the letter
matchings of the cipher alphabet to the plain alphabet. The repeats of
letters in the word are removed, then the cipher alphabet is generated
with the keyword matching to A, B, C, etc. until the keyword is used up,
 whereupon the rest of the ciphertext letters are used in alphabetical
order, excluding those already used in the key.

Encryption:

The keyword is "Crypto"

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
"""

class Cipher:
    def __init__(self, keyword="Crypto"):
        self.__keyword = keyword
        self.__alphabet = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
        self.__equivalent = {}

        used_chars = set()
        i = 0
        for char in self.__keyword:
            if char.upper() not in used_chars:
                self.__equivalent[self.__alphabet[i]] = char.upper()
                used_chars.add(char.upper())
                i += 1

        for char in self.__alphabet:
            if char.upper() not in used_chars:
                self.__equivalent[self.__alphabet[i]] = char.upper()
                used_chars.add(char.upper())
                i += 1

        self.__reversed_equivalent = {v: k for k, v in self.__equivalent.items()}


    def encode(self, data):
        encoded_data = ""
        for char in data:
            if "A" <= char.upper() <= "Z":
                if char.isupper():
                    encoded_data += self.__equivalent[char.upper()]
                else:
                    encoded_data += self.__equivalent[char.upper()].lower()
            else:
                encoded_data += char
        return encoded_data


    def decode(self, data):
        decoded_data = ""
        for char in data:
            if "A" <= char.upper() <= "Z":
                if char.isupper():
                    decoded_data += self.__reversed_equivalent[char.upper()]
                else:
                    decoded_data += self.__reversed_equivalent[char.upper()].lower()
            else:
                decoded_data += char
        return decoded_data


if __name__ == "__main__":
    cipher = Cipher()
    print(cipher.encode("Hello world"))
    print(cipher.decode("Fjedhc dn atidsn"))
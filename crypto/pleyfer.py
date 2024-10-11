# key_text = input("Enter key: ")
key_text = "state engineering university of armenia"
text = input("Enter text: ")
# text = "some text with Zltter and some zzz"
which_func = input("To encrypt enter e\nTo decrypt enter d\n")
key = ""

ar = []

matrix = []
alphabet = {}

text = "".join(text.upper().split())
print(text)

key_text = key_text.upper()
dict_ind = ord("A")
for letter in key_text:
    if letter not in key and ord("A") <= ord(letter) <= ord("Z"):
        key += letter
        ar.append(letter)
        alphabet[letter] = []

for letter in range(ord("A"), ord("Z") + 1):
    if chr(letter) not in key:
        key += chr(letter)
        ar.append(chr(letter))
        alphabet[chr(letter)] = []

ar.remove("J")

ind = -1
for i in range(len(ar)):
    if i % 5 == 0:
        matrix.append([])
        ind += 1
    matrix[ind].append(ar[i])
    alphabet[ar[i]] = [ind, len(matrix[ind]) - 1]
        
for i in matrix:
    print(i)

def encrypt(text, matrix, alphabet):
    text = text.replace("J", "I")
    res = ""
    i = 0
    while i < len(text):
        if i == len(text) - 1 or ord(text[i]) == ord(text[i+1]):
            a = alphabet[text[i]][0]
            b = alphabet[text[i]][1]
            c = alphabet["Z"][0]
            d = alphabet["Z"][1]
        else:
            a = alphabet[text[i]][0]
            b = alphabet[text[i]][1]
            c = alphabet[text[i+1]][0]
            d = alphabet[text[i+1]][1]
            i+=1
        if a == c and b == d:
            res += "ZZ"
        elif a == c:
            res += matrix[c][(b+1)%5]
            res += matrix[a][(d+1)%5]
        elif b == d:
            res += matrix[(a+1)%5][d]
            res += matrix[(c+1)%5][b]
        else:
            res += matrix[a][d]
            res += matrix[c][b]
        i += 1
    print(res)
    return res

def decrypt(text, matrix, alphabet):
    res = ""
    i = 0
    while i < len(text):
        a = alphabet[text[i]][0]
        b = alphabet[text[i]][1]
        c = alphabet[text[i+1]][0]
        d = alphabet[text[i+1]][1]
        if a == c and b == d:
            res += matrix[a][b]
        elif a == c:
            res += matrix[a][(b+4)%5]
            res += matrix[a][(d+4)%5]
        elif b == d:
            res += matrix[(a+4)%5][b]
            res += matrix[(c+4)%5][b]
        else :
            res += matrix[a][d]
            res += matrix[c][b]
        i += 2
    print(res)
    return res


if which_func == "e":
    encrypt(text, matrix, alphabet)
elif which_func == "d":
    decrypt(text, matrix, alphabet)
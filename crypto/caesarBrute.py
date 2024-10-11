# brute_force
import enchant
d = enchant.Dict("en_US")
count = 26

def encrypt(text, key):
  encrypted = ""
  for i in text:
    if ord('A') <= ord(i) <= ord('Z'):
      encrypted += chr((ord(i) + key - ord('A')) % count + ord('A'))
    elif ord('a') <= ord(i) <= ord('z'):
      encrypted += chr((ord(i) + key - ord('a')) % count + ord('a'))
    else:
      encrypted += i
  return encrypted


def decrypt(text, key):
  decrypted = ""
  key = count - (key % count)
  decrypted = encrypt(text, key)
  return decrypted


text = input("Enter text: ")
text_splited = text.split()
j = 0

brute_res = {i: "" for i in range(26)}

valid_keys = [i for i in range(26)]
for j in range(len(text_splited)):
  keys_to_remove = []
  for i in valid_keys:
    word = decrypt(text_splited[j], i)
    check_word = ''.join(filter(str.isalpha, word))
    if d.check(check_word):
      brute_res[i] += f"{word} "
    else:
      keys_to_remove.append(i)
  for key in keys_to_remove:
      valid_keys.remove(key)

  if len(valid_keys) == 1:
    break

if valid_keys:
  print(f"key: {valid_keys[0]}")
  print(f"Decrypted text: {decrypt(text, valid_keys[0])}")
else:
  print("There is no key for this!")

import requests

def get_random_word():
    url = "https://random-word-api.herokuapp.com/word"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        random_word = response.json()[0]  # Extract the word from the JSON response
        return random_word
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

random_word = get_random_word()

if random_word:
    print("Random Word:", random_word)

print("Welcome to Guess Word Game")
win = False
res = ["_" for i in range(len(random_word))]
word = "".join(res) 
while not win:
    print(word)
    changes = False
    letter = input("Enter letter\n>> ")
    for index, l in enumerate(random_word):
        if l == letter:
            res[index] = l
            changes = True
    if not changes:
        print("OOOPS THERE IS NO SUCH A LETTER")
    word = "".join(res)
    if word == random_word:
        win = True
print(f"You Won!!!\nRight answer was '{word}'")

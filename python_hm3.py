# guess number game
import random

def start_end():
    b = True
    while b:
        start = input()
        end = input()
        try:
            start = int(start)
            end = int(end)
            if start < 0 or start >= end or end < 0:
                print("Invalid input. Please enter a valid number.")
            else:
                return start, end
        except ValueError:
            print("Invalid input. Please enter a valid number.")


print("Welcome to Guess Number Game\n\nIf you want to exit the game print exit!\n\nLet's start the game")
play = True
print("Enter [start, end]")
s_e = start_end()
secrete_number = random.randint(s_e[0], s_e[1])
# print("Secret: ", secrete_number)
guess = input("Enter your guess: ")
attempts = 1
message = ["Keep going", "Try again", "Don't give up"]
while play == True:
    try:
        if attempts % 5 == 0:
            random.shuffle(message)
            print(message[0])
        if guess == "exit":
            play = False
        elif int(guess) == secrete_number:  
            print("Yeeeey that's the secret number!\nYour attempts count =", attempts)
            play = False
        elif int(guess) > secrete_number:
            print("Your guess is too higher then the secrete number!")
            guess = input("Enter your guess: ")
            attempts += 1
        elif int(guess) < secrete_number:
            print("Your guess is too lower then the secrete number!")
            guess = input("Enter your guess: ")
            attempts += 1
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        guess = input("Enter your guess: ")

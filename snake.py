import os
import time
import random
from pynput.keyboard import Key, Listener

matrix_size = 13

matrix = []
pos_y = [6]
pos_x = [6]
eat_pos = [random.randint(1, matrix_size - 2), random.randint(1, matrix_size - 2)]
key_pressed = None


# Make matrix
for i in range(matrix_size):
    matrix.append([])
    for j in range(matrix_size):
        if i == 0 or i == matrix_size-1:
            matrix[i].append('*')
        elif 0 < i < matrix_size - 1 and (j == 0 or j == matrix_size-1):
            matrix[i].append('*')
        else:
            matrix[i].append(" ")

# function for printin matrix
def pr():
    os.system("clear")
    matrix[eat_pos[1]][eat_pos[0]] = "*"
    for i in range(len(pos_y)):
        matrix[pos_y[i]][pos_x[i]] = "#"
    for i in matrix:
        for j in i:
            print(j, " ", sep="", end="")
        print()
    print("Score:", len(pos_x) - 1)

def move_up():
    matrix[pos_y[0]][pos_x[0]] = " "
    new_pos_y = pos_y[-1] - 1
    if new_pos_y == 0:
        new_pos_y = matrix_size - 2 
    pos_y.append(new_pos_y)
    pos_y.pop(0)
    pos_x.append(pos_x[-1])
    pos_x.pop(0)

def move_right():
    matrix[pos_y[0]][pos_x[0]] = " "
    new_pos_x = pos_x[-1] + 1
    if new_pos_x == matrix_size - 1:
        new_pos_x = 1
    pos_y.append(pos_y[-1])
    pos_y.pop(0)
    pos_x.append(new_pos_x)
    pos_x.pop(0)

def move_down():
    matrix[pos_y[0]][pos_x[0]] = " "
    new_pos_y = pos_y[-1] + 1
    if new_pos_y == matrix_size - 1:
        new_pos_y = 1
    pos_y.append(new_pos_y)
    pos_y.pop(0)
    pos_x.append(pos_x[-1])
    pos_x.pop(0)

def move_left():
    matrix[pos_y[0]][pos_x[0]] = " "
    new_pos_x = pos_x[-1] - 1
    if new_pos_x == 0:
        new_pos_x = matrix_size - 2
    pos_y.append(pos_y[-1])
    pos_y.pop(0)
    pos_x.append(new_pos_x)
    pos_x.pop(0)

def eat():
    pos_y.insert(0, pos_y[0])
    pos_x.insert(0, pos_x[0])
    global eat_pos
    eat_pos = [random.randint(1, matrix_size - 2), random.randint(1, matrix_size - 2)]

def die():
    if (pos_y[-1], pos_x[-1]) in zip(pos_y[:-1], pos_x[:-1]):
        return True
    return False

def move_snake():
    if key_pressed == Key.up:
        move_up()
    elif key_pressed == Key.down:
        move_down()
    elif key_pressed == Key.right:
        move_right()
    elif key_pressed == Key.left:
        move_left()

def on_press(key):
    global key_pressed
    if key == Key.up and key_pressed != Key.down:
        key_pressed = key
    elif key == Key.down and key_pressed != Key.up:
        key_pressed = key
    elif key == Key.right and key_pressed != Key.left:
        key_pressed = key
    elif key == Key.left and key_pressed != Key.right:
        key_pressed = key
    
def on_release(key):
    if key == Key.esc:
        return False

listener = Listener(on_press=on_press)
listener.start()

while True:
    move_snake()
    if die():
        print()
        print("*" * 61)
        print("*" * 25, " Game Over ", "*" * 25, sep="")
        print("*" * 61)
        break
    if pos_y[-1] == eat_pos[1] and pos_x[-1] == eat_pos[0]:
        eat()
    pr()
    time.sleep(0.2)

listener.join()
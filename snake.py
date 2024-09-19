import os
import time
import random

matrix_size = 13

matrix = []
pos_y = [6]
pos_x = [6]
eat_pos = [random.randint(1, matrix_size - 2), random.randint(1, matrix_size - 2)]

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
    for i in range(len(pos_y)):
        matrix[pos_y[i]][pos_x[i]] = "#"
    matrix[eat_pos[1]][eat_pos[0]] = "*"
    for i in matrix:
        for j in i:
            print(j, " ", sep="", end="")
        print()
    print(eat_pos)
    time.sleep(0.07)
    
def move_up():
    matrix[pos_y[0]][pos_x[0]] = " "
    pos_y.append(pos_y[-1] - 1)
    pos_y.pop(0)
    pos_x.append(pos_x[-1])
    pos_x.pop(0)


def move_right():
    matrix[pos_y[0]][pos_x[0]] = " "
    pos_y.append(pos_y[-1])
    pos_y.pop(0)
    pos_x.append(pos_x[-1] + 1)
    pos_x.pop(0)

def move_down():
    matrix[pos_y[0]][pos_x[0]] = " "
    pos_y.append(pos_y[-1] + 1)
    pos_y.pop(0)
    pos_x.append(pos_x[-1])
    pos_x.pop(0)

def move_left():
    matrix[pos_y[0]][pos_x[0]] = " "
    pos_y.append(pos_y[-1])
    pos_y.pop(0)
    pos_x.append(pos_x[-1] - 1)
    pos_x.pop(0)

def eat():
    pos_y.insert(0, pos_y[0])
    pos_x.insert(0, pos_x[0])
    global eat_pos
    eat_pos = [random.randint(1, matrix_size - 2), random.randint(1, matrix_size - 2)]

# pr()
arr_x = []
arr_y = []

while True:
    while pos_y[-1] > 1:
        move_up()
        if pos_y[-1] == eat_pos[1] and pos_x[-1] == eat_pos[0]:
            eat()
            # eat_pos = [random.randint(1, matrix_size - 1), random.randint(1, matrix_size - 1)]
        pr()

    while pos_x[-1] > 1:
        move_left()
        if pos_y[-1] == eat_pos[1] and pos_x[-1] == eat_pos[0]:
            eat()
            # eat_pos = [random.randint(1, matrix_size - 1), random.randint(1, matrix_size - 1)]
        pr()

    while pos_y[-1] < matrix_size - 2:
        move_down()
        if pos_y[-1] == eat_pos[1] and pos_x[-1] == eat_pos[0]:
            eat()
            # eat_pos = [random.randint(1, matrix_size - 1), random.randint(1, matrix_size - 1)]
        pr()

    while pos_x[-1] < matrix_size - 2:
        move_right()
        if pos_y[-1] == eat_pos[1] and pos_x[-1] == eat_pos[0]:
            eat()
            # eat_pos = [random.randint(1, matrix_size - 1), random.randint(1, matrix_size - 1)]
        pr()

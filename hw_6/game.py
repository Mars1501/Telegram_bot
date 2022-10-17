
import random as r
import field as f

sign_empty = ''
sign_h = ''
sign_ai = ''
field = []


def is_cell_valid(data):
    x = data[0]
    y = data[1]
    if x < 0 or y < 0 or x >= 3 or y >= 3:
        return False
    return field[x][y] == sign_empty


def is_win(sign):
    for i in range(3):
        horizontal = field[i][0] == sign and field[i][1] == sign and field[i][2] == sign
        vertical = field[0][i] == sign and field[1][i] == sign and field[2][i] == sign
        if horizontal or vertical:
            return True
        diagonal_1 = field[0][0] == sign and field[1][1] == sign and field[2][2] == sign
        diagonal_2 = field[0][2] == sign and field[1][1] == sign and field[2][0] == sign
        if diagonal_1 or diagonal_2:
            return True
    return False


def check_win(sign, x, y):
    is_winner = False
    if is_cell_valid([x, y]):
        field[x][y] = sign
        if is_win(sign):
            is_winner = True
        field[x][y] = sign_empty
    return is_winner


def is_draw():
    for i in range(3):
        for j in range(3):
            if field[i][j] == sign_empty:
                return False
    return True


def turn_human():
    data = [-1, -1]
    while not is_cell_valid(data):
        data = [int(i) for i in input("Укажите ячейку: ").split()]
        data[0] = data[0] - 1
        data[1] = data[1] - 1
    field[data[0]][data[1]] = sign_h


def turn_ai():
    for i in range(len(field)):
        for j in range(len(field)):
            if check_win(sign_ai, i, j):
                field[i][j] = sign_ai
                return

    for i in range(len(field)):
        for j in range(len(field)):
            if check_win(sign_h, i, j):
                field[i][j] = sign_ai
                return

    data = [-1, -1]
    while not is_cell_valid(data):
        data[0] = r.randint(0, 3)
        data[1] = r.randint(0, 3)
    field[data[0]][data[1]] = sign_ai


def init_globals(user_field, user_sign_empty, user1_sign, user2_sign):
    global sign_empty, sign_h, sign_ai, field
    sign_empty = user_sign_empty
    sign_h = user1_sign
    sign_ai = user2_sign
    field = user_field


def run_game(user_field, user_sign_empty, user1_sign, user2_sign):

    init_globals(user_field, user_sign_empty, user1_sign, user2_sign)

    while True:
        turn_human()
        if is_win(sign_h):
            print("Человек победил!")
            break
        if is_draw():
            print("Ничья!")
            break

        turn_ai()
        f.print_field(field)
        if is_win(sign_ai):
            print("Робот победил!")
            break
        if is_draw():
            print("Ничья!")
            break

    print("Игра окончена!")
    f.print_field(field)
def init_field(field, sign):
    for i in range(3):
        field.append([sign for i in range(3)])


def print_field(field):
    for i in range(len(field)):
        for j in range(len(field)):
            print(field[i][j], end=' ')
        print()